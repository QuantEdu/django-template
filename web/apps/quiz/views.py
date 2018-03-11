# Django core
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView

from apps.blocks.forms import (ChoiceBlockForm, FloatBlockForm,
                               TextAnswerBlockForm, TextBlockForm)
# Our apps
from apps.blocks.models import (ChoiceBlock, FloatBlock, TextAnswerBlock,
                                TextBlock)

from .models import Quiz, QuizProgress


def get_block_form_class(block):
    if block.__class__ is TextBlock:
        return TextBlockForm
    elif block.__class__ is ChoiceBlock:
        return ChoiceBlockForm
    elif block.__class__ is FloatBlock:
        return FloatBlockForm
    elif block.__class__ is FloatBlock:
        return FloatBlockForm
    elif block.__class__ is TextAnswerBlock:
        return TextAnswerBlockForm
    else:
        raise Exception('Unknown type of block')


@login_required
def quiz_take(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)

    if request.method == 'POST':
        progress = QuizProgress.objects.user_progress(request.user, quiz)      # get current progress
        current_block = progress.get_next_block()                              # get current block, we expect in form data
        block_form_class = get_block_form_class(current_block)                 # define current block type and his form type
        form = block_form_class(request.POST, block=current_block)             # searching for this form data on page
        if form.is_valid():
            current_block.handle_answer_data(request, form.cleaned_data)
            progress.go_to_next_block()
            if progress.complete:
                return redirect('quiz_result', pk)
        else:
            context = {
                'quiz': quiz,
                'progress': progress,
                'next_block': current_block,
                'block_form': form
            }
            return render(request, 'quiz/quiz_take.html', context)
    else:
        progress = QuizProgress.objects.user_progress(request.user, quiz)      # always reload progress for non-post requests

    if not progress.complete:
        next_block = progress.get_next_block()                                 # get next block to render
        block_form_class = get_block_form_class(next_block)                    # get form class for next block
        block_form = block_form_class(block=next_block)                        # Fill this form with block data
        context = {
            'quiz': quiz,
            'progress': progress,
            'next_block': next_block,
            'block_form': block_form
        }
        return render(request, 'quiz/quiz_take.html', context)
    else:
        return redirect('quiz_results', pk)


class QuizListView(ListView):
    model = Quiz

    def get_queryset(self):
        queryset = super(QuizListView, self).get_queryset()
        return queryset


@method_decorator(login_required, name='dispatch')
class QuizDetailView(DetailView):
    model = Quiz

    def get_context_data(self, **kwargs):
        progresses = QuizProgress.objects.filter(user=self.request.user, quiz=self.object).order_by('-end_time')

        if progresses.filter(complete=False).count() == 0:
            has_incomplete_progress = False
        else:
            has_incomplete_progress = True

        context = super().get_context_data(**kwargs)
        context['fresh'] = self.kwargs.get('fresh', False)
        context['progresses'] = progresses
        context['has_incomplete_progress'] = has_incomplete_progress
        return context


@method_decorator(login_required, name='dispatch')
class QuizProgressView(DetailView):
    model = QuizProgress
    template_name = 'quiz/quiz_progress.html'
