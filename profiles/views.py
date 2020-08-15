from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import UserForm, ProfileForm
from .models import UserProfile


def profile(request):
    """ A view to individual profiles"""
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
