from django.shortcuts import render
from .models import Student, ScheduleLesson, Schedule, \
                    PassedLessons, Teacher
from django.views import generic

class IndexDetailView(generic.ListView):
    template_name = 'notebook/index.html'
    model = ScheduleLesson

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return ScheduleLesson.objects.filter(teacher=user).order_by('start_time')
        else: return ScheduleLesson.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user'] = self.request.user
        return context