from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ats.forms import SchoolForm
from utils.models import School
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import DeleteView # this is the generic view
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q

import datetime


class SchoolDelete(DeleteView):
	model=School
	success_url=reverse_lazy('list_schools')
	template_name = 'delete_school.html'

def curr_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> The time is now : %s. </body></html>" % now
    return HttpResponse(html)


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
	
    if request.GET.get("q","") != "":
        search_query=request.GET.get("q","")
        schools = School.objects.filter(Q(name__icontains=search_query)|Q(address__icontains=search_query))
    else:
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
	
	

