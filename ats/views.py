from django.shortcuts import render
from django.http import HttpResponse
from ats.forms import SchoolForm

import datetime


def curr_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> The time is now : %s. </body></html>" % now
    return HttpResponse(html)


def create_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SchoolForm()
    context_data = {'form': form}

    # return HttpResponse('create_school.html', context_data)
    # return render_to_response('create_school.html', context_data,
    #       context_instance=RequestContext(request))
    return render(request, 'create_school.html', context_data)
