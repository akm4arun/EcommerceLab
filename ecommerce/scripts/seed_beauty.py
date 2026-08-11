from app import create_app
from ecommerce.extensions import db
from ecommerce.models.product import Product

app = create_app()

PRODUCTS = [
    {
        'name': 'Vitamin C Face Serum',
        'description': 'Brightening face serum with Vitamin C and hyaluronic acid.',
        'price': 599,
        'image_url': 'beauty/vitamin_c_serum.jpg',
        'stock': 40,
        'category': 'beauty',
        'brand': 'Minimalist',
        'model': 'Vitamin C 10%',
        'rating': 4.5,
        'warranty': 'No Warranty',
        'specifications': '30ml, Vitamin C 10%, fragrance free'
    },
    {
        'name': 'Aloe Vera Gel',
        'description': 'Pure aloe vera gel for skin and hair care.',
        'price': 249,
        'image_url': 'beauty/aloe_vera_gel.jpg',
        'stock': 60,
        'category': 'beauty',
        'brand': 'Patanjali',
        'model': 'Aloe Gel',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': '150ml, aloe vera extract'
    },
    {
        'name': 'Shampoo Anti Hair Fall',
        'description': 'Strengthens hair and reduces hair fall.',
        'price': 349,
        'image_url': 'beauty/shampoo_hairfall.jpg',
        'stock': 55,
        'category': 'beauty',
        'brand': 'L’Oréal',
        'model': 'Fall Resist',
        'rating': 4.4,
        'warranty': 'No Warranty',
        'specifications': '340ml, anti-hair fall formula'
    },
    {
        'name': 'Hair Conditioner Smooth',
        'description': 'Smoothening conditioner for dry and frizzy hair.',
        'price': 299,
        'image_url': 'beauty/conditioner_smooth.jpg',
        'stock': 48,
        'category': 'beauty',
        'brand': 'Dove',
        'model': 'Smooth Care',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': '180ml, smoothening conditioner'
    },
    {
        'name': 'Face Wash Oil Control',
        'description': 'Gentle oil-control face wash for daily use.',
        'price': 199,
        'image_url': 'beauty/facewash_oilcontrol.jpg',
        'stock': 70,
        'category': 'beauty',
        'brand': 'Cetaphil',
        'model': 'Oil Control',
        'rating': 4.5,
        'warranty': 'No Warranty',
        'specifications': '125ml, soap-free cleanser'
    },
    {
        'name': 'Sunscreen SPF 50',
        'description': 'Broad-spectrum sunscreen with SPF 50 protection.',
        'price': 499,
        'image_url': 'beauty/sunscreen_spf50.jpg',
        'stock': 52,
        'category': 'beauty',
        'brand': 'Neutrogena',
        'model': 'Ultra Sheer',
        'rating': 4.6,
        'warranty': 'No Warranty',
        'specifications': '88ml, SPF 50+, water resistant'
    },
    {
        'name': 'Body Lotion Cocoa Butter',
        'description': 'Deep moisturizing body lotion with cocoa butter.',
        'price': 379,
        'image_url': 'beauty/body_lotion_cocoa.jpg',
        'stock': 46,
        'category': 'beauty',
        'brand': 'Nivea',
        'model': 'Cocoa Nourish',
        'rating': 4.4,
        'warranty': 'No Warranty',
        'specifications': '400ml, cocoa butter formula'
    },
    {
        'name': 'Lip Balm Strawberry',
        'description': 'Moisturizing lip balm with strawberry flavor.',
        'price': 149,
        'image_url': 'beauty/lip_balm_strawberry.jpg',
        'stock': 80,
        'category': 'beauty',
        'brand': 'Maybelline',
        'model': 'Baby Lips',
        'rating': 4.2,
        'warranty': 'No Warranty',
        'specifications': '4g, SPF 20'
    },
    {
        'name': 'Matte Lipstick Nude',
        'description': 'Long-lasting matte nude lipstick.',
        'price': 399,
        'image_url': 'beauty/matte_lipstick_nude.jpg',
        'stock': 38,
        'category': 'beauty',
        'brand': 'Lakmé',
        'model': 'Nude Dream',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': 'Matte finish, long lasting'
    },
    {
        'name': 'Liquid Foundation Natural',
        'description': 'Lightweight liquid foundation with natural finish.',
        'price': 699,
        'image_url': 'beauty/foundation_natural.jpg',
        'stock': 25,
        'category': 'beauty',
        'brand': 'Maybelline',
        'model': 'Fit Me',
        'rating': 4.5,
        'warranty': 'No Warranty',
        'specifications': '30ml, natural finish'
    },
    {
        'name': 'Perfume Floral Mist',
        'description': 'Fresh floral fragrance for everyday wear.',
        'price': 899,
        'image_url': 'beauty/perfume_floral.jpg',
        'stock': 20,
        'category': 'beauty',
        'brand': 'Bella Vita',
        'model': 'Floral Mist',
        'rating': 4.1,
        'warranty': 'No Warranty',
        'specifications': '100ml eau de parfum'
    },
    {
        'name': 'Beard Trimmer Cordless',
        'description': 'Cordless beard trimmer with multiple length settings.',
        'price': 1599,
        'image_url': 'beauty/beard_trimmer.jpg',
        'stock': 18,
        'category': 'beauty',
        'brand': 'Philips',
        'model': 'BT1232',
        'rating': 4.4,
        'warranty': '2 Years',
        'specifications': 'USB charging, 30 min runtime'
    },
    {
        'name': 'Hair Dryer 1200W',
        'description': 'Compact hair dryer with heat and speed settings.',
        'price': 1299,
        'image_url': 'beauty/hair_dryer.jpg',
        'stock': 22,
        'category': 'beauty',
        'brand': 'Havells',
        'model': 'HD3151',
        'rating': 4.3,
        'warranty': '2 Years',
        'specifications': '1200W, 3 heat settings'
    },
    {
        'name': 'Facial Kit Gold',
        'description': 'Gold facial kit for glowing skin.',
        'price': 549,
        'image_url': 'beauty/facial_kit_gold.jpg',
        'stock': 30,
        'category': 'beauty',
        'brand': 'VLCC',
        'model': 'Gold Facial Kit',
        'rating': 4.2,
        'warranty': 'No Warranty',
        'specifications': '6-step facial kit'
    },
    {
        'name': 'Nail Paint Set 6 Shades',
        'description': 'Set of 6 vibrant nail paint shades.',
        'price': 299,
        'image_url': 'beauty/nail_paint_set.jpg',
        'stock': 44,
        'category': 'beauty',
        'brand': 'Colorbar',
        'model': 'Rainbow Set',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': 'Set of 6 shades, glossy finish'
    }
]

with app.app_context():
    existing = Product.query.filter_by(category='beauty').count()

    if existing >= 15:
        print(f'Beauty category already has {existing} products. Skipping insert.')
    else:
        for item in PRODUCTS:
            db.session.add(Product(**item))

        db.session.commit()
        print('Inserted 15 Beauty products successfully.')