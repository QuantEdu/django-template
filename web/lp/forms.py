from django import forms
from django.core.mail import send_mail


class LeadForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()

    def create_lead(self, form):
        # send email using the self.cleaned_data dictionary
        name = form.cleaned_data.get('name')
        phone = form.cleaned_data.get('phone')
        send_mail(
            'Новая заявка от клиента {}'.format(name),
            'Новая заявка от "{}". Позвонить по телефону {}'.format(name, phone),
            'info@quant.zone',
            ['clients@quant.zone'],
            fail_silently=False,
        )
