from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    schedule = models.ForeignKey('Schedule', on_delete=models.SET_NULL, null=True, blank=True)
    passed_lessons = models.ManyToManyField('PassedLessons', 'прошедшие_уроки', blank=True)

    def __str__(self):
        return f'({self.id}) - {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Schedule(models.Model):
    monday = models.ManyToManyField('ScheduleLesson', 'Понедельник', blank=True)
    tuesday = models.ManyToManyField('ScheduleLesson', 'Вторник', blank=True)
    wednesday = models.ManyToManyField('ScheduleLesson', 'Среда', blank=True)
    thursday = models.ManyToManyField('ScheduleLesson', 'Четверг', blank=True)
    friday = models.ManyToManyField('ScheduleLesson', 'Пятница', blank=True)
    saturday = models.ManyToManyField('ScheduleLesson', 'Суббота', blank=True)
    sunday = models.ManyToManyField('ScheduleLesson', 'Воскресенье', blank=True)

    def __str__(self):
        try:
            teacher = Teacher.objects.get(schedule=self.id)
            return f'({self.id}) - {teacher.first_name} {teacher.last_name}'
        except Exception:
            return f'({self.id})'
        
    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class ScheduleLesson(models.Model):
    subject = models.CharField('Предмет', max_length=150)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    start_time = models.TimeField('Начало урока')
    end_time = models.TimeField('Конец урока')
    price = models.PositiveSmallIntegerField('Цена')

    def __str__(self):
        return f'{self.subject} - {self.student}'
        
    class Meta:
        verbose_name = 'Планируемый урок'
        verbose_name_plural = 'Планируемые уроки'


class Student(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    schedule = models.ForeignKey('Schedule', null=True, on_delete=models.SET_NULL, blank=True)
    creator = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
        
    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class PassedLessons(models.Model):
    schedule_lesson = models.ForeignKey('ScheduleLesson', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField()

    def __str__(self):
        return f'{self.date}, {self.schedule_lesson.price}'

    class Meta:
        verbose_name = 'Законченный урок'
        verbose_name_plural = 'Законченные уроки'
