from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from . import models
from . import forms


def faculty(request):
     faculties = models.Faculty.objects.all()
     f = 'f'
     ctx = {'faculties': faculties, 'f': f}
     return render(request, 'faculty_list.html', ctx)

def group(request):
    groups = models.Group.objects.all()
    g = 'g'
    ctx = {'groups': groups, 'g': g}
    return render(request, 'faculty_list.html', ctx)

def department(request):
    departments = models.Department.objects.all()
    d = 'd'
    ctx = {'departments': departments, 'd': d}
    return render(request, 'faculty_list.html', ctx)

def student(request):
    students = models.Student.objects.all()
    s = 's'
    ctx = {'students': students, 's': s}
    return render(request, 'faculty_list.html', ctx)

def subject(request):
    subjects = models.Subject.objects.all()
    su = 'su'
    ctx = {'subjects': subjects, 'su': su}
    return render(request, 'faculty_list.html', ctx)

def teacher(request):
    teachers = models.Teacher.objects.all()
    t = 't'
    ctx = {'teachers': teachers, 't': t}
    return render(request, 'faculty_list.html', ctx)

def faculty_form(request):
    teg = """
        <h1 style="text-align: center">Form is invalid</h1>
    """
    if request.method == 'POST':
        form = forms.FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
        else:
            return HttpResponse(teg)

    ctx = {'forms': forms.FacultyForm}
    return render(request, 'faculty_form.html', ctx)


def group_form(request):
    teg = """
        <h1 style="text-align: center">Form is invalid</h1>
    """
    if request.method == 'POST':
        form = forms.GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
        else:
            return HttpResponse(teg)

    group_confirm = 'group'
    ctx = {'forms': forms.GroupForm, 'group': group_confirm}
    return render(request, 'faculty_form.html', ctx)


def department_form(request):
    teg = """
        <h1 style="text-align: center">Form is invalid</h1>
    """
    if request.method == 'POST':
        form = forms.DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
        else:
            return HttpResponse(teg)

    department_confirm = 'department'
    ctx = {'forms': forms.DepartmentForm, 'department': department_confirm}
    return render(request, 'faculty_form.html', ctx)


def student_form(request):
    teg = """
        <h1 style="text-align: center">Form is invalid</h1>
    """
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            return HttpResponse(teg)

    student_confirm = 'student'
    ctx = {'forms': forms.StudentForm, 'student': student_confirm}
    return render(request, 'faculty_form.html', ctx)


def subject_form(request):
    teg = """
        <h1 style="text-align: center">Form is invalid</h1>
    """
    if request.method == 'POST':
        form = forms.SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
        else:
            return HttpResponse(teg)

    subject_confirm = 'subject'
    ctx = {'forms': forms.SubjectForm, 'subject': subject_confirm}
    return render(request, 'faculty_form.html', ctx)


def teacher_form(request):
    teg = """
        <h1 style="text-align: center">Form is invalid</h1>
    """
    if request.method == 'POST':
        form = forms.TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
        else:
            return HttpResponse(teg)

    teacher_confirm = 'teacher'
    ctx = {'forms': forms.TeacherForm, 'teacher': teacher_confirm}
    return render(request, 'faculty_form.html', ctx)

def update_faculty(request, pk):
    faculty_update = get_object_or_404(models.Faculty, pk=pk)
    teg = """
           <h1 style="text-align: center">Form is invalid</h1>
       """
    if request.method == 'POST':
        form = forms.FacultyForm(request.POST, instance=faculty_update)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
        else:
            return HttpResponse(teg)

    form = {'forms': forms.FacultyForm(instance=faculty_update), 'f': faculty_update}
    return render(request, 'faculty_form.html', form)

def update_group(request, pk):
    group_update = get_object_or_404(models.Group, pk=pk)
    teg = """
           <h1 style="text-align: center">Form is invalid</h1>
       """
    if request.method == 'POST':
        form = forms.GroupForm(request.POST, instance=group_update)
        if form.is_valid():
            form.save()
            return redirect('group_list')
        else:
            return HttpResponse(teg)

    form = {'forms': forms.GroupForm(instance=group_update), 'g': group_update}
    return render(request, 'faculty_form.html', form)

