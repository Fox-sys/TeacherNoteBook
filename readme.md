# Teachers Note Book is a web service made for tutors. In fact, it is a site that makes it possible to easily make a schedule and calculate payment for lessons. 

## starting on dev server:

1) mkdir TeachersNoteBook && cd TeachersNoteBook
2) git clone https://github.com/Fox-sys/TeacherNoteBook.git
3) sudo docker-compose up -d --build
4) sudo docker-compose exec web python manage.py createsuperuser

## developing with:

- python 3.8.5
- django 3.2.0
- PostgreSQL 12.0
- Docker and Docker Compose


## Patch Note:

### Version: 0.1.0

- Added first models and some setting in admin
