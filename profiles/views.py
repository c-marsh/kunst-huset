from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import UserForm, ArtistForm
from .models import UserProfile

from artworks.models import Artwork, Artists


def profile(request):
    """ A view to individual profiles"""
    profile = get_object_or_404(UserProfile, user=request.user)
    artworks = Artwork.objects.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'artworks': artworks
    }

    return render(request, template, context)


@login_required
def edit_profile(request, user_id):
    """ Edit profiles"""
    profile = get_object_or_404(UserProfile, user_id=request.user_id)

    template = 'profiles/edit_profile.html'
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)
