# Django core
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout

from .models import UserSocialAuth
from apps.crm.users import User


class RegistrationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    photo = forms.CharField(widget=forms.HiddenInput)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    uid = forms.CharField(widget=forms.HiddenInput)


# Url, where user redirects after success vk authorization
def vk_complete(request):
    uid = request.GET.get('uid', '')
    first_name = request.GET.get('first_name', '')
    last_name = request.GET.get('last_name', '')
    photo = request.GET.get('photo', '')
    hash = request.GET.get('hash', '')
    # if only redirects, detect current authorization and existing of vk auth
    if request.method == 'GET':
        try:
            # if user is authenticated and already have vk integration - do nothing
            vk_auth = UserSocialAuth.objects.get(uid=uid, provider='vk')
            if request.user.is_authenticated:
                if request.user == vk_auth.user:
                    return redirect('lms:index')
                else:
                    logout(request)
                    return redirect('login')
            else:
                login(request, vk_auth.user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('lms:index')
        except UserSocialAuth.DoesNotExist:
            if request.user.is_authenticated:
                vk_auth = UserSocialAuth.objects.create(
                    uid=uid,
                    user=request.user,
                    provider='vk',
                    hash=hash
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
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            uid = form.cleaned_data['uid']

            new_user = User.objects.create_user(email, password, first_name=first_name, last_name=last_name)

            vk_auth = UserSocialAuth.objects.create(
                uid=uid,
                user=new_user,
                provider='vk',
                hash=hash,
                first_name=first_name,
                last_name=last_name,
                photo=photo
            )
            vk_auth.save()

            login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('lms:index')
        else:
            form = RegistrationForm(request.POST)
            context = {
                'form': form,
                'photo': photo
            }
            return render(request, 'social/registration.html', context)
