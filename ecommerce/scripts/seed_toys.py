# from app import create_app
# from ecommerce.extensions import db
# from ecommerce.models.product import Product

# app = create_app()

PRODUCTS = [
    {
        'name': 'Building Blocks Set 500 Pieces',
        'description': 'Creative building blocks set for kids.',
        'price': 1999,
        'image_url': 'toys/building_blocks_500.jpg',
        'stock': 25,
        'category': 'toys',
        'brand': 'FunBuilder',
        'model': 'Creative 500',
        'rating': 4.6,
        'warranty': 'No Warranty',
        'specifications': '500 pieces, ABS plastic, age 5+'
    },
    {
        'name': 'Remote Control Car',
        'description': 'Rechargeable RC racing car with remote control.',
        'price': 2499,
        'image_url': 'toys/rc_car.jpg',
        'stock': 18,
        'category': 'toys',
        'brand': 'HotWheels',
        'model': 'Racer X',
        'rating': 4.5,
        'warranty': '3 Months',
        'specifications': '2.4GHz remote, rechargeable battery'
    },
    {
        'name': 'Doll House Set',
        'description': 'Miniature doll house with furniture accessories.',
        'price': 3299,
        'image_url': 'toys/doll_house.jpg',
        'stock': 12,
        'category': 'toys',
        'brand': 'Barbie',
        'model': 'Dream House Mini',
        'rating': 4.7,
        'warranty': 'No Warranty',
        'specifications': 'Includes furniture, age 3+'
    },
    {
        'name': 'Board Game Monopoly',
        'description': 'Classic family board game.',
        'price': 1499,
        'image_url': 'toys/monopoly.jpg',
        'stock': 20,
        'category': 'toys',
        'brand': 'Hasbro',
        'model': 'Classic Monopoly',
        'rating': 4.8,
        'warranty': 'No Warranty',
        'specifications': '2-6 players, age 8+'
    },
    {
        'name': 'Puzzle 1000 Pieces',
        'description': 'Premium landscape jigsaw puzzle.',
        'price': 799,
        'image_url': 'toys/puzzle_1000.jpg',
        'stock': 30,
        'category': 'toys',
        'brand': 'Skillmatics',
        'model': 'Landscape 1000',
        'rating': 4.4,
        'warranty': 'No Warranty',
        'specifications': '1000 pieces, finished size 70x50 cm'
    },
    {
        'name': 'Educational Science Kit',
        'description': 'Hands-on science experiments for children.',
        'price': 1799,
        'image_url': 'toys/science_kit.jpg',
        'stock': 16,
        'category': 'toys',
        'brand': 'Smartivity',
        'model': 'Science Lab',
        'rating': 4.6,
        'warranty': 'No Warranty',
        'specifications': '25 experiments, age 6+'
    },
    {
        'name': 'Stuffed Teddy Bear Large',
        'description': 'Soft plush teddy bear gift toy.',
        'price': 999,
        'image_url': 'toys/teddy_bear_large.jpg',
        'stock': 28,
        'category': 'toys',
        'brand': 'SoftBuddy',
        'model': 'Hug Bear',
        'rating': 4.5,
        'warranty': 'No Warranty',
        'specifications': '60 cm plush toy, washable fabric'
    },
    {
        'name': 'Toy Train Set',
        'description': 'Battery-operated train set with tracks.',
        'price': 2199,
        'image_url': 'toys/train_set.jpg',
        'stock': 14,
        'category': 'toys',
        'brand': 'Funskool',
        'model': 'Express Track',
        'rating': 4.3,
        'warranty': '3 Months',
        'specifications': 'Battery operated, 12 track pieces'
    },
    {
        'name': 'Basketball Mini Hoop Set',
        'description': 'Indoor mini basketball hoop for kids.',
        'price': 1299,
        'image_url': 'toys/mini_hoop.jpg',
        'stock': 22,
        'category': 'toys',
        'brand': 'Nivia',
        'model': 'Mini Dunk',
        'rating': 4.2,
        'warranty': 'No Warranty',
        'specifications': 'Wall mount hoop, mini ball included'
    },
    {
        'name': 'Art & Craft Kit',
        'description': 'Creative art and craft activity kit.',
        'price': 899,
        'image_url': 'toys/art_craft_kit.jpg',
        'stock': 35,
        'category': 'toys',
        'brand': 'Pidilite',
        'model': 'Creative Box',
        'rating': 4.4,
        'warranty': 'No Warranty',
        'specifications': 'Colors, papers, glue, craft tools'
    },
    {
        'name': 'Action Figure Superhero',
        'description': 'Collectible superhero action figure.',
        'price': 699,
        'image_url': 'toys/action_figure.jpg',
        'stock': 40,
        'category': 'toys',
        'brand': 'Marvel',
        'model': 'Hero Max',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': '15 cm figure, movable joints'
    },
    {
        'name': 'Chess Set Wooden',
        'description': 'Classic wooden chess set for all ages.',
        'price': 1199,
        'image_url': 'toys/chess_wooden.jpg',
        'stock': 26,
        'category': 'toys',
        'brand': 'Staunton',
        'model': 'Classic Wood',
        'rating': 4.7,
        'warranty': 'No Warranty',
        'specifications': 'Wooden board and pieces, foldable'
    },
    {
        'name': 'Doctor Play Set',
        'description': 'Pretend play doctor kit for children.',
        'price': 999,
        'image_url': 'toys/doctor_play_set.jpg',
        'stock': 24,
        'category': 'toys',
        'brand': 'Toyshine',
        'model': 'Doctor Fun',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': 'Stethoscope, syringe, medical tools'
    },
    {
        'name': 'Magnetic Drawing Board',
        'description': 'Reusable magnetic drawing board for kids.',
        'price': 649,
        'image_url': 'toys/drawing_board.jpg',
        'stock': 38,
        'category': 'toys',
        'brand': 'FunBlast',
        'model': 'Magic Board',
        'rating': 4.2,
        'warranty': 'No Warranty',
        'specifications': 'Magnetic pen, erasable surface'
    },
    {
        'name': 'Outdoor Cricket Set',
        'description': 'Plastic cricket set for outdoor play.',
        'price': 899,
        'image_url': 'toys/cricket_set_kids.jpg',
        'stock': 32,
        'category': 'toys',
        'brand': 'Toyshine',
        'model': 'Kids Cricket',
        'rating': 4.1,
        'warranty': 'No Warranty',
        'specifications': 'Bat, ball, stumps included'
    }
]

# with app.app_context():
#     existing = Product.query.filter_by(category='toys').count()

#     if existing >= 15:
#         print(f'Toys category already has {existing} products. Skipping insert.')
#     else:
#         for item in PRODUCTS:
#             db.session.add(Product(**item))

#         db.session.commit()
#         print('Inserted 15 Toys products successfully.')