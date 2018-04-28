# Django core
from django import forms
from django.views.generic.edit import FormView


class RegistrationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    uid = forms.HiddenInput()

    def register(self):
        # send email using the self.cleaned_data dictionary
        pass


def vk_complete(request):

    if request.method == 'GET':
        uid = request.GET.get('uid', '')
        first_name = request.GET.get('first_name', '')
        last_name = request.GET.get('last_name', '')
        photo = request.GET.get('photo', '')
        photo_rec = request.GET.get('photo_rec', '')
        hash = request.GET.get('hash', '')
        # if user already exist - check authorization hash and authorize in django
        # if user not exist - create a new one and take to user creation form
        return True


class RegistrationView(FormView):
    template_name = 'social/registration.html'
    form_class = RegistrationForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.register()
        return super().form_valid(form)
