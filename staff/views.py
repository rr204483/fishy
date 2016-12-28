from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from staff.forms import StaffForm
from utils.models import Staff
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import DeleteView # this is the generic view
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q


import datetime

# Create your views here.

class StaffDelete(DeleteView):
	model=Staff
	success_url=reverse_lazy('list_staff')
	template_name = 'delete_staff.html'
	
def home(request):
    now = datetime.datetime.now()
    html = "<html><body> welcome to Staff home page <br> The time is now : %s. </body></html>" % now
    return HttpResponse(html)
	

def create_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
			#message = "School added"
            return render(request, 'staff_added.html', {'form': form})
    else:
        form = StaffForm()
    context_data = {'form': form}	
    return render(request, 'create_staff.html', context_data)
	
def list_staff(request):
    if request.GET.get("q","") != "":
        search_query=request.GET.get("q","")
        staffs = Staff.objects.filter(Q(first_name__icontains=search_query)|Q(last_name__icontains=search_query))
    else:
        staffs = Staff.objects.all()  
    return render(request, 'list_staff.html', {'staffs': staffs})
	
def staff_detail(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff_detail.html', {'staff': staff})
	
def staff_edit(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
			#message = "School added"
            return render(request, 'staff_added.html', {'form': form})
    else:
        form = StaffForm(instance=staff)
    context_data = {'form': form}

    # return HttpResponse('create_school.html', context_data)
    # return render_to_response('create_school.html', context_data,
    #       context_instance=RequestContext(request))
    return render(request, 'create_staff.html', context_data)
	
'''

def create_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
			#message = "School added"
            return render(request, 'school_added.html', {'form': form})
    else:
        form = SchoolForm()
    context_data = {'form': form}

    # return HttpResponse('create_school.html', context_data)
    # return render_to_response('create_school.html', context_data,
    #       context_instance=RequestContext(request))
    return render(request, 'create_school.html', context_data)
	
		
def list_schools(request):
    schools = School.objects.all()  
    return render(request, 'list_schools.html', {'schools': schools})
	
def school_detail(request, pk):
    school = get_object_or_404(School, pk=pk)
    return render(request, 'school_detail.html', {'school': school})
	
def school_edit(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
			#message = "School added"
            return render(request, 'school_added.html', {'form': form})
    else:
        form = SchoolForm(instance=school)
    context_data = {'form': form}

    # return HttpResponse('create_school.html', context_data)
    # return render_to_response('create_school.html', context_data,
    #       context_instance=RequestContext(request))
    return render(request, 'create_school.html', context_data)
'''