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
			 
ATTN_CHOICES = (
    ('Present', 'Present'),
    ('Absent', 'Absent'),
    ('Sick', 'Sick'),
    ('Vacation', 'Vacation'),
    ('Medical', 'Medical')
)			 
ASSIGNMENT_STATUS = (
    (1, 'Assigned'),
    (2, 'Completed'),
    (3, 'Late Completion'),
    (4, 'Partially Completed'),
    (5, 'Did Not Complete')
)			 

BOARD_TYPES = (
		('CBSE', 'CBSE'),
		('ICSE', 'ICSE'),
		('State Board Tamil', 'State Board'),
		('State Board Matriculation', 'State Board Matriculation')
)

class School(models.Model):
	name = models.CharField("Name of school", max_length=150)
	board = models.CharField(max_length=30, choices=BOARD_TYPES)
	address = models.TextField(max_length=1000)
	city = models.CharField(max_length=50, blank=True, null=True)
	state = models.CharField(max_length=50, default="Tamil Nadu", editable=False)
	country = models.CharField(max_length=50, default="India", editable=False)
	phone1 = models.CharField(max_length=30)
	phone2 = models.CharField(max_length=30, blank=True, null=True)
	fax = models.CharField(max_length=30, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	website = models.URLField(blank=True, null=True)

	def __str__(self):
		return self.name

class Subject(models.Model):

	#subject_id = models.CharField(max_length=50, primary_key=True)
	subject_name = models.CharField(max_length=100, default="")
	school_id = models.ForeignKey(School)
	
	def __str__(self):
		return self.subject_name

		
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

	def __str__(self):
		return self.first_name+self.last_name
		
		
class Parent(models.Model):
	PARENT_TYPE = ( 
			('Mother', 'Mother'), ('Father', 'Father'), 
			('Guardian','Guardian')
		)

	parent_type = models.CharField(max_length=20, choices=PARENT_TYPE)
	title = models.CharField(max_length=10, default='Mr.', choices=TITLE_CHOICES)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	dob = models.DateField()
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=50, null=True)
	address = models.TextField(max_length=500)
	city = models.CharField(max_length=50, blank=True, null=True)
	state = models.CharField(max_length=50, default="Tamil Nadu", editable=False)
	country = models.CharField(max_length=50, default="India", editable=False)
	photo = models.ImageField(upload_to='/tmp', blank=True, null=True)
	student_id = models.ForeignKey(Student, blank=True, null=True)
	school_id = models.ForeignKey(School, blank=True, null=True)

	def __str__(self):
		return self.first_name+self.last_name
		

class Staff(models.Model):
	title = models.CharField(max_length=5, default='Mr.', choices=TITLE_CHOICES)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
	staff_type = models.CharField(max_length=20, choices=STAFF_TYPE_CHOICES)
	dob = models.DateField()
	doj = models.DateField()
	phone1 = models.CharField(max_length=20)
	phone2 = models.CharField(max_length=20)
	email = models.EmailField(blank=True, null=True)
	address = models.TextField(max_length=500)
	city = models.CharField(max_length=50, blank=True, null=True)
	state = models.CharField(max_length=50, default="Tamil Nadu", editable=False)
	country = models.CharField(max_length=30, default="India", editable=False)
	qualification = models.CharField(max_length=30, blank=True, null=True)
	experience = models.CharField(max_length=30, blank=True, null=True)
	photo = models.ImageField(upload_to='/tmp', blank=True, null=True)
	emergencycontact = models.CharField(max_length=20, blank=True, null=True)
	major_subjects = models.CharField(max_length=50, blank=True, null=True)
	school_id = models.ForeignKey(School)
		

class Class(models.Model):
	class Meta:
		unique_together = (('standard', 'section', 'school_id'))
	
	standard = models.CharField(max_length=30) 
	section = models.CharField(max_length=30)
	school_id = models.ForeignKey(School)
	class_teacher_id = models.ForeignKey(Staff, null=True, related_name='class_teacher')
	class_teacher_bkp_id = models.ForeignKey(Staff, null=True, related_name='class_teacher_bkp')
	class_leader_id = models.ForeignKey(Student, null=True, related_name='class_leader')
	class_leader_bkp_id = models.ForeignKey(Student,null=True, related_name='class_leader_bkp')
	location  = models.CharField(max_length=500, null=True, blank=True)

	def __str__(self):
		return self.standard+self.section+self.school_id

