from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя", null=True)
    last_name = models.CharField(max_length=255, verbose_name="фамилия", null=True)
    age = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название группы")
    students = models.ManyToManyField("core.Student", blank=True)
    teacher_name = models.CharField(
        max_length=255,
        verbose_name="Имя учителя",
        null=True
    )

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    age = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return self.name
