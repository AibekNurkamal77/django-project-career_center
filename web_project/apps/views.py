from django.shortcuts import render, redirect

from django.views.generic import View
from .models import Teacher_Post
from .forms import *


def Index(request):
    teacher = Teacher_Post.objects.filter(success_check=False)
    check_post = CheckTeacher(request.POST or None)
    if check_post.is_valid():
        new_check = check_post.save()
        return redirect('/')
    return render(request, 'apps/index.html', {'forms': teacher, 'check_post': check_post})


class TeacherCreate(View):
    def get(self, request):
        form = TeacherForm()
        return render(request, 'apps/teacher_create.html', {'forms': form})
    
    def post(self, request):
        bound_form = TeacherForm(request.POST)

        if bound_form.is_valid():
            new_form = bound_form.save()
            return redirect(request.META.get('teacher_create_url', '/'))
        


# AUTH | REGISTRETION

def AuthCreate(request):

    return render(request, 'apps/auth_register.html')