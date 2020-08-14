from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import UserForm, ProfileForm
from .models import UserProfile
from django.contrib.auth.models import User


# # Create your views here.
# def profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()

# def profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     return render(request, 'profile.html')


def profile(request, product_id):
    """ A view to individual profiles"""
    user = get_object_or_404(User, pk=user_id)

    context = {
        'username': user_id,
    }

    return render(request, 'profiles/profile.html', context)