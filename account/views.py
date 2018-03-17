from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from account.forms import UserCreateForm
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
User = get_user_model()
from django.http import Http404
from braces.views import SelectRelatedMixin

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = "accounts/signup.html"

    def get_queryset(self):
        try:
            self.user = User.objects.get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.user

