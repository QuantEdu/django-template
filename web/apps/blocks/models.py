# Django core
from django.db import models

# External libraries
from model_utils.managers import InheritanceManager
from markdownx.models import MarkdownxField

# Our apps
import apps.results.models as result_models


# All lessons contains blocks (text, choice, question with float answer)
class Block(models.Model):
    time = models.SmallIntegerField(
        verbose_name='Время в минутах на выполнение блока',
        blank=True,
        default=5
    )
    max_score = models.SmallIntegerField(
        verbose_name='Балл за верное выполнение блока',
        blank=True,
        default=0
    )

    # From django-model-utils
    objects = InheritanceManager()

    class Meta:
        verbose_name = 'блок'
        verbose_name_plural = 'блоки'

    def __str__(self):
        return u'Block #{}'.format(self.pk)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('block-detail', args=[str(self.pk)])

    def get_class_name(self):
        class_name = self.__class__.__name__
        return class_name

    def get_subclass(self):
        return Block.objects.get_subclass(pk=self.pk)


# Block, that contains markdown content
class TextBlock(Block):
    title = models.CharField(max_length=200, unique=True)
    body = MarkdownxField()

    class Meta:
        verbose_name = 'блок: текст'
        verbose_name_plural = 'блоки: текст'

    def __str__(self):
        return u'"{}..."'.format(self.title[:20])

    @property
    def block_type_name(self):
        return u'Текст'

    def handle_answer_data(self, request, data):
        """
        Create result from form data
            Expecting format: {'block_pk': 2}
        and request object (need for associate result)
        """
        result = result_models.TextBlockResult.objects.create(
            block=self,
            is_read=True,
            user=request.user
        )
        result.set_score(new_score=1)


# Define where to store image
# Instance is an instanсe of model, that contains image
def choice_block_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/...
    return 'blocks/choice_blocks/choice_block_{0}/{1}'.format(
        instance.pk,
        filename)


# Block, that contains mono- or multiple choice
class ChoiceBlock(Block):
    question_text = MarkdownxField(verbose_name='Текст вопроса')
    answer_text = MarkdownxField(verbose_name='Решение')
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to=choice_block_image_directory_path,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'блок: выбор'
        verbose_name_plural = 'блоки: выбор'

    def __str__(self):
        return u'"{}..."'.format(self.question_text[:20])

    def block_type_name(self):
        if self.allow_multiple_answers:
            return u'Выбор ответов'
        else:
            return u'Выбор ответа'

    def get_options(self):
        options = ChoiceBlockOption.objects.filter(choice_block=self)
        return options

    def get_true_options(self):
        options = ChoiceBlockOption.objects.filter(choice_block=self, is_true=True)
        return options

    def get_options_by_pks(self, pks):
        options = ChoiceBlockOption.objects.filter(choice_block=self).filter(pk__in=pks)
        return options

    def handle_answer_data(self, request, data):
        """
        Create result from form data
            Expecting format: {'block_pk': 2, 'answers': ['4', '2', '1']}
        and request object (need for associate result)
        """
        # if we get radio select form result - convert data to array
        if not self.allow_multiple_answers():
            data['answers'] = [data['answers']]

        result = result_models.ChoiceBlockResult.objects.create(
            block=self,
            user=request.user,
            answers=data['answers']
        )
        result.set_score()

    def allow_multiple_answers(self):
        true_answers_count = self.get_options().filter(is_true=True).count()
        if true_answers_count == 1:
            return False
        else:
            return True


# Define where to store image
# Instance is an instanсe of model, that contains image
def choice_block_option_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/...
    return 'blocks/choice_blocks/choice_block_{0}/options/{1}/{2}'.format(
        instance.choice_block.pk,
        instance.pk,
        filename)


class ChoiceBlockOption(models.Model):
    choice_block = models.ForeignKey(
        ChoiceBlock,
        related_name='choices',
        on_delete=models.CASCADE
    )
    option_text = MarkdownxField(verbose_name='Вариант ответа')
    option_image = models.ImageField(
        verbose_name='Картинка',
        upload_to=choice_block_option_image_directory_path,
        null=True,
        blank=True
    )
    help_text = models.CharField(
        verbose_name='Подсказка',
        max_length=300,
        blank=True
    )
    is_true = models.BooleanField(verbose_name='Правильный?')

    class Meta:
        verbose_name = 'вариант ответа на тестовый вопрос'
        verbose_name_plural = 'варианты ответа на тестовые вопросы'

    def __str__(self):
        return self.option_text


# Define where to store image
# Instance is an instanсe of model, that contains image
def float_block_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/...
    return 'blocks/float_blocks/float_block_{0}/{1}'.format(
        instance.pk,
        filename)


# Block, that expect float answer
class FloatBlock(Block):
    question_text = MarkdownxField(verbose_name='Текст вопроса')
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to=float_block_image_directory_path,
        null=True,
        blank=True
    )
    true_answer = models.FloatField(verbose_name='Ответ')

    class Meta:
        verbose_name = 'блок: числовой ответ'
        verbose_name_plural = 'блоки: числовой ответ'

    def __str__(self):
        return u'"{}..."'.format(self.question_text[:20])

    @property
    def block_type_name(self):
        return u'Число'

    def handle_answer_data(self, request, data):
        """
        Create result from form data
            Expecting format: {'block_pk': 2, 'answer': '12.10'}
        and request object (need for associate result)
        """
        result = result_models.FloatBlockResult.objects.create(
            block=self,
            user=request.user,
            answer=data['answer']
        )
        result.set_score()


# Define where to store image
# Instance is an instanсe of model, that contains image
def text_answer_block_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/...
    return 'blocks/text_answer_blocks/text_answer_block_{0}/{1}'.format(
        instance.pk,
        filename)


# Block, that expect string answer
class TextAnswerBlock(Block):
    question_text = MarkdownxField(verbose_name='Текст вопроса')
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to=text_answer_block_image_directory_path,
        null=True,
        blank=True
    )
    true_answer = models.CharField('Ответ', max_length=600)

    class Meta:
        verbose_name = 'блок: текстовый ответ'
        verbose_name_plural = 'блоки: текстовый ответ'

    def __str__(self):
        return u'"{}..."'.format(self.question_text[:20])

    @property
    def block_type_name(self):
        return u'Строка'

    def handle_answer_data(self, request, data):
        """
        Create result from form data
            Expecting format: {'block_pk': 2, 'answer': '12.10'}
        and request object (need for associate result)
        """
        result = result_models.TextAnswerBlockResult.objects.create(
            block=self,
            user=request.user,
            answer=data['answer']
        )
        result.set_score()
