from __future__ import unicode_literals

from django.db import models


TITLE_CHOICES = (
    ('Dr.', 'Dr.'),
    ('Mr.', 'Mr.'),
    ('Ms.', 'Ms.'),
    ('Mrs.', 'Mrs.'),
    ('Miss.', 'Miss.'),
)

GENDER_CHOICES = ( ('M', 'Male'), 
		   ('F', 'Female') 
		  )

# todo : populate STAFF_TYPE with the correct value

STAFF_TYPE_CHOICES = ( ('T', 'TEACHING'),
			   ('NT', 'NON-TEACHING'),
			   ('P', 'PRINCIPAL')
		     )

class School(models.Model):
	BOARD_TYPES = (
			('CBSE', 'CBSE'),
			('ICSE', 'ICSE'),
			('State Board Tamil', 'State Board'),
			('State Board Matriculation', 'State Board Matriculation')
	)
	name = models.CharField("Name of school", max_length=150)
	board = models.CharField(max_length=30, choices=BOARD_TYPES)
	address = models.TextField(max_length=500)
	city = models.CharField(max_length=50, blank=True, null=True)
	state = models.CharField(max_length=50, default="Tamil Nadu", editable=False)
	country = models.CharField(max_length=30, default="India", editable=False)
	phone1 = models.CharField(max_length=30)
	phone2 = models.CharField(max_length=30, blank=True, null=True)
	fax = models.CharField(max_length=30, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	website = models.URLField(blank=True, null=True)

	def __str__(self):
		return self.name


class Class(models.Model):

	class Meta:
		unique_together = (('standard', 'section', 'school_id'))

	standard = models.CharField(max_length=2) 
	section = models.CharField(max_length=1)
	school_id = models.ForeignKey(School)
	location  = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.standard+self.section

class Parent(models.Model):
	PARENT_TYPE = ( 
			('Mother', 'Mother'), ('Father', 'Father'), 
			('Guardian','Guardian')
		)

	parent_type = models.CharField(max_length=20, choices=PARENT_TYPE)
	title = models.CharField(max_length=5, default='Mr.', choices=TITLE_CHOICES)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	dob = models.DateField()
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	phone = models.CharField(max_length=20)
	address = models.TextField(max_length=500)
	city = models.CharField(max_length=50, blank=True, null=True)
	state = models.CharField(max_length=50, default="Tamil Nadu", editable=False)
	country = models.CharField(max_length=50, default="India", editable=False)
	photo = models.ImageField(upload_to='/tmp', blank=True, null=True)
	school_id = models.ManyToManyField(School)

	def __str__(self):
		return self.first_name+self.last_name

class Staff(models.Model):
	title = models.CharField(max_length=5, default='Mr.', choices=TITLE_CHOICES)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	staff_id = models.CharField(max_length=10)
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	staff_type = models.CharField(max_length=20, choices=STAFF_TYPE_CHOICES)
	dob = models.DateField()
	doj = models.DateField()
	phone1 = models.CharField(max_length=20)
	phone2 = models.CharField(max_length=20)
	address = models.TextField(max_length=500)
	city = models.CharField(max_length=50, blank=True, null=True)
	state = models.CharField(max_length=50, default="Tamil Nadu", editable=False)
	country = models.CharField(max_length=30, default="India", editable=False)
	experience = models.CharField(max_length=30, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	photo = models.ImageField(upload_to='/tmp', blank=True, null=True)

	class_id = models.ManyToManyField(Class)
	school_id = models.ForeignKey(School)

class Subject(models.Model):
	class Meta:
		unique_together = (('subject_id', 'subject_name', 'school_id'))

	subject_id = models.CharField(max_length=10)
	subject_name = models.CharField(max_length=100)
	school_id = models.ForeignKey(School)
	staff_id = models.ForeignKey(Staff)

class Student(models.Model):
	title = models.CharField(max_length=5, default='Mr.', choices=TITLE_CHOICES)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	dob = models.DateField()
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	roll_no = models.CharField(max_length=10)
	phone = models.CharField(max_length=20)
	email = models.EmailField(blank=True, null=True)
	address = models.TextField(max_length=500, null=True, blank=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	state = models.CharField(max_length=50, default="Tamil Nadu", editable=False)
	country = models.CharField(max_length=30, default="India", editable=False)
	photo = models.ImageField(upload_to='/tmp', blank=True, null=True)
	school_id = models.ForeignKey(School)
	parent_id = models.ForeignKey(Parent)
	class_id = models.ForeignKey(Class)
	subject_id = models.ManyToManyField(Subject)

class Term(models.Model):
	term_id = models.IntegerField()
	start_month = models.CharField(max_length=20)
	end_month = models.CharField(max_length=20)
	school_id = models.ForeignKey(School)


class Attn(models.Model):
	class_id = models.ForeignKey(Class)
	subject_id = models.ManyToManyField(Subject)
	school_id = models.ForeignKey(School)
	student_id = models.ForeignKey(Student)
	attn = models.CharField(max_length=20)
	# add choices for attn

'''todo : StudentClass table, where to keep 
EndYear
Additional Info 
Result
'''	
''' keerthi :
	check the term table, where it needs to associated ??
'''
