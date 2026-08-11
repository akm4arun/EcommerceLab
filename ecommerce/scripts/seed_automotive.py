from app import create_app
from ecommerce.extensions import db
from ecommerce.models.product import Product

app = create_app()

PRODUCTS = [
    {
        'name': 'Car Vacuum Cleaner Portable',
        'description': 'Portable car vacuum cleaner with strong suction.',
        'price': 1799,
        'image_url': 'automotive/car_vacuum.jpg',
        'stock': 20,
        'category': 'automotive',
        'brand': 'Black+Decker',
        'model': 'PV1200AV',
        'rating': 4.4,
        'warranty': '1 Year',
        'specifications': '12V DC, portable, crevice tool included'
    },
    {
        'name': 'Tyre Inflator Digital',
        'description': 'Digital tyre inflator with auto shut-off.',
        'price': 2499,
        'image_url': 'automotive/tyre_inflator.jpg',
        'stock': 18,
        'category': 'automotive',
        'brand': 'Michelin',
        'model': '12266',
        'rating': 4.5,
        'warranty': '1 Year',
        'specifications': 'Digital display, auto shut-off, 12V'
    },
    {
        'name': 'Car Mobile Holder Dashboard',
        'description': 'Adjustable dashboard mobile holder for cars.',
        'price': 699,
        'image_url': 'automotive/mobile_holder.jpg',
        'stock': 50,
        'category': 'automotive',
        'brand': 'Portronics',
        'model': 'Clamp X',
        'rating': 4.2,
        'warranty': '6 Months',
        'specifications': '360° rotation, dashboard mount'
    },
    {
        'name': 'Seat Cover Set Premium',
        'description': 'Premium leatherette seat cover set for cars.',
        'price': 5999,
        'image_url': 'automotive/seat_cover_set.jpg',
        'stock': 10,
        'category': 'automotive',
        'brand': 'AutoFurnish',
        'model': 'Premium Fit',
        'rating': 4.3,
        'warranty': '6 Months',
        'specifications': 'Leatherette material, full set'
    },
    {
        'name': 'Car Air Freshener Gel',
        'description': 'Long-lasting gel car air freshener.',
        'price': 299,
        'image_url': 'automotive/air_freshener.jpg',
        'stock': 60,
        'category': 'automotive',
        'brand': 'Ambi Pur',
        'model': 'Ocean Breeze',
        'rating': 4.1,
        'warranty': 'No Warranty',
        'specifications': 'Gel type, fresh fragrance'
    },
    {
        'name': 'Engine Oil 5W-30 Fully Synthetic',
        'description': 'Fully synthetic engine oil for petrol engines.',
        'price': 2299,
        'image_url': 'automotive/engine_oil_5w30.jpg',
        'stock': 25,
        'category': 'automotive',
        'brand': 'Castrol',
        'model': 'Magnatec 5W-30',
        'rating': 4.7,
        'warranty': 'No Warranty',
        'specifications': '3.5L, fully synthetic'
    },
    {
        'name': 'Bike Helmet ISI Certified',
        'description': 'ISI certified full-face motorcycle helmet.',
        'price': 1999,
        'image_url': 'automotive/bike_helmet.jpg',
        'stock': 22,
        'category': 'automotive',
        'brand': 'Studds',
        'model': 'Shifter D2',
        'rating': 4.5,
        'warranty': '6 Months',
        'specifications': 'Full-face, ISI certified, visor included'
    },
    {
        'name': 'Car Cover Waterproof',
        'description': 'Waterproof dustproof car body cover.',
        'price': 1499,
        'image_url': 'automotive/car_cover.jpg',
        'stock': 28,
        'category': 'automotive',
        'brand': 'AutoKraftZ',
        'model': 'All Weather',
        'rating': 4.3,
        'warranty': '3 Months',
        'specifications': 'Waterproof fabric, UV protection'
    },
    {
        'name': 'Jump Starter Power Bank',
        'description': 'Portable jump starter with power bank feature.',
        'price': 4999,
        'image_url': 'automotive/jump_starter.jpg',
        'stock': 8,
        'category': 'automotive',
        'brand': 'Ambrane',
        'model': 'JumpStart Pro',
        'rating': 4.6,
        'warranty': '1 Year',
        'specifications': '10000mAh, USB output, LED torch'
    },
    {
        'name': 'Microfiber Cleaning Cloth Pack',
        'description': 'Soft microfiber cloths for car cleaning.',
        'price': 399,
        'image_url': 'automotive/microfiber_cloth.jpg',
        'stock': 70,
        'category': 'automotive',
        'brand': '3M',
        'model': 'Microfiber Pack',
        'rating': 4.4,
        'warranty': 'No Warranty',
        'specifications': 'Pack of 4, lint-free microfiber'
    },
    {
        'name': 'Car Pressure Washer Gun',
        'description': 'High-pressure washer gun attachment for car cleaning.',
        'price': 1299,
        'image_url': 'automotive/pressure_washer_gun.jpg',
        'stock': 16,
        'category': 'automotive',
        'brand': 'Bosch',
        'model': 'EasyClean Gun',
        'rating': 4.2,
        'warranty': '6 Months',
        'specifications': 'High-pressure spray, hose connector included'
    },
    {
        'name': 'Bike Phone Mount Handlebar',
        'description': 'Secure phone mount for motorcycle handlebars.',
        'price': 799,
        'image_url': 'automotive/bike_phone_mount.jpg',
        'stock': 34,
        'category': 'automotive',
        'brand': 'BOBO',
        'model': 'BM4',
        'rating': 4.5,
        'warranty': '6 Months',
        'specifications': 'Handlebar mount, anti-slip grip'
    },
    {
        'name': 'Dash Camera Full HD',
        'description': 'Full HD dash camera with night vision.',
        'price': 3999,
        'image_url': 'automotive/dash_camera.jpg',
        'stock': 12,
        'category': 'automotive',
        'brand': 'DDPAI',
        'model': 'Mini 5',
        'rating': 4.6,
        'warranty': '1 Year',
        'specifications': '1080p recording, night vision, loop recording'
    },
    {
        'name': 'Car Bluetooth FM Transmitter',
        'description': 'Bluetooth FM transmitter with USB charging.',
        'price': 999,
        'image_url': 'automotive/fm_transmitter.jpg',
        'stock': 26,
        'category': 'automotive',
        'brand': 'Portronics',
        'model': 'Auto 12',
        'rating': 4.1,
        'warranty': '6 Months',
        'specifications': 'Bluetooth 5.0, dual USB charging'
    },
    {
        'name': 'Alloy Wheel Cleaner Spray',
        'description': 'Foaming alloy wheel cleaner spray for cars.',
        'price': 549,
        'image_url': 'automotive/wheel_cleaner.jpg',
        'stock': 32,
        'category': 'automotive',
        'brand': '3M',
        'model': 'Wheel Shine',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': '500ml foam cleaner, alloy safe'
    }
]

with app.app_context():
    existing = Product.query.filter_by(category='automotive').count()

    if existing >= 15:
        print(f'Automotive category already has {existing} products. Skipping insert.')
    else:
        for item in PRODUCTS:
            db.session.add(Product(**item))

        db.session.commit()
        print('Inserted 15 Automotive products successfully.')