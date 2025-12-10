from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Course, Subject, Lesson, Teacher, Contact
from .forms import ContactForm


def base(request):
    return render(request,'courses/base.html')


def home(request):
    courses = Course.objects.all()[:6]
    return render(request, 'courses/home.html', {'courses': courses})

def courses_list(request):
    courses_all = Course.objects.all()
    paginator = Paginator(courses_all, 6)
    page = request.GET.get('page')
    courses = paginator.get_page(page)
    return render(request, 'courses/courses.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    subjects = course.subjects.all()
    return render(request, 'courses/course_detail.html', {'course': course, 'subjects': subjects})

def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})

def teachers_list(request):
    teachers_all = Teacher.objects.all()
    paginator = Paginator(teachers_all, 8)
    page = request.GET.get('page')
    teachers = paginator.get_page(page)
    return render(request, 'courses/teachers.html', {'teachers': teachers})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)

            contact.set_current_language('uz')  

            contact.subject = form.cleaned_data['subject']
            contact.message = form.cleaned_data['message']

            contact.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'courses/contact.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'courses/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')