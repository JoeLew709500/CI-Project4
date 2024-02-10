from django.shortcuts import render,reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Incident, Action
from .forms import IncidentForm

# Create your views here.

def incident_list(request):
    """

    View to display a list of incidents

    ## Templates: incidents/incident_list.html
    
    """

    return render(
        request,
        'incidents/incident_list.html',
        {
            "incident_list": Incident.objects.all(),
        },
    )

def incident_detail(request, incident_id):
    """

    View to display the details of an individual incident

    ## Templates: incidents/incident_detail.html

    """

    if request.method == "POST":
        incident = get_object_or_404(Incident, pk=incident_id)
        incident_form = IncidentForm(data=request.POST, instance=incident)
        if incident_form.is_valid():
            incident_form.save()
            messages.add_message(request, messages.SUCCESS, 'Incident updated')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating incident')

        return HttpResponseRedirect(reverse('incident_detail', args=(incident_id,)))
    
    else:

    # display/edit individual incidents
        incident_form = IncidentForm(
            instance=Incident.objects.get(id=incident_id)
        )
        
        return render(
            request,
            'incidents/incident.html',
            {
                "incident": Incident.objects.get(id=incident_id),
                "incident_form": incident_form,
                "save_button_type": "Update",
            },
        )  

def incident_new(request):
    """

    View to create a new incident

    ## Templates: incidents/incident_new.html

    """

    if request.method == "POST":
        incident_form = IncidentForm(data=request.POST)
        if incident_form.is_valid():
            incident = incident_form.save(commit=False)
            incident.created_by = request.user
            incident.save()
            messages.add_message(request, messages.SUCCESS, 'Incident created')
            return HttpResponseRedirect(reverse('incident_detail', args=(incident.id,)))
        else:
            messages.add_message(request, messages.ERROR, 'Error creating incident')
    else:
        incident_form = IncidentForm()

    return render(
        request,
        'incidents/incident.html',
        {
            "incident_form": incident_form,
            "save_button_type": "Create Incident",
        },
    )