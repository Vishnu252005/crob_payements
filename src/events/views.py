from django.shortcuts import render, redirect
from events.models import EventRegistration, TeamMember
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from events.forms import EventRegistrationForm  # Ensure you have imported the form

@login_required
def register_events_view(request, event_name):
    event_data = {
        "Line Follower": {
            "rulebook": "https://drive.google.com/file/d/1kQzCfkjC4W0i0uaaRmfrYe5igCCdI3TT/view?usp=drivesdk",
            "fee": 1200,
        },
        "MicroMouse": {
            "rulebook": "https://drive.google.com/file/d/1kQzCfkjC4W0i0uaaRmfrYe5igCCdI3TT/view?usp=drivesdk",
            "fee": 1200,
        },
        "Roborace": {
            "rulebook": "https://drive.google.com/file/d/1kQzCfkjC4W0i0uaaRmfrYe5igCCdI3TT/view?usp=drivesdk",
            "fee": 1200,
        },

        "200g Antweight": {
            "rulebook": "https://drive.google.com/file/d/1kQzCfkjC4W0i0uaaRmfrYe5igCCdI3TT/view?usp=drivesdk",
            "fee": 1200,
        },
        "Robosoccer": {
            "rulebook": "https://drive.google.com/file/d/1kQzCfkjC4W0i0uaaRmfrYe5igCCdI3TT/view?usp=drivesdk",
            "fee": 1200,
        },
        "8Kg Robowar": {
            "rulebook": "https://drive.google.com/file/d/1kQzCfkjC4W0i0uaaRmfrYe5igCCdI3TT/view?usp=drivesdk",
            "fee": 1200,
        },
        "25Kg Robowar": {
            "rulebook": "https://drive.google.com/file/d/1kQzCfkjC4W0i0uaaRmfrYe5igCCdI3TT/view?usp=drivesdk",
            "fee": 1200,
        },
        "500g Robowar": {
            "rulebook": "https://drive.google.com/file/d/1kQzCfkjC4W0i0uaaRmfrYe5igCCdI3TT/view?usp=drivesdk",
            "fee": 1200,
        },

    }

    return render(request, "crob/event_registration.html", {
        "rulebook_link": event_data[event_name]["rulebook"],
        "fee": event_data[event_name]["fee"],
        "event_name": event_name.capitalize(),
    })

def register_submission_view(request, event_name):  # Accept event_name parameter
    if request.method == 'POST':
        leader_name = request.POST['leader_name']
        form = EventRegistrationForm(request.POST, request.FILES)
        if form.is_valid():  # Fixed method call
            event_registration = form.save(commit=False)
            event_registration.user = request.user
            event_registration.event_name = event_name  # Set event_name from URL
            event_registration.save()
            team_members = request.POST.getlist('team_members[]')
            for member_name in team_members:
                TeamMember.objects.create(
                    name=member_name,
                    event_registration=event_registration
                )
            messages.success(request, f"Successfully registered for {event_name}!")
            return redirect('crob-home')
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, 'crob/event_registration.html', {
                "form": form,
                "event_name": event_name
            })
    form = EventRegistrationForm()
    return render(request, 'crob/event_registration.html', {
        "form": form,
        "event_name": event_name
    })

@login_required
def my_events_view(request):
    registrations = EventRegistration.objects.filter(user=request.user)
    return render(request, 'crob/my_events.html', {'registrations': registrations})

def payment_page_view(request):
    pass

# Removed duplicate model classes
