from artworks.models import Artwork


def menu_content(request):
    menu_artist = Artwork.objects.all()

    context = {
        "menu_artist": menu_artist
    }
    return context
