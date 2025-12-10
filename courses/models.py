from django.db import models
from django.contrib.auth.models import User
from parler.models import TranslatableModel, TranslatedFields



class Teacher(TranslatableModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.CharField(max_length=500, blank=True)

    translations = TranslatedFields(
        bio = models.TextField(),
        expertise = models.CharField(max_length=200),
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username



class Course(TranslatableModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        description = models.TextField(),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

    def __str__(self):
         return self.safe_translation_getter('title', any_language=True)



class Subject(TranslatableModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects')

    translations = TranslatedFields(
        title = models.CharField(max_length=200),
    )

    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)




class Lesson(TranslatableModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='lessons')

    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        content = models.TextField(),
    )

    video_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    duration = models.CharField(max_length=20)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)




class Contact(TranslatableModel):
    translations = TranslatedFields(
        subject = models.CharField(max_length=200),
        message = models.TextField(),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.safe_translation_getter('subject', any_language=True)}"
