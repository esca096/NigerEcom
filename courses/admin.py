from django.contrib import admin
from courses.models import Courses, Language, Framework, School, Student, Profile
# Register your models here.

admin.site.register(Courses)

#one to many 
admin.site.register(Language)

class AdminFramework(admin.ModelAdmin):
    list_display = ('name', 'language')
admin.site.register(Framework, AdminFramework)


#many to many
admin.site.register(School)
admin.site.register(Student)

#one to one
admin.site.register(Profile)
