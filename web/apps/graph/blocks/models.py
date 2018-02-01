# Django core
from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect

# External libraries
from polymorphic.models import PolymorphicModel
from markdownx.models import MarkdownxField


# All lessons contains blocks (text, choice, question with float answer)
class Block(PolymorphicModel):
    time = models.SmallIntegerField(
        verbose_name='Время в минутах на выполнение блока',
        blank=True,
        default=5)
    score = models.SmallIntegerField(
        verbose_name='Балл за верное выполнение блока',
        blank=True,
        default=0)

    def __str__(self):
        return u'Block #{}'.format(self.id)

    class Meta:
        verbose_name = 'блок'
        verbose_name_plural = 'блоки'

    def get_absolute_url(self):
        return HttpResponseRedirect(reverse('blocks', args=[self.id]))


# Block, that contains markdown content
class TextBlock(Block):
    title = models.CharField(max_length=200, unique=True)
    body = MarkdownxField()

    class Meta:
        verbose_name = 'текстовая статья'
        verbose_name_plural = 'текстовые статьи'

    def __str__(self):
        return self.title[:100]


# Define where to store image
# Instance is an instanse of model, that contains image
def choice_block_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/...
    return 'blocks/choice_blocks/choice_block_{0}/{1}'.format(
        instance.pk,
        filename)


# Block, that contains mono- or multiple choice
class ChoiceBlock(Block):
    question_text = MarkdownxField(verbose_name='Текст вопроса')
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to=choice_block_image_directory_path,
        null=True,
        blank=True)

    class Meta:
        verbose_name = 'тестовый вопрос'
        verbose_name_plural = 'тестовые вопросы'

    def __str__(self):
        return self.question_text[:100]


# Define where to store image
# Instance is an instanse of model, that contains image
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
        on_delete=models.CASCADE)
    option_text = MarkdownxField(verbose_name='Вариант ответа')
    option_image = models.ImageField(
        verbose_name='Картинка',
        upload_to=choice_block_option_image_directory_path,
        null=True,
        blank=True)
    help_text = models.CharField(
        verbose_name='Подсказка',
        max_length=300,
        blank=True)
    is_true = models.BooleanField(verbose_name='Правильный?')

    class Meta:
        verbose_name = 'вариант ответа на тестовый вопрос'
        verbose_name_plural = 'варианты ответа на тестовые вопросы'

    def __str__(self):
        return self.option_text


# Define where to store image
# Instance is an instanse of model, that contains image
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
        blank=True)
    answer = models.FloatField(verbose_name='Ответ')

    class Meta:
        verbose_name = 'задача с численным ответом'
        verbose_name_plural = 'задачи с численным ответом'

    def __str__(self):
        return self.question_text[:100]


# Define where to store image
# Instance is an instanse of model, that contains image
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
        blank=True)
    answer = models.CharField('Ответ', max_length=600)

    class Meta:
        verbose_name = 'задача с текстовым ответом'
        verbose_name_plural = 'задачи с текстовым ответом'

    def __str__(self):
        return self.question_text[:100]


# Включение блоков в урок
# class NodeBlockRelation(models.Model):
#     node = models.ForeignKey('nodes.Node')
#     block = models.ForeignKey(Block)
#     order = models.IntegerField('Порядковый номер блока внутри узла', default=0)
#     # TODO
#     # подумать про order. Когда будет много вершин, порядок не выгоден,
#     # будет лучше между блоками сделать приоритет
#
#     class Meta:
#         verbose_name = 'включение блока в узел'
#         verbose_name_plural = 'включения блоков в узел'
#
#     def __str__(self):
#         return "{} in {}".format(self.block, self.node)
