from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.db.models import Q
from core.models import Student, Teacher
from core.forms import GroupCreateForm


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        teachers = Teacher.objects.all()
        context = {
            'teachers': teachers
        }
        if 'filter' in self.request.GET:
            context['filter'] = self.request.GET['filter']
            teachers = teachers.filter(
                Q(age__contains=self.request.GET['filter']) |
                Q(first_name__contains=self.request.GET['filter']) |
                Q(last_name__contains=self.request.GET['filter'])
            )
            context['teachers'] = teachers
        return context


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
