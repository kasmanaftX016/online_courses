from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.core.mail import send_mail
from django.conf import settings
import random

# Tasdiqlash kodlarini vaqtinchalik saqlash
verification_codes = {}

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  
            user.save()

          
            code = str(random.randint(100000, 999999))
            verification_codes[user.email] = code

            
            send_mail(
                'Onlayn kurs platformasi - Email tasdiqlash',
                f'Sizning tasdiqlash kodingiz: {code}',
                settings.EMAIL_HOST_USER,  
                [user.email],               
                fail_silently=False,
            )

            # Emailni sessionda saqlash
            request.session['email'] = user.email
            return redirect('verify_code')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def verify_code(request):
    email = request.session.get('email')
    if not email:
        return redirect('register')

    if request.method == "POST":
        input_code = request.POST.get('code')
        if verification_codes.get(email) == input_code:
            from django.contrib.auth.models import User
            user = User.objects.get(email=email)
            user.is_active = True
            user.save()
            verification_codes.pop(email)
            return redirect('login')
        else:
            error = "Kod noto‘g‘ri"
            return render(request, 'users/verify_code.html', {'error': error})
    return render(request, 'users/verify_code.html')
