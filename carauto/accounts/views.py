from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View

from accounts.forms import UserRegisterForm


class RegisterView(View):
    form = UserRegisterForm()
    template_name = "accounts/register.html"

    def get(self, request):
        return render(request, self.template_name, {"form": self.form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Account created for {username} successfuly, please log in!"
                )
            return redirect("login")
        else:
            messages.warning(
                request,
                'Something wrong with your data, check all info one more time.'
                )
            return redirect('register')


