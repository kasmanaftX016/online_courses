from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Teacher, Course, Subject, Lesson, Contact

@admin.register(Teacher)
class TeacherAdmin(TranslatableAdmin):
    list_display = ['user', 'expertise']

@admin.register(Course)
class CourseAdmin(TranslatableAdmin):
    list_display = ['title', 'teacher', 'level', 'created_at']

@admin.register(Subject)
class SubjectAdmin(TranslatableAdmin):
    list_display = ['title', 'course', 'order']

@admin.register(Lesson)
class LessonAdmin(TranslatableAdmin):
    list_display = ['title', 'subject', 'order', 'duration']

@admin.register(Contact)
class ContactAdmin(TranslatableAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']

