from django.contrib import admin
from core.models import Student, Group, Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', )


admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Teacher, TeacherAdmin)
