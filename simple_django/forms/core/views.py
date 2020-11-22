from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from core.models import Student, Group
from core.forms import GroupCreateForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        groups = Group.objects.all().values('name')
        students = Student.objects.all().values('name')
        return {
                'students': students,
                'groups': groups,
            }


class StudentCreateView(CreateView):
    template_name = 'create_student.html'
    success_url = '/'
    model = Student
    fields = '__all__'


class GroupCreateView(FormView):
    template_name = 'create_group.html'
    form_class = GroupCreateForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(GroupCreateView, self).form_valid(form)
