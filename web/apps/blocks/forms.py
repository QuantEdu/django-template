# Django core
from django import forms


class TextBlockForm(forms.Form):
    block_pk = forms.IntegerField(label='block_pk', widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        block = kwargs.pop('block', None)
        super().__init__(*args, **kwargs)
        if block:
            self.initial['block_pk'] = block.pk


class ChoiceBlockForm(forms.Form):
    block_pk = forms.IntegerField(label='block_pk', widget = forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        block = kwargs.pop('block', None)
        super().__init__(*args, **kwargs)
        if block:
            self.initial['block_pk'] = block.pk
            block_options = block.get_options()
            choice_list = [(option.id, option.option_text) for option in block_options]
            if block.allow_multiple_answers():
                self.fields['answers'] = forms.MultipleChoiceField(
                    label="Ответы:",
                    widget=forms.CheckboxSelectMultiple,
                    choices=choice_list,
                    required=True
                )
            else:
                self.fields['answers'] = forms.ChoiceField(
                    label="Ответы:",
                    widget=forms.RadioSelect,
                    choices=choice_list,
                    required=True
                )


class FloatBlockForm(forms.Form):
    block_pk = forms.IntegerField(label='block_pk', widget=forms.HiddenInput())
    answer = forms.FloatField(label='Ответ')

    def __init__(self, *args, **kwargs):
        block = kwargs.pop('block', None)
        super().__init__(*args, **kwargs)
        if block:
            self.initial['block_pk'] = block.pk


class TextAnswerBlockForm(forms.Form):
    block_pk = forms.IntegerField(label='block_pk', widget=forms.HiddenInput())
    answer = forms.CharField(label='Ответ')

    def __init__(self, *args, **kwargs):
        block = kwargs.pop('block', None)
        super().__init__(*args, **kwargs)
        if block:
            self.initial['block_pk'] = block.pk
