from rest_framework import generics
from utils.models import *
from .serializers import *

from rest_framework import viewsets

	
class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

	
class TermViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Term.objects.all()
	serializer_class = TermSerializer

