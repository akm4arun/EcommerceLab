from app import create_app
from ecommerce.extensions import db
from ecommerce.models.product import Product

app = create_app()

PRODUCTS = [
    {
        'name': 'Air Fryer 4L',
        'description': '4-liter digital air fryer with rapid hot air technology.',
        'price': 5499,
        'image_url': 'air_fryer_4l.jpg',
        'stock': 18,
        'category': 'home-kitchen',
        'brand': 'Philips',
        'model': 'HD9200',
        'rating': 4.6,
        'specifications': '4L capacity, 1400W, digital controls'
    },
    {
        'name': 'Mixer Grinder 750W',
        'description': '750W mixer grinder with 3 stainless steel jars.',
        'price': 3499,
        'image_url': 'mixer_grinder_750w.jpg',
        'stock': 22,
        'category': 'home-kitchen',
        'brand': 'Prestige',
        'model': 'Iris Plus',
        'rating': 4.3,
        'specifications': '750W motor, 3 jars, overload protection'
    },
    {
        'name': 'Induction Cooktop',
        'description': 'Energy-efficient induction cooktop with touch controls.',
        'price': 2499,
        'image_url': 'induction_cooktop.jpg',
        'stock': 30,
        'category': 'home-kitchen',
        'brand': 'Bajaj',
        'model': 'Majesty ICX',
        'rating': 4.2,
        'specifications': '2000W, touch panel, timer'
    },
    {
        'name': 'Electric Kettle 1.5L',
        'description': 'Fast boiling stainless steel electric kettle.',
        'price': 1299,
        'image_url': 'electric_kettle_1_5l.jpg',
        'stock': 35,
        'category': 'home-kitchen',
        'brand': 'Pigeon',
        'model': 'Amaze Plus',
        'rating': 4.4,
        'specifications': '1.5L, stainless steel body, auto shut-off'
    },
    {
        'name': 'Cookware Set 5 Pieces',
        'description': 'Non-stick cookware set suitable for gas and induction.',
        'price': 3999,
        'image_url': 'cookware_set_5pc.jpg',
        'stock': 16,
        'category': 'home-kitchen',
        'brand': 'Wonderchef',
        'model': 'Royal Velvet',
        'rating': 4.5,
        'specifications': '5 pieces, non-stick coating, induction base'
    },
    {
        'name': 'Stainless Steel Dinner Set',
        'description': '24-piece stainless steel dinner set for family use.',
        'price': 2799,
        'image_url': 'dinner_set_24pc.jpg',
        'stock': 20,
        'category': 'home-kitchen',
        'brand': 'Cello',
        'model': 'Classic 24',
        'rating': 4.1,
        'specifications': '24 pieces, food-grade stainless steel'
    },
    {
        'name': 'Vacuum Cleaner 1200W',
        'description': 'Compact vacuum cleaner with powerful suction.',
        'price': 4599,
        'image_url': 'vacuum_cleaner_1200w.jpg',
        'stock': 14,
        'category': 'home-kitchen',
        'brand': 'Eureka Forbes',
        'model': 'Quick Clean',
        'rating': 4.3,
        'specifications': '1200W, dry vacuum, reusable dust bag'
    },
    {
        'name': 'Steam Iron 1600W',
        'description': 'Steam iron with ceramic soleplate and spray function.',
        'price': 1799,
        'image_url': 'steam_iron_1600w.jpg',
        'stock': 28,
        'category': 'home-kitchen',
        'brand': 'Philips',
        'model': 'GC1905',
        'rating': 4.4,
        'specifications': '1600W, steam burst, ceramic soleplate'
    },
    {
        'name': 'Water Bottle Set 6 Pieces',
        'description': 'BPA-free refrigerator water bottle set.',
        'price': 799,
        'image_url': 'water_bottle_set_6pc.jpg',
        'stock': 40,
        'category': 'home-kitchen',
        'brand': 'Milton',
        'model': 'Fridge Set',
        'rating': 4.2,
        'specifications': '6 bottles, BPA-free plastic, 1L each'
    },
    {
        'name': 'Storage Container Set',
        'description': 'Airtight kitchen storage containers for dry food.',
        'price': 1599,
        'image_url': 'storage_container_set.jpg',
        'stock': 26,
        'category': 'home-kitchen',
        'brand': 'Signoraware',
        'model': 'Airtight Set',
        'rating': 4.5,
        'specifications': 'Set of 8, airtight lids, food-safe plastic'
    },
    {
        'name': 'Pressure Cooker 5L',
        'description': 'Hard anodized pressure cooker for everyday cooking.',
        'price': 2899,
        'image_url': 'pressure_cooker_5l.jpg',
        'stock': 19,
        'category': 'home-kitchen',
        'brand': 'Hawkins',
        'model': 'Contura 5L',
        'rating': 4.6,
        'specifications': '5L, hard anodized body, induction compatible'
    },
    {
        'name': 'Chimney 60cm',
        'description': 'Wall-mounted kitchen chimney with auto-clean feature.',
        'price': 8999,
        'image_url': 'chimney_60cm.jpg',
        'stock': 8,
        'category': 'home-kitchen',
        'brand': 'Faber',
        'model': 'Hood Crest',
        'rating': 4.3,
        'specifications': '60cm, auto-clean, 1200 m3/hr suction'
    },
    {
        'name': 'Microwave Oven 20L',
        'description': 'Solo microwave oven for reheating and cooking.',
        'price': 6499,
        'image_url': 'microwave_20l.jpg',
        'stock': 12,
        'category': 'home-kitchen',
        'brand': 'LG',
        'model': 'MS2043DB',
        'rating': 4.4,
        'specifications': '20L, solo, 700W'
    },
    {
        'name': 'Hand Blender 300W',
        'description': 'Lightweight hand blender for smoothies and soups.',
        'price': 1399,
        'image_url': 'hand_blender_300w.jpg',
        'stock': 24,
        'category': 'home-kitchen',
        'brand': 'Inalsa',
        'model': 'Robot INOX',
        'rating': 4.1,
        'specifications': '300W, stainless steel shaft'
    },
    {
        'name': 'Rice Cooker 1.8L',
        'description': 'Automatic rice cooker with keep-warm function.',
        'price': 2299,
        'image_url': 'rice_cooker_1_8l.jpg',
        'stock': 21,
        'category': 'home-kitchen',
        'brand': 'Panasonic',
        'model': 'SR-WA18',
        'rating': 4.3,
        'specifications': '1.8L, keep warm, detachable pot'
    }
]

with app.app_context():
    existing = Product.query.filter_by(category='home-kitchen').count()

    if existing >= 15:
        print(f'Home & Kitchen category already has {existing} products. Skipping insert.')
    else:
        for item in PRODUCTS:
            product = Product(**item)
            db.session.add(product)

        db.session.commit()
        print('Inserted 15 Home & Kitchen products successfully.')