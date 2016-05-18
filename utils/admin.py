from django.contrib import admin
from utils.models import * 

from django.db import models
from django.forms import TextInput, Textarea

#@admin.register(School)
""" check with Jon
#@admin.register(Student)
"""

class SchoolAdmin(admin.ModelAdmin):
	formfield_overrides = {
			models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':30})},
	}
	list_display = ('name',)
	list_filter = ('name',)
	ordering = ('name',)
	search_fields = ('name',)

admin.site.register(School, SchoolAdmin)

class StudentAdmin(admin.ModelAdmin):
	formfield_overrides = {
			models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':30})},
	}
	list_display = ('first_name', 'roll_no')
	list_filter = ('first_name',)
	ordering = ('first_name',)
	search_fields = ('first_name',)

class ClassAdmin(admin.ModelAdmin):
	ordering = ('standard',)

class ParentAdmin(admin.ModelAdmin):
	list_display=('first_name',)
	list_filter=('first_name',)
	search_fields = ('first_name',)

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Staff)
admin.site.register(Term)
admin.site.register(Attn)


