from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from accounts.forms import RegistrationForm, LoginForm


# @login_required
class AccountView(TemplateView):
    template_name = "accounts/my-account.html"

    def get(self, request):
        args = {'user': request.user}
        return render(request, self.template_name, args)

    def post(self, request):
        args = {'user': request.user}
        return render(request, self.template_name, args)


class LoginRegisterView(TemplateView):
    template_name = "accounts/login-register.html"

    def get(self, request):
        register_form = UserCreationForm()
        login_form = LoginForm()
        args = {'register_form': register_form,
                'login_form': login_form}
        return render(request, self.template_name, args)

    def post(self, request):
        register_form = UserCreationForm(request.POST)
        login_form = LoginForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            raw_password = register_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accounts:accounts')
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('accounts:accounts')
        args = {'register_form': register_form,
                'login_form': login_form}
        return render(request, self.template_name, args)

#
# # 改密码
# @login_required
# def change_password(request):
#     if request.method == "POST":
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect('/accounts/profile')
#         else:
#             return redirect('/accounts/change-password')
#     else:
#         form = PasswordChangeForm(user=request.user)
#         args = {'form': form}
#         return render(request, 'accounts/change_password.html', args)
#
#
# # 登出
# def logout_view(request):
#     logout(request)
#     return redirect('home:index')
#
