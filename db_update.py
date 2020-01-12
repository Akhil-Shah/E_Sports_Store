from product.models import Game,Team,Item

product_db = {

    'Game 1': {
        'Team 1' : {
            'Items' : [['Item 1'], ['Item 2'], ['Item 3']]
        },

        'Team 2' : {
            'Items' : [['Item 1'], ['Item 2'], ['Item 3']]
        },

        'Team 3' : {
            'Items' : [['Item 1'], ['Item 2'], ['Item 3']]
        },
    },

    'Game 2': {
        'Team 4' : {
            'Items' : [['Item 1'], ['Item 2'], ['Item 3']]
        },

        'Team 5' : {
            'Items' : [['Item 1'], ['Item 2'], ['Item 3']]
        },
    },

}

# Removes everything from the tables
Game.objects.all().delete()
Team.objects.all().delete()
Item.objects.all().delete()

# Adds elements to the database
for game_name, game_values in product_db.items():
    game_obj = Game.objects.create(name=game_name)

    for team_name, team_values in game_values.items():
        team_obj = Team.objects.create(name=team_name,game=game_obj)
        
        for array in team_values.values():
            for each_item in array:
                for item_name in each_item:
                    Item.objects.create(name=item_name,team=team_obj)
