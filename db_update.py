from product.models import Game,Team,Item

hat_url = 'https://cdn.shopify.com/s/files/1/0264/4583/products/mX5wbOljShW7hRot9rNa_difuzed_0004_Ebene_6_360x.jpg?v=1582026119'
shirt_url = 'https://cdn.shopify.com/s/files/1/0264/4583/products/214rQfdQTiqeQuxTaNCQ_ESL307_1_360x.jpg?v=1582890895'
hoodie_url = 'https://cdn.shopify.com/s/files/1/0264/4583/products/TmSFGhDdSUqEnxFHKvCj_ESL269-front_360x.jpg?v=1582026295'
scarf_url = 'https://cdn.shopify.com/s/files/1/0264/4583/products/NLMPHVNQhm2taSd5TNqw_AST125-4_360x.jpg?v=1582037570'
jacket_url = 'https://cdn.shopify.com/s/files/1/0264/4583/products/WujvmZxJTKmJfEoxKKd2_ESL254-front_360x.jpg?v=1582031880'

product_db = {

    'Fortnite': {
        'Team Liquid' : {
            'Items' : [['Hat',50,hat_url], ['Shirt',30,shirt_url], ['Jacket',20,jacket_url]]
        },

        'Fnatic' : {
            'Items' : [['Shirt',60,shirt_url], ['Scarf',50,scarf_url], ['Cap',10,hat_url]]
        },

        'NRG Esports' : {
            'Items' : [['Hoodie',40,hoodie_url], ['Jacket',20,jacket_url], ['Hat',10,hat_url]]
        },
    },

    'CS:GO': {
        'Astralis' : {
            'Items' : [['Shirt',70,shirt_url], ['Shirt',50,shirt_url], ['Hat',30,hat_url]]
        },

        'MiBR' : {
            'Items' : [['Jacket',40,jacket_url], ['Scarf',40,scarf_url], ['Cap',10,hat_url]]
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
                Item.objects.create(name=each_item[0],price=each_item[1],
                                    img_url=each_item[2],team=team_obj)
