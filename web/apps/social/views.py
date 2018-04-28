# Django core
from django import forms
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.contrib.auth import login

from .models import VKAuth
from apps.users.models import User


class RegistrationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    photo = forms.CharField(widget=forms.HiddenInput)
    uid = forms.CharField(widget=forms.HiddenInput)


def vk_complete(request):
    if request.method == 'GET':
        uid = request.GET.get('uid', '')
        first_name = request.GET.get('first_name', '')
        last_name = request.GET.get('last_name', '')
        photo = request.GET.get('photo', '')
        photo_rec = request.GET.get('photo_rec', '')
        hash = request.GET.get('hash', '')

        try:
            vk_auth = VKAuth.objects.get(uid=uid)
            if request.user.is_authenticated:
                return redirect('lms:index')
            else:
                user = vk_auth.user
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('lms:index')
        except VKAuth.DoesNotExist:
            if request.user.is_authenticated:
                vk_auth = VKAuth.objects.create(
                    uid=uid,
                    user=request.user,
                    hash=hash,
                    first_name=first_name,
                    last_name=last_name,
                    photo=photo
                )
                vk_auth.save()
                return redirect('lms:index')
            else:
                context = {
                    'form': RegistrationForm(initial={
                        'uid': uid,
                        'first_name': first_name,
                        'last_name': last_name,
                        'photo': photo
                    }),
                    'photo': photo
                }
                return render(request, 'social/registration.html', context)


def vk_reg(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            User
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