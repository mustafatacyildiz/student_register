# PRECLASS SETUP

```bash
# CREATING VIRTUAL ENVIRONMENT
# windows
py -m venv env
# windows other option
python -m venv env
# linux / Mac OS
python3 -m venv env

# ACTIVATING ENVIRONMENT
# windows
.\env\Scripts\activate
# linux / Mac OS
source env/bin/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django
# alternatively python -m pip install django

python -m django --version
django-admin startproject student_project .

pip install python-decouple
pip freeze > requirements.txt
```
add a gitignore file at same level as env folder

create a new file and name as .env at same level as env folder

copy your SECRET_KEY from settings.py into this .env file. Don't forget to remove quotation marks from SECRET_KEY

```
SECRET_KEY = django-insecure-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!#1^ui7j
```

go to settings.py, make amendments below

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

go to terminal

```bash
py manage.py migrate
py manage.py runserver
```

click the link with CTRL key pressed in the terminal and see django rocket.

go to terminal, stop project, add app

python manage.py startapp student_register

```
py manage.py runserver student_register
```

go to settings.py and add 'student_register' app to installed apps and add below lines

go to student_register/models.py

```python
from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=154, unique=True, blank=True, null=True)

    GENDER =(
        ("Female", "Female"),
        ("Male", "Male"),
        ("Other", "Other"),
        ("Prefer Not Say", "Prefer Not Say"),
    )
    gender = models.CharField(max_length=50, choices=GENDER)

    PATH =(
        ("Aws-Dewops", "Aws-Dewops"),
        ("Data Science", "Data Science"),
        ("Full Stack", "Full Stack"),
        ("Cyber Security", "Cyber Security"),
    )
    path = models.CharField(max_length=50, choices=PATH)


    def __str__(self):
        return f"{self.full_name} {self.path}"

```

go to terminal

```bash
py manage.py makemigrations
py manage.py migrate
python manage.py createsuperuser
```

student_register/admin.py

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

go to Admin site and add student objects

create template folder as student_register/templates/student_register

base.html

```html
<!DOCTYPE html>
{% load static %}

<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css"
      integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ"
      crossorigin="anonymous"
    />

    {% comment %}
    <link rel="stylesheet" href=" {% static 'student_register/css/bootstrap.min.css' %}" />
    {% endcomment %}

    <link rel="stylesheet" href=" {% static 'student_register/css/style.css' %}  " />

    <title>Document</title>
  </head>
  <body>
    {% comment %} {% include "users/navbar.html" %} {% endcomment %}
    <div style="margin-top: 100px; margin-bottom: 100px" class="container">
      
      {% if messages %}
        {% for message in messages %} 
          {% if message.tags == "success" %}
            <div class="alert alert-success">{{ message }}</div>
          {% else %}
            <div class="alert alert-{{ message.tags }}">{{ message }}</div>
          {% endif %}
      {% endfor %}
    {% endif %}

      {% block container %}
      {% endblock container %}
    </div>
    <script
      src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"
    ></script>
    <script src="{% static 'student_register/js/timeout.js' %}"></script>
    <script>
      let message = document.querySelector(".alert")

      setTimeout(function () {
        message.style.display = "none";
      }, 3000);
    </script>
  </body>
</html>
```

/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
/*/                                     /*/
/*/         CRUD  - READ(GET)           /*/
/*/                                     /*/
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

go to student_register/views.py
```python
from django.shortcuts import render
from .models import Student

def student_list(request):
    students  = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'student_register/student_list.html', context)

```
go to student_project/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_register.urls')),
]
```

go to student_register/urls.py
```python
from django.urls import path
from .views import student_list

urlpatterns = [
    path('',student_list , name='list'),
]
```

student_list.html
```html
{% extends 'student_register/base.html' %}

{% block container %}
<table>
<h2>Student Register</h2>
<p>Python Django project for implementing CRUD operations</p>
<hr>
    <tr>
        <th>Full Name</th>
        <th>Path</th>
        <td><button><a href="{% url 'add' %}">+Add New</a></button></td>
    </tr>
</table>
    <hr>
        <ul>
            {% for student in students  %}
            <li>{{ student.full_name }}-{{ student.path }}
            <button><a href="{% url 'update' student.id %}">UPDATE</a></button>
            <button><a href="{% url 'delete' student.id %}">DELETE</a></button>
            </li>  
                {% endfor %}
        </ul>     
    </tr>
{% endblock container %}
```

/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
/*/                                     /*/
/*/         CRUD  - CREATE (POST)       /*/
/*/                                     /*/
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

go to student_register/forms.py
```python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

```

go to student_register/views.py
```python
from django.shortcuts import render, redirect
from .forms import StudentForm

def student_add(request):
    form = StudentForm() 
    if request.method == 'POST':          
        print(request.POST)				   
        form = StudentForm(request.POST)   
        if form.is_valid():				   
            form.save()
            messages.success(request, "Student saved successfully")
            return redirect("list")					   
    context = {
        'form' : form
    }
    return render(request, 'student_register/student_form.html', context)
```

go to student_register/urls.py
```python
from django.urls import path
from .views import student_list, student_add

urlpatterns = [
    path('list/',student_list , name='list'),
    path('',student_add , name='add'),
]
```

student_form.html
```html
{% extends 'student_register/base.html' %}

{% block container %}
    <h2>Add Student</h2>
    <form action="" method="POST">
        {% csrf_token %}                   
        {{form.as_p}}						   
        <input type="submit" value="OK">
        <button><a href="{% url 'list' %}">Back to list</a></button>
    </form>
{% endblock container %}
```

/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
/*/                                     /*/
/*/         CRUD  - UPDATE (POST)       /*/
/*/                                     /*/
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

go to student_register/views.py
```python
def student_update(request, id):
    student =Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method== "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully")
            return redirect("list")   
    context = {
        'form':form,
        "student" : student
    }
    return render(request, 'student_register/student_form.html', context)
```

go to student_register/urls.py
```python
from django.urls import path
from .views import student_list, student_add, student_update

urlpatterns = [
    path('list/',student_list , name='list'),
    path('',student_add , name='add'),
    path('<int:id>',student_update , name='update'),
]
```

/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
/*/                                     /*/
/*/         CRUD  - DELETE (POST)       /*/
/*/                                     /*/
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

go to student_register/views.py
```python
def student_delete(request, id):
    student =Student.objects.get(id=id)
    form = StudentForm(instance=student)
    messages.warning(request, "If you click OK, you will delete this student record.")
    if request.method== "POST":
        form = StudentForm(request.POST, instance=student)
        student.delete()
        return redirect("list") 
    context = {
        "student" : student,
        'form': form
    }
    return render(request, 'student_register/student_form.html', context) 
```

go to student_register/urls.py
```python
from django.urls import path
from .views import student_list, student_add, student_update, student_delete

urlpatterns = [
    path('list/',student_list , name='list'),
    path('',student_add , name='add'),
    path('<int:id>',student_update , name='update'),
    path('delete/<int:id>',student_delete , name='delete'),
]
```


### add messages

go to base.html:
```html
        {% if messages %} 
        {% for message in messages %} 
            {% if message.tags == "error" %}
                <div class="alert alert-danger">{{ message }}</div>
            {% else %}
                <div class="alert alert-{{ message.tags }}">{{ message }}</div>
            {% endif %} 
        {% endfor %} 
      {% endif %} 

```

go to views.py:
```python
from django.contrib import messages

            form.save()
            messages.success(request, "student created succesfully!")
            return redirect("list")
```

NOTES: Backend Sprint-1 survey