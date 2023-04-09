from django import forms 
from .models import *
import random
import string

class TeacherForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=50)
    surname = forms.CharField(label='Фамилия', max_length=50)
    email = forms.EmailField(label='Email', required=False)
    number_phone = forms.IntegerField(label='Номер телефона', )
    organization = forms.CharField(label='Название компании', max_length=100)

    name.widget.attrs.update({'class': 'form-control'})
    surname.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    number_phone.widget.attrs.update({'class': 'form-control'})
    organization.widget.attrs.update({'class': 'form-control'})
    # def clean_

    def save(self):
        teacher_post = Teacher_Post.objects.create(
            name=self.cleaned_data['name'],
            surname=self.cleaned_data['surname'],
            email=self.cleaned_data['email'],
            number_phone=self.cleaned_data['number_phone'],
            organization=self.cleaned_data['organization']
        )
        return teacher_post

    
class CheckTeacher(forms.Form):
    label_random = random.sample(string.ascii_letters+str(string.digits), random.randint(5, 67))
    label_random = ''.join(label_random)
    email = forms.EmailField(label='Email', required=False)
    success_check = forms.BooleanField(initial=False, required=False)
    delete_check = forms.BooleanField(initial=False, required=False)
    def save(self):
        if self.cleaned_data['success_check']==True:
            check_post = Teacher_Post.objects.filter(
                email=self.cleaned_data['email']
            ).update(                                                                                                                                                                                                                                                           
                success_check=self.cleaned_data['success_check']
            )
        if self.cleaned_data['delete_check']==True:
            check_post = Teacher_Post.objects.filter(
                email=self.cleaned_data['email']
                ).delete()
        return check_post