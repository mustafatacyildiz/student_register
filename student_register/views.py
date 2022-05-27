from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.contrib import messages



def student_add(request):
    form = StudentForm() 
    if request.method == 'POST':          
        print(request.POST)				   
        form = StudentForm(request.POST)   
        if form.is_valid():				   
            form.save()
            messages.success(request, f"{ student } saved successfully")
            return redirect("list")					   
    context = {
        'form' : form
    }
    return render(request, 'student_register/student_form.html', context)


def student_update(request, id):
    student =Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method== "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f"{ student } updated successfully")
            return redirect("list")   
    context = {
        'form':form,
        "student" : student
    }
    return render(request, 'student_register/student_form.html', context)



def student_list(request):
    students  = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'student_register/student_list.html', context)



def student_delete(request, id):
    student =Student.objects.get(id=id)
    form = StudentForm(instance=student)
    messages.warning(request, f"If you click OK, you will delete this { student } record.")
    if request.method== "POST":
        form = StudentForm(request.POST, instance=student)
        student.delete()
        messages.success(request, f"{ student } deleted successfully")
        return redirect("list") 
    context = {
        "student" : student,
        'form': form
    }
    return render(request, 'student_register/student_form.html', context)


