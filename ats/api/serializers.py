from rest_framework import serializers
from utils.models import *

class SchoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = School
		fields = ('name', 'board', 'address', 'city', 'state', 'country',
                  'phone1', 'phone2', 'fax', 'email', 'website')

class TermSerializer(serializers.ModelSerializer):
	class Meta:
		model = Term
		fields = ('term_id', 'start_month', 'end_month', 'school_id')