class StudentClass(models.Model):
	stu_class_rev_no = models.FloatField()
	student_id = models.ForeignKey(Student)
	class_id = models.ForeignKey(Class) 
	school_id = models.ForeignKey(School)
	end_year = models.DateField()
	result = models.CharField(max_length=50, null=True)
	additional_info = models.CharField(max_length=500, null=True)

	def __str__(self):
		return self.id+'#'+self.student_id+'#'+self.class_id+'#'+self.stu_class_rev_no
		
class StudentClassSubject(models.Model):
	stu_class_sub_rev_no = models.FloatField()
	stu_class_id = models.ForeignKey(StudentClass)
	subject_id = models.ForeignKey(Subject) 
	school_id = models.ForeignKey(School)
	eval_year = models.DateField()
	result = models.CharField(max_length=50, null=True)
	#additional_info = models.CharField(max_length=500, null=True)

	def __str__(self):
		return self.id+'#'+self.subject_id+'#'+self.stu_class_sub_rev_no		
		
class StaffSubject(models.Model):
	staff_sub_rev_no = models.FloatField()
	staff_id = models.ForeignKey(Staff)
	subject_id = models.ForeignKey(Subject) 
	school_id = models.ForeignKey(School)
	active = models.CharField(max_length=20)

	def __str__(self):
		return self.id+'#'+self.staff_id+'#'+self.subject_id+'#'+self.stu_class_sub_rev_no	
		
class StaffClassSubject(models.Model):
	staff_class_sub_rev_no = models.FloatField()
	staff_sub_id = models.ForeignKey(StaffSubject)
	class_id = models.ForeignKey(Class) 
	school_id = models.ForeignKey(School)
	active = models.CharField(max_length=20)

	def __str__(self):
		return self.id+'#'+self.staff_sub_id+'#'+self.staff_class_sub_rev_no		

class TransactionHistory(models.Model):
	rev_no = models.FloatField()
	time_stamp = models.DateField()
	modified_by = models.ForeignKey(Staff) 
	reason = models.CharField(max_length=500)
	transaction_code = models.CharField(max_length=10)  # SH - School table, ST - Student, CL - Class….
	school_id = models.ForeignKey(School)

	def __str__(self):
		return self.id+'#'+self.rev_no+'#'+self.modified_by

class TimeTableSchedule(models.Model):
	class Meta:
		unique_together = (('id', 'tts_rev_no'))

	tts_rev_no = models.FloatField()
	week_day = models.CharField(max_length=15)
	date = models.DateField()
	day_type = models.CharField(max_length=15)    # R - Regular, E- Exam, S-School Day, A-Actvities
	day_desc = models.CharField(max_length=500)   # Exam, School Day, inter-school sports day…
	subject1 = models.ForeignKey(Subject, null=True, related_name='p_subject1')
	planned_session_1 = models.CharField(max_length=200)    # Ex1: C=111#T=1,2#ST=1,2,3,4,5  (C=chapter, T=topic, ST=sub topic) Ex2: C=111,222#T=1,2,3,4#ST=1,2,3,4,5,6,7
	planned_assignment_1 = models.CharField(max_length=200)
	planned_staff1 = models.ForeignKey(Staff, null=True, related_name='p_staff1')
	subject2 = models.ForeignKey(Subject, null=True, related_name='p_subject2')
	planned_session_2 = models.CharField(max_length=200)
	planned_assignment_2 = models.CharField(max_length=200)
	planned_staff2 = models.ForeignKey(Staff, null=True, related_name='p_staff2')
	subject3 = models.ForeignKey(Subject, null=True, related_name='p_subject3')
	planned_session_3 = models.CharField(max_length=200)
	planned_assignment_3 = models.CharField(max_length=200)
	planned_staff3 = models.ForeignKey(Staff, null=True, related_name='p_staff3')
	subject4= models.ForeignKey(Subject, null=True, related_name='p_subject4')
	planned_session_4 = models.CharField(max_length=200)
	planned_assignment_4 = models.CharField(max_length=200)
	planned_staff4 = models.ForeignKey(Staff, null=True, related_name='p_staff4')
	subject5 = models.ForeignKey(Subject, null=True, related_name='p_subject5')
	planned_session_5 = models.CharField(max_length=200)
	planned_assignment_5 = models.CharField(max_length=200)
	planned_staff5 = models.ForeignKey(Staff, null=True, related_name='p_staff5')
	subject6 = models.ForeignKey(Subject, null=True, related_name='p_subject6')
	planned_session_6 = models.CharField(max_length=200)
	planned_assignment_6 = models.CharField(max_length=200)
	planned_staff6 = models.ForeignKey(Staff, null=True, related_name='p_staff6')
	subject7 = models.ForeignKey(Subject, null=True, related_name='p_subject7')
	planned_session_7 = models.CharField(max_length=200)
	planned_assignment_7 = models.CharField(max_length=200)
	planned_staff7 = models.ForeignKey(Staff, null=True, related_name='p_staff7')
	subject8 = models.ForeignKey(Subject, null=True, related_name='p_subject8')
	planned_session_8 = models.CharField(max_length=200)
	planned_assignment_8 = models.CharField(max_length=200)
	planned_staff8 = models.ForeignKey(Staff, null=True, related_name='p_staff8')
	subject9 = models.ForeignKey(Subject, null=True, related_name='p_subject9')
	planned_session_9 = models.CharField(max_length=200)
	planned_assignment_9 = models.CharField(max_length=200)
	planned_staff9 = models.ForeignKey(Staff, null=True, related_name='p_staff9')
	subject10 = models.ForeignKey(Subject, null=True, related_name='p_subject10')
	planned_session_10 = models.CharField(max_length=200)
	planned_assignment_10 = models.CharField(max_length=200)
	planned_staff10 = models.ForeignKey(Staff, null=True, related_name='p_staff10')
	class_id = models.ForeignKey(Class)
	term = models.CharField(max_length=200)
	school_id = models.ForeignKey(School)
	

