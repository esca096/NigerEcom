from django.shortcuts import get_object_or_404, redirect, render
from .models  import Courses
from .form import  CoursesForm

from django.views import View

# Create your views here.

class List_view(View):
    template_name = 'courses/course_list.html'
    
    def get(self, request, *args, **kwargs):
        queryset = Courses.objects.all()
        return render(request, self.template_name, {'object_list':queryset})
    

class Detail_view(View):
    template_name = 'courses/course_detail.html'
    
    def get(self, request, id=None, *args, **kwargs):
        id = self.kwargs.get('pk')
        context = {}
        if id is not None:
            obj = get_object_or_404(Courses, id=id)
            context['object']=obj
        return render(request, self.template_name, context)


class Create_view(View):
    form = CoursesForm()
    template_name = 'courses/course_create.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form})
    
    def post(self, request, *args, **kwargs):
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/courses')
    
    
class Update_view(View):
    template_name = 'courses/course_create.html'
    
    def get_object(self):
        id = self.kwargs.get('pk')
        if id is not None:
            obj = get_object_or_404(Courses, id=id)
            return obj
    
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        form = CoursesForm(instance=obj)
        return render(request, self.template_name, {'form':form})
    
    
    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        form = CoursesForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/courses')
        
        
        
class Delete_view(View):
    template_name = 'courses/course_delete.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def get_object(self):
        id = self.kwargs.get('pk')
        if id is not None:
            obj = get_object_or_404(Courses, id=id)
            return obj
    
    
    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return redirect('/courses')