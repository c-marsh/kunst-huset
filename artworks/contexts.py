from artworks.models import Artwork


def menu_content(request):
    """
    Provides access to Artist list to create menu list
    """
    menu_artist = Artwork.objects.all()

    context = {
        "menu_artist": menu_artist
    }
    return context
