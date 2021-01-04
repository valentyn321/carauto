from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView

from accounts.forms import UserRegisterForm

from poll.models import SearchModel


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


# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html', {})

class LastPollsListView(ListView):
    template_name = "accounts/profile.html"
    context_object_name = 'searches'
    
    def get_queryset(self):
        queryset = SearchModel.objects.filter(user=self.request.user)
        return queryset