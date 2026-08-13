# from app import create_app
# from ecommerce.extensions import db
# from ecommerce.models.product import Product

# app = create_app()

PRODUCTS = [
    {
        'name': 'Atomic Habits',
        'description': 'Build good habits and break bad ones.',
        'price': 599,
        'image_url': 'books/atomic_habits.jpg',
        'stock': 40,
        'category': 'books',
        'brand': 'Penguin',
        'model': 'Paperback',
        'rating': 4.8,
        'specifications': 'English, Paperback, 320 pages'
    },
    {
    'name': 'The Pragmatic Programmer',
    'category': 'books',
    'price': 699,
    'description': 'Your journey to mastery.',
    'image_url': 'books/pragmatic_programmer.jpg',
    'stock': 30,
    'brand': 'Addison-Wesley',
    'model': 'Paperback',
    'rating': 4.7,
    'specifications': 'English, Paperback, 352 pages'
    },
    {
        'name': 'Clean Code',
        'description': 'A Handbook of Agile Software Craftsmanship.',
        'price': 799,
        'image_url': 'books/clean_code.jpg',
        'stock': 25,
        'category': 'books',
        'brand': 'Prentice Hall',
        'model': 'Paperback',
        'rating': 4.6,
        'specifications': 'English, Paperback, 464 pages'
    },
    {
        'name': 'The Lean Startup',
        'description': 'How today’s entrepreneurs use continuous innovation.',
        'price': 499,
        'image_url': 'books/lean_startup.jpg',
        'stock': 30,
        'category': 'books',
        'brand': 'Crown Business',
        'model': 'Paperback',
        'rating': 4.5,
        'specifications': 'English, Paperback, 336 pages'
    },
    {
        'name': 'The Psychology of Money',
        'description': 'Timeless lessons on wealth and behavior.',
        'price': 399,
        'image_url': 'books/psychology_of_money.jpg',
        'stock': 35,
        'category': 'books',
        'brand': 'Jaico',
        'model': 'Paperback',
        'rating': 4.7,
        'specifications': 'English, Paperback, 256 pages'
    },
    {
        'name': 'Rich Dad Poor Dad',
        'description': 'Personal finance classic by Robert Kiyosaki.',
        'price': 350,
        'image_url': 'books/rich_dad_poor_dad.jpg',
        'stock': 50,
        'category': 'books',
        'brand': 'Plata Publishing',
        'model': 'Paperback',
        'rating': 4.6,
        'specifications': 'English, Paperback, 336 pages'
    },
    {
        'name': 'Ikigai',
        'description': 'Japanese secret to a long and happy life.',
        'price': 299,
        'image_url': 'books/ikigai.jpg',
        'stock': 45,
        'category': 'books',
        'brand': 'Penguin',
        'model': 'Paperback',
        'rating': 4.5,
        'specifications': 'English, Paperback, 208 pages'
    },
    {
        'name': 'Deep Work',
        'description': 'Rules for focused success in a distracted world.',
        'price': 450,
        'image_url': 'books/deep_work.jpg',
        'stock': 28,
        'category': 'books',
        'brand': 'Piatkus',
        'model': 'Paperback',
        'rating': 4.7,
        'specifications': 'English, Paperback, 304 pages'
    },
    {
        'name': 'Sapiens',
        'description': 'A brief history of humankind.',
        'price': 599,
        'image_url': 'books/sapiens.jpg',
        'stock': 20,
        'category': 'books',
        'brand': 'Harper',
        'model': 'Paperback',
        'rating': 4.8,
        'specifications': 'English, Paperback, 512 pages'
    },
    {
        'name': 'The Alchemist',
        'description': 'Inspirational novel by Paulo Coelho.',
        'price': 250,
        'image_url': 'books/the_alchemist.jpg',
        'stock': 60,
        'category': 'books',
        'brand': 'HarperCollins',
        'model': 'Paperback',
        'rating': 4.6,
        'specifications': 'English, Paperback, 208 pages'
    },
    {
        'name': 'Think and Grow Rich',
        'description': 'Classic success and wealth book.',
        'price': 299,
        'image_url': 'books/think_and_grow_rich.jpg',
        'stock': 38,
        'category': 'books',
        'brand': 'Fingerprint',
        'model': 'Paperback',
        'rating': 4.5,
        'specifications': 'English, Paperback, 320 pages'
    },
    {
        'name': 'Can’t Hurt Me',
        'description': 'Master your mind and defy the odds.',
        'price': 699,
        'image_url': 'books/cant_hurt_me.jpg',
        'stock': 18,
        'category': 'books',
        'brand': 'Lioncrest',
        'model': 'Paperback',
        'rating': 4.8,
        'specifications': 'English, Paperback, 364 pages'
    },
    {
        'name': 'Zero to One',
        'description': 'Notes on startups and building the future.',
        'price': 399,
        'image_url': 'books/zero_to_one.jpg',
        'stock': 26,
        'category': 'books',
        'brand': 'Crown Business',
        'model': 'Paperback',
        'rating': 4.5,
        'specifications': 'English, Paperback, 224 pages'
    },
    {
        'name': 'The Power of Your Subconscious Mind',
        'description': 'Unlock the power of your subconscious.',
        'price': 275,
        'image_url': 'books/subconscious_mind.jpg',
        'stock': 42,
        'category': 'books',
        'brand': 'Fingerprint',
        'model': 'Paperback',
        'rating': 4.4,
        'specifications': 'English, Paperback, 312 pages'
    },
    {
        'name': 'Start With Why',
        'description': 'How great leaders inspire action.',
        'price': 499,
        'image_url': 'books/start_with_why.jpg',
        'stock': 24,
        'category': 'books',
        'brand': 'Portfolio',
        'model': 'Paperback',
        'rating': 4.6,
        'specifications': 'English, Paperback, 256 pages'
    },
    {
        'name': 'The Intelligent Investor',
        'description': 'The definitive book on value investing.',
        'price': 799,
        'image_url': 'books/intelligent_investor.jpg',
        'stock': 15,
        'category': 'books',
        'brand': 'Harper Business',
        'model': 'Paperback',
        'rating': 4.8,
        'specifications': 'English, Paperback, 640 pages'
    },
    {
        'name': 'Man’s Search for Meaning',
        'description': 'Memoir and psychological exploration by Viktor Frankl.',
        'price': 349,
        'image_url': 'books/mans_search_for_meaning.jpg',
        'stock': 30,
        'category': 'books',
        'brand': 'Beacon Press',
        'model': 'Paperback',
        'rating': 4.7,
        'specifications': 'English, Paperback, 184 pages'
    },
    {
        'name': 'The 7 Habits of Highly Effective People',
        'description': 'Powerful lessons in personal change.',
        'price': 549,
        'image_url': 'books/7_habits.jpg',
        'stock': 22,
        'category': 'books',
        'brand': 'Simon & Schuster',
        'model': 'Paperback',
        'rating': 4.7,
        'specifications': 'English, Paperback, 432 pages'
    }
]

# with app.app_context():
#     existing = Product.query.filter_by(category='books').count()

#     if existing >= 15:
#         print(f'Books category already has {existing} products. Skipping insert.')
#     else:
#         for item in PRODUCTS:
#             product = Product(**item)
#             db.session.add(product)

#         db.session.commit()
#         print('Inserted 15 Books products successfully.')