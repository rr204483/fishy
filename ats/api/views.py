from rest_framework import generics
from utils.models import School
from .serializers import SchoolSerializer


class SchoolListView(generics.ListAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

class SchoolDetailView(generics.RetrieveAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer


#http://techbus.safaribooksonline.com/book/web-development/django/9781784391911/12dot-building-an-api/ch12s02_html#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE3ODQzOTE5MTElMkZjaDEybHZsMnNlYzE1OF9odG1sJnF1ZXJ5PQ==
