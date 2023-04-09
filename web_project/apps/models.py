from django.db import models


class Teacher_Post(models.Model):
    name = models.CharField(("Имя"), max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    email = models.EmailField('E-mail', max_length=50)
    number_phone = models.IntegerField('Номер телефона', blank=True)
    organization = models.CharField('Название компании', max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    success_check = models.BooleanField(default=False)
    delete_post = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    