def update_department(request, pk):
    department_update = get_object_or_404(models.Department, pk=pk)
    teg = """
           <h1 style="text-align: center">Form is invalid</h1>
       """
    if request.method == 'POST':
        form = forms.DepartmentForm(request.POST, instance=department_update)
        if form.is_valid():
            form.save()
            return redirect('department_list')
        else:
            return HttpResponse(teg)

    form = {'forms': forms.DepartmentForm(instance=department_update), 'd': department_update}
    return render(request, 'faculty_form.html', form)

def update_student(request, pk):
    student_update = get_object_or_404(models.Student, pk=pk)
    teg = """
           <h1 style="text-align: center">Form is invalid</h1>
       """
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, instance=student_update)
        if form.is_valid():
            form.save()
            return redirect('student_list')
        else:
            return HttpResponse(teg)

    form = {'forms': forms.StudentForm(instance=student_update), 's': student_update}
    return render(request, 'faculty_form.html', form)

def update_subject(request, pk):
    subject_update = get_object_or_404(models.Subject, pk=pk)
    teg = """
           <h1 style="text-align: center">Form is invalid</h1>
       """
    if request.method == 'POST':
        form = forms.SubjectForm(request.POST, instance=subject_update)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
        else:
            return HttpResponse(teg)

    form = {'forms': forms.SubjectForm(instance=subject_update), 'su': subject_update}
    return render(request, 'faculty_form.html', form)

def update_teacher(request, pk):
    teacher_update = get_object_or_404(models.Teacher, pk=pk)
    teg = """
           <h1 style="text-align: center">Form is invalid</h1>
       """
    if request.method == 'POST':
        form = forms.TeacherForm(request.POST, instance=teacher_update)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
        else:
            return HttpResponse(teg)

    form = {'forms': forms.TeacherForm(instance=teacher_update), 't': teacher_update}
    return render(request, 'faculty_form.html', form)

def delete_faculty(request, pk):

    faculty_delete = get_object_or_404(models.Faculty, pk=pk)

    if request.method == 'POST':
        faculty_delete.delete()
        return redirect('faculty_list')

    return render(request, 'confirm.html', {'f': faculty_delete})

def delete_group(request, pk):

    group_delete = get_object_or_404(models.Group, pk=pk)

    if request.method == 'POST':
        group_delete.delete()
        return redirect('group_list')

    g = 'g'
    ctx = {'group': group_delete, 'g': g}
    return render(request, 'confirm.html', ctx)

def delete_department(request, pk):

    department_delete = get_object_or_404(models.Department, pk=pk)

    if request.method == 'POST':
        department_delete.delete()
        return redirect('department_list')

    d = 'd'
    ctx = {'department': department_delete, 'd': d}
    return render(request, 'confirm.html', ctx)

def delete_student(request, pk):

    student_delete = get_object_or_404(models.Student, pk=pk)

    if request.method == 'POST':
        student_delete.delete()
        return redirect('student_list')

    s = 's'
    ctx = {'student': student_delete, 's': s}
    return render(request, 'confirm.html', ctx)

def delete_subject(request, pk):

    subject_delete = get_object_or_404(models.Subject, pk=pk)

    if request.method == 'POST':
        subject_delete.delete()
        return redirect('subject_list')

    su = 'su'
    ctx = {'subject': subject_delete, 'su': su}
    return render(request, 'confirm.html', ctx)

def delete_teacher(request, pk):

    teacher_delete = get_object_or_404(models.Teacher, pk=pk)

    if request.method == 'POST':
        teacher_delete.delete()
        return redirect('teacher_list')

    t = 't'
    ctx = {'teacher': teacher_delete, 't': t}
    return render(request, 'confirm.html', ctx)

def dashboard(request):
    faculties_count = models.Faculty.objects.count()
    groups_count = models.Group.objects.count()
    departments_count = models.Department.objects.count()
    students_count = models.Student.objects.count()
    subjects_count = models.Subject.objects.count()
    teachers_count = models.Teacher.objects.count()
    cxt = {
        'faculties': faculties_count,
        'groups': groups_count,
        'departments': departments_count,
        'students': students_count,
        'subjects': subjects_count,
        'teachers': teachers_count
    }
    return render(request, 'dashboard.html', cxt)


