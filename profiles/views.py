from django.shortcuts import render, get_object_or_404
from profiles.models import Profile


def index(request):
    """Display the list of profiles

    Args:
        - request (HttpRequest): The received HTTP request object.

    Returns:
        - HttpResponse: The HTTP response object that displays the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis,
# pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis
# fringilla, eros leo tristique lacus, it. Nam aliquam dignissim congue. Pellentesque habitant
# morbi tristique senectus et netus et males


def profile(request, username):
    """Render the profile page for a specific user.

    Args:
        - request (HttpRequest): The request object.
        - username (str): The username of the user.

    Returns:
        - HttpResponse: The rendered profile page.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
