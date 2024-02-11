from django.shortcuts import render,reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Incident, Action
from .forms import IncidentForm, ActionForm, ActionFormNew, IncidentFormSearch

# Create your views here.

def index(request):
    """

    View to display the index page

    ## Templates: incidents/index.html

    """

    return render(
        request,
        'incidents/index.html',
    )

def incident_list(request):
    """

    View to display a list of incidents

    ## Templates: incidents/incident_list.html
    
    """
    if request.method == "POST":
        incident_form = IncidentFormSearch(data=request.POST)
        if incident_form.is_valid():
            selected_category = incident_form.cleaned_data.get('incident_category')
            incidents = Incident.objects.filter(incident_category=selected_category)
        else:
            print(incident_form.errors)  # print form errors
            incidents = Incident.objects.all()
    else:
        incident_form = IncidentFormSearch()
        incidents = Incident.objects.all()

    return render(
        request,
        'incidents/incident_list.html',
        {
            "incident_list": incidents,
            "incident_form": incident_form,
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

def incident_delete(request, incident_id):  
    """

    View to delete an incident

    ## Templates: incidents/incident_delete.html

    """

    incident = get_object_or_404(Incident, pk=incident_id)
    incident.delete()
    messages.add_message(request, messages.SUCCESS, 'Incident deleted')
    return HttpResponseRedirect(reverse('incident_list'))

def actions(request, incident_id):
    """

    View to display a list of actions

    ## Templates: incidents/actions.html

    """

    return render(
        request,
        'incidents/actions.html',
        {
            "action_list": Action.objects.filter(incident=incident_id),
            "incident_id": incident_id,
            "incident": Incident.objects.get(id=incident_id),
        },
    )

def action_detail(request,incident_id, action_id):
    """

    View to display the details of an individual action

    ## Templates: incidents/action_detail.html

    """
    if request.method == "POST":
        action = get_object_or_404(Action, pk=action_id)
        action_form = ActionForm(data=request.POST, instance=action)
        if action_form.is_valid():
            action_form.save()
            messages.add_message(request, messages.SUCCESS, 'Action updated')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating action')

        return HttpResponseRedirect(reverse('action_detail', args=(incident_id,action_id,)))
    
    else:

        action_form = ActionForm(
            instance=Action.objects.get(id=action_id)
        )

        return render(
            request,
            'incidents/action_detail.html',
            {
                "action": Action.objects.get(id=action_id),
                "action_form": action_form,
                "save_button_type": "Update",
                "incident_id": incident_id,
            },
        )

def action_new(request, incident_id):
    """

    View to create a new action

    ## Templates: incidents/action_detail.html

    """

    if request.method == "POST":
        action_form = ActionFormNew(data=request.POST)
        if action_form.is_valid():
            action = action_form.save(commit=False)
            action.created_by = request.user
            action.incident = Incident.objects.get(id=incident_id)
            action.save()
            messages.add_message(request, messages.SUCCESS, 'Action created')
            return HttpResponseRedirect(reverse('actions', args=(incident_id,)))
        else:
            messages.add_message(request, messages.ERROR, 'Error creating action')
    else:
        action_form = ActionFormNew()

    return render(
        request,
        'incidents/action_detail.html',
        {
            "action_form": action_form,
            "save_button_type": "Create Action",
        },)

def action_delete(request, incident_id, action_id):
    """

    View to delete an action

    """

    action = get_object_or_404(Action, pk=action_id)
    action.delete()
    messages.add_message(request, messages.SUCCESS, 'Action deleted')
    return HttpResponseRedirect(reverse('actions', args=(incident_id,)))
