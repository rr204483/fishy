from rest_framework import generics
from utils.models import *
from .serializers import *

from rest_framework import viewsets


class SchoolListView(generics.ListAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

class SchoolDetailView(generics.RetrieveAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

class TermListView(generics.ListAPIView):
	queryset = Term.objects.all()
	serializer_class = TermSerializer

class TermDetailView(generics.RetrieveAPIView):
	queryset = Term.objects.all()
	serializer_class = TermSerializer

class TermViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Term.objects.all()
	serializer_class = TermSerializer

