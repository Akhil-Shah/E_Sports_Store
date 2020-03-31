from product.models import Game

def add_to_context(request):

    game_names = Game.objects.all()

    no_of_items = len(request.session['cart_details'])

    context = {
        'game_names':game_names,
        'no_of_items':no_of_items,
    }
    
    return context