from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .form import Form_Register
from .models import User
# Create your views here.
class RegisterView(View):
    def get(self , request):
        form = Form_Register()
        context = {
            "form" : form
        }
        return render(request , "register/register.html" , context)
    def post(self , request):
        form = Form_Register(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            passwd = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")
            user : bool = User.objects.filter(email__exact=email).exists()
            if user:
                raise Http404("Your email is already saved")
            else :
                new_user = User(email=email , username=username)
                new_user.set_password(passwd)

                new_user.save()
                return redirect(reverse("ProductView"))