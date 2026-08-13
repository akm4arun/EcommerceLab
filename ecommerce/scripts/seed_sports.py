# from app import create_app
# from ecommerce.extensions import db
# from ecommerce.models.product import Product

# app = create_app()

PRODUCTS = [
    {
        'name': 'Adjustable Dumbbell Set 20kg',
        'description': 'Adjustable dumbbell set suitable for home workouts.',
        'price': 7999,
        'image_url': 'sports/dumbbell_20kg.jpg',
        'stock': 12,
        'category': 'sports',
        'brand': 'Cultsport',
        'model': 'Adjust 20',
        'rating': 4.6,
        'warranty': '6 Months',
        'specifications': '20kg total weight, steel plates, anti-slip grip'
    },
    {
        'name': 'Yoga Mat 6mm',
        'description': 'Non-slip yoga mat for yoga and stretching.',
        'price': 999,
        'image_url': 'sports/yoga_mat_6mm.jpg',
        'stock': 40,
        'category': 'sports',
        'brand': 'Boldfit',
        'model': 'Yoga 6mm',
        'rating': 4.5,
        'warranty': 'No Warranty',
        'specifications': '6mm thickness, non-slip surface, lightweight'
    },
    {
        'name': 'Resistance Bands Set',
        'description': '5 resistance bands for strength training.',
        'price': 1299,
        'image_url': 'sports/resistance_bands.jpg',
        'stock': 35,
        'category': 'sports',
        'brand': 'Strauss',
        'model': 'Power Bands',
        'rating': 4.4,
        'warranty': '3 Months',
        'specifications': '5 resistance levels, latex material'
    },
    {
        'name': 'Treadmill 2HP',
        'description': 'Motorized treadmill with LCD display.',
        'price': 25999,
        'image_url': 'sports/treadmill_2hp.jpg',
        'stock': 5,
        'category': 'sports',
        'brand': 'PowerMax',
        'model': 'TDM-98',
        'rating': 4.5,
        'warranty': '1 Year Motor Warranty',
        'specifications': '2HP motor, speed 1-14 km/h, foldable design'
    },
    {
        'name': 'Cricket Bat Kashmir Willow',
        'description': 'Kashmir willow cricket bat for beginners.',
        'price': 2499,
        'image_url': 'sports/cricket_bat.jpg',
        'stock': 18,
        'category': 'sports',
        'brand': 'SG',
        'model': 'RSD Spark',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': 'Kashmir willow, short handle'
    },
    {
        'name': 'Football Size 5',
        'description': 'Training football for outdoor play.',
        'price': 899,
        'image_url': 'sports/football_size5.jpg',
        'stock': 30,
        'category': 'sports',
        'brand': 'Nivia',
        'model': 'Storm',
        'rating': 4.2,
        'warranty': 'No Warranty',
        'specifications': 'Size 5, PVC material, stitched'
    },
    {
        'name': 'Badminton Racket Pair',
        'description': 'Lightweight badminton rackets with cover.',
        'price': 1599,
        'image_url': 'sports/badminton_pair.jpg',
        'stock': 24,
        'category': 'sports',
        'brand': 'Yonex',
        'model': 'GR 303',
        'rating': 4.4,
        'warranty': 'No Warranty',
        'specifications': 'Aluminium frame, pair with cover'
    },
    {
        'name': 'Skipping Rope Adjustable',
        'description': 'Adjustable skipping rope for cardio workouts.',
        'price': 399,
        'image_url': 'sports/skipping_rope.jpg',
        'stock': 50,
        'category': 'sports',
        'brand': 'Boldfit',
        'model': 'Speed Rope',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': 'Adjustable length, foam handles'
    },
    {
        'name': 'Fitness Smartwatch',
        'description': 'Fitness smartwatch with heart rate monitor.',
        'price': 2999,
        'image_url': 'sports/fitness_watch.jpg',
        'stock': 22,
        'category': 'sports',
        'brand': 'Noise',
        'model': 'ColorFit Pulse',
        'rating': 4.2,
        'warranty': '1 Year Warranty',
        'specifications': 'Heart rate, SpO2, sleep tracking'
    },
    {
        'name': 'Cycling Helmet',
        'description': 'Lightweight safety helmet for cycling.',
        'price': 1499,
        'image_url': 'sports/cycling_helmet.jpg',
        'stock': 20,
        'category': 'sports',
        'brand': 'Btwin',
        'model': 'Road 500',
        'rating': 4.5,
        'warranty': '6 Months',
        'specifications': 'Adjustable fit, ventilation vents'
    },
    {
        'name': 'Protein Shaker 700ml',
        'description': 'Leak-proof shaker bottle for gym use.',
        'price': 499,
        'image_url': 'sports/protein_shaker.jpg',
        'stock': 60,
        'category': 'sports',
        'brand': 'MuscleBlaze',
        'model': 'Gym Shaker',
        'rating': 4.4,
        'warranty': 'No Warranty',
        'specifications': '700ml, BPA-free, leak-proof lid'
    },
    {
        'name': 'Kettlebell 10kg',
        'description': 'Cast iron kettlebell for strength training.',
        'price': 2199,
        'image_url': 'sports/kettlebell_10kg.jpg',
        'stock': 16,
        'category': 'sports',
        'brand': 'Aurion',
        'model': 'KB10',
        'rating': 4.5,
        'warranty': 'No Warranty',
        'specifications': '10kg, cast iron, powder coated'
    },
    {
        'name': 'Foam Roller',
        'description': 'High-density foam roller for muscle recovery.',
        'price': 899,
        'image_url': 'sports/foam_roller.jpg',
        'stock': 25,
        'category': 'sports',
        'brand': 'FitBox',
        'model': 'Recovery Roller',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': 'High-density EVA foam, 33cm length'
    },
    {
        'name': 'Push Up Bar Set',
        'description': 'Ergonomic push-up bars for upper body workouts.',
        'price': 699,
        'image_url': 'sports/pushup_bars.jpg',
        'stock': 32,
        'category': 'sports',
        'brand': 'Strauss',
        'model': 'Push Pro',
        'rating': 4.2,
        'warranty': 'No Warranty',
        'specifications': 'Non-slip base, ergonomic grip'
    },
    {
        'name': 'Gym Gloves',
        'description': 'Breathable gym gloves with wrist support.',
        'price': 799,
        'image_url': 'sports/gym_gloves.jpg',
        'stock': 45,
        'category': 'sports',
        'brand': 'Nivia',
        'model': 'Gym Grip',
        'rating': 4.1,
        'warranty': 'No Warranty',
        'specifications': 'Breathable fabric, wrist support strap'
    }
]

# with app.app_context():
#     existing = Product.query.filter_by(category='sports').count()

#     if existing >= 15:
#         print(f'Sports category already has {existing} products. Skipping insert.')
#     else:
#         for item in PRODUCTS:
#             db.session.add(Product(**item))

#         db.session.commit()
#         print('Inserted 15 Sports products successfully.')