from django import forms
from . import models


class FacultyForm(forms.ModelForm):
    class Meta:
        model = models.Faculty
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a name'
            })
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = models.Group
        fields = ('name', 'faculty')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a name'
            }),
            'faculty': forms.Select(attrs={
                'class': 'form-control'
            })
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a name'
            })
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ('first_name', 'last_name', 'group', 'department')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'group': forms.Select(attrs={
                'class': 'form-control',
            }),
            'department': forms.Select(attrs={
                'class': 'form-control',
            })
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = models.Subject
        fields = ('name', 'department')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a name'
            }),
            'department': forms.Select(attrs={
                'class': 'form-control',
            })
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = ('first_name', 'last_name', 'subject')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'subject': forms.Select(attrs={
                'class': 'form-control',
            })
        }
