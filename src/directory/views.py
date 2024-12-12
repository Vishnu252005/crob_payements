from django.shortcuts import render, redirect
from directory.forms import AccountProfileForm
from directory.models import Profile

from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User 
from django.contrib import messages

@login_required
def account_profile_view(request):
    if not hasattr(request.user, 'profile'):
        messages.error(request, "User profile does not exist.")
        return redirect('crob-home') 
    
    profile = request.user.profile
    form = AccountProfileForm(instance=profile)

    if request.method == 'POST':
        form = AccountProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile-page') 

    context = {'form': form}
    return render(request, 'directory/account_profile.html', context)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
