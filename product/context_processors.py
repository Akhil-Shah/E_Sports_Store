from product.models import Game

def add_to_context(request):

    game_names = Game.objects.all()

    context = {
        'game_names':game_names
    }
    
    return context