class TimeTableActual(models.Model):
	class Meta:
		unique_together = (('id', 'tta_rev_no'))

	tta_rev_no = models.FloatField()
	week_day = models.CharField(max_length=15)
	date = models.DateField()
	day_type = models.CharField(max_length=15)    # R - Regular, E- Exam, S-School Day, A-Actvities
	day_desc = models.CharField(max_length=500)   # Exam, School Day, inter-school sports day…
	subject1 = models.ForeignKey(Subject, null=True, related_name='a_subject1')
	actual_session_1 = models.CharField(max_length=200)
	actual_assignment_1 = models.CharField(max_length=200)
	actual_staff1 = models.ForeignKey(Staff, null=True, related_name='a_staff1')
	subject2 = models.ForeignKey(Subject, null=True, related_name='a_subject2')
	actual_session_2 = models.CharField(max_length=200)
	actual_assignment_2 = models.CharField(max_length=200)
	actual_staff2 = models.ForeignKey(Staff, null=True, related_name='a_staff2')
	subject3 = models.ForeignKey(Subject, null=True, related_name='a_subject3')
	actual_session_3 = models.CharField(max_length=200)
	actual_assignment_3 = models.CharField(max_length=200)
	actual_staff3 = models.ForeignKey(Staff, null=True, related_name='a_staff3')
	subject4= models.ForeignKey(Subject, null=True, related_name='a_subject4')
	actual_session_4 = models.CharField(max_length=200)
	actual_assignment_4 = models.CharField(max_length=200)
	actual_staff4 = models.ForeignKey(Staff, null=True, related_name='a_staff4')
	subject5 = models.ForeignKey(Subject, null=True, related_name='a_subject5')
	actual_session_5 = models.CharField(max_length=200)
	actual_assignment_5 = models.CharField(max_length=200)
	actual_staff5 = models.ForeignKey(Staff, null=True, related_name='a_staff5')
	subject6 = models.ForeignKey(Subject, null=True, related_name='a_subject6')
	actual_session_6 = models.CharField(max_length=200)
	actual_assignment_6 = models.CharField(max_length=200)
	actual_staff6 = models.ForeignKey(Staff, null=True, related_name='a_staff6')
	subject7 = models.ForeignKey(Subject, null=True, related_name='a_subject7')
	actual_session_7 = models.CharField(max_length=200)
	actual_assignment_7 = models.CharField(max_length=200)
	actual_staff7 = models.ForeignKey(Staff, null=True, related_name='a_staff7')
	subject8 = models.ForeignKey(Subject, null=True, related_name='a_subject8')
	actual_session_8 = models.CharField(max_length=200)
	actual_assignment_8 = models.CharField(max_length=200)
	actual_staff8 = models.ForeignKey(Staff, null=True, related_name='a_staff8')
	subject9 = models.ForeignKey(Subject, null=True, related_name='a_subject9')
	actual_session_9 = models.CharField(max_length=200)
	actual_assignment_9 = models.CharField(max_length=200)
	actual_staff9 = models.ForeignKey(Staff, null=True, related_name='a_staff9')
	subject10 = models.ForeignKey(Subject, null=True, related_name='a_subject10')
	actual_session_10 = models.CharField(max_length=200)
	actual_assignment_10 = models.CharField(max_length=200)
	actual_staff10 = models.ForeignKey(Staff, null=True, related_name='a_staff10')
	class_id = models.ForeignKey(Class)
	term = models.CharField(max_length=200)
	school_id = models.ForeignKey(School)	
	

