from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Teacher, Schedule, ScheduleLesson, Student, PassedLessons


@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Teacher info'), {'fields': ('schedule', 'passed_lessons')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'schedule')
    filter_horizontal = ('groups', 'user_permissions', 'passed_lessons')

admin.site.register(Schedule)
admin.site.register(ScheduleLesson)
admin.site.register(Student)
admin.site.register(PassedLessons)