class AttnTracking(models.Model):
	log_rev_no = models.FloatField()
	class_id = models.ForeignKey(Class)
	staff_id = models.ForeignKey(Staff)
	student_id = models.ForeignKey(Student)
	attendence = models.CharField(max_length=50, choices=ATTN_CHOICES)     # Present / Absent / Sick / Vacation / Medical
	timetable_id = models.ForeignKey(TimeTableActual, null=True, related_name='attn_timetable_id')
	tta_rev_no = models.FloatField()
	school_id = models.ForeignKey(School)

class HomeworkMgmt(models.Model):
	assignment_rev_no = models.FloatField()
	class_id = models.ForeignKey(Class)
	staff_id = models.ForeignKey(Staff)
	student_id = models.ForeignKey(Student)
	assignment_details = models.CharField(max_length=500)    # Capture the ActualAssignmentN from TimeTableActual table
	status = models.IntegerField(null = True, choices=ASSIGNMENT_STATUS)     # 1 - Assigned 2 - Completed 3 - Late completion 4 - Partially completed 5 - Did not complete
	timetable_id = models.ForeignKey(TimeTableActual, null=True, related_name='hw_timetable_id')
	tta_rev_no = models.FloatField()
	school_id = models.ForeignKey(School)

class Syllabus(models.Model):
	syllabus_rev_no = models.FloatField()
	board = models.CharField(max_length=30, choices=BOARD_TYPES)
	term = models.CharField(max_length=200)
	start_year = models.DateField
	end_year = models.DateField
	subject_id = models.ForeignKey(Subject)
	class_id = models.ForeignKey(Class)
	school_id = models.ForeignKey(School)
	
class SyllabusUnitsChap(models.Model):
	unit_no = models.CharField(max_length=50)
	unit_title = models.CharField(max_length=1000)
	chapter_no = models.CharField(max_length=50)
	chap_title = models.CharField(max_length=1000)
	topics = models.CharField(max_length=1000)
	syllabus_id = models.ForeignKey(Syllabus)
	syllabus_rev_no = models.FloatField()   
	school_id = models.ForeignKey(School)	

class Books(models.Model):
	book_rev_no = models.FloatField()
	book_name = models.CharField(max_length=500)
	book_desc = models.CharField(max_length=1000)
	book_author = models.CharField(max_length=200)
	book_publications = models.CharField(max_length=500)
	book_published = models.DateField() # captures the year of book published
	subject_id = models.ForeignKey(Subject)
	class_id = models.ForeignKey(Class)
	school_id = models.ForeignKey(School)	
	
class SyllabusBooks(models.Model):
	book_id = models.ForeignKey(Books)
	book_rev_no = models.FloatField()
	book_used = models.NullBooleanField()   # You can only have one Book that is active per school (CBSC - where you have more than one recommended books)
	syllabus_id = models.ForeignKey(Syllabus)
	syllabus_rev_no = models.FloatField()   
	school_id = models.ForeignKey(School)	
	
	
class BookChapters(models.Model):
	chap_title = models.CharField(max_length=500)    # This can be something like Unit 1. Chapter 1, Unit 1. Chapter 2
	page_nos = models.CharField(max_length=100)   #10-20 (means - start page - 10 end page - 20) while populating the chapters listing in UI - combine this field as well - like Unit 1. Chapter 1 (10-20)
	chap_assignment = models.CharField(max_length=1000)   # chap level home work
	assignment_page_nos = models.CharField(max_length=100) 
	book_id = models.ForeignKey(Books)
	book_rev_no = models.FloatField()
	school_id = models.ForeignKey(School)	
	
	
class BookTopics(models.Model):
	Topic = models.CharField(max_length=1000)    
	page_nos = models.CharField(max_length=100)   # similar to chapters
	topic_assignment = models.CharField(max_length=1000)   # chap level home work
	assignment_page_nos = models.CharField(max_length=100) 
	book_chap_id = models.ForeignKey(BookChapters)
	school_id = models.ForeignKey(School)	
		
class BookSubTopics(models.Model):
	subtopic = models.CharField(max_length=1000)    
	page_nos = models.CharField(max_length=100)  
	subtopic_assignment = models.CharField(max_length=1000)   # chap level home work
	assignment_page_nos = models.CharField(max_length=100) 
	book_topics_id = models.ForeignKey(BookTopics)
	school_id = models.ForeignKey(School)	
		
class Term(models.Model):
	term_id = models.IntegerField()
	start_month = models.CharField(max_length=20)
	end_month = models.CharField(max_length=20)
	school_id = models.ForeignKey(School)




