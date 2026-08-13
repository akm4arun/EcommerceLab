# from app import create_app
# from ecommerce.extensions import db
# from ecommerce.models.product import Product

# app = create_app()

PRODUCTS = [
    {
        'name': 'Men Slim Fit T-Shirt',
        'description': 'Cotton slim fit casual T-shirt',
        'price': 799,
        'image_url': 'fashion/men_tshirt.jpg',
        'stock': 50,
        'category': 'fashion',
        'brand': 'Levis',
        'model': 'Slim Tee',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': '100% cotton, round neck, machine washable'
    },
    {
        'name': 'Women Floral Dress',
        'description': 'Elegant floral printed dress',
        'price': 1899,
        'image_url': 'fashion/floral_dress.jpg',
        'stock': 35,
        'category': 'fashion',
        'brand': 'Biba',
        'model': 'Flora',
        'rating': 4.5,
        'warranty': 'No Warranty',
        'specifications': 'Viscose fabric, midi length, floral print'
    },
    {
        'name': 'Men Denim Jeans',
        'description': 'Comfort stretch blue denim jeans',
        'price': 2199,
        'image_url': 'fashion/denim_jeans.jpg',
        'stock': 40,
        'category': 'fashion',
        'brand': 'Wrangler',
        'model': 'Stretch Blue',
        'rating': 4.4,
        'warranty': 'No Warranty',
        'specifications': '98% cotton, 2% elastane, slim fit'
    },
    {
        'name': 'Women Kurti Set',
        'description': 'Printed kurti with palazzo set',
        'price': 2499,
        'image_url': 'fashion/kurti_set.jpg',
        'stock': 30,
        'category': 'fashion',
        'brand': 'W',
        'model': 'Ethnic Bloom',
        'rating': 4.6,
        'warranty': 'No Warranty',
        'specifications': 'Cotton blend, 3-piece set'
    },
    {
        'name': 'Men Formal Shirt',
        'description': 'Full sleeve office wear formal shirt',
        'price': 1599,
        'image_url': 'fashion/formal_shirt.jpg',
        'stock': 45,
        'category': 'fashion',
        'brand': 'Arrow',
        'model': 'Office Pro',
        'rating': 4.2,
        'warranty': 'No Warranty',
        'specifications': 'Cotton blend, regular fit, full sleeve'
    },
    {
        'name': 'Women Handbag',
        'description': 'Premium faux leather handbag',
        'price': 2999,
        'image_url': 'fashion/handbag.jpg',
        'stock': 20,
        'category': 'fashion',
        'brand': 'Caprese',
        'model': 'Urban Chic',
        'rating': 4.4,
        'warranty': '6 Months',
        'specifications': 'Faux leather, zipper closure, 3 compartments'
    },
    {
        'name': 'Men Running Shoes',
        'description': 'Lightweight sports running shoes',
        'price': 3499,
        'image_url': 'fashion/running_shoes.jpg',
        'stock': 28,
        'category': 'fashion',
        'brand': 'Puma',
        'model': 'RunFlex',
        'rating': 4.5,
        'warranty': '3 Months',
        'specifications': 'Mesh upper, EVA sole, lightweight design'
    },
    {
        'name': 'Women Sneakers',
        'description': 'Trendy everyday casual sneakers',
        'price': 2799,
        'image_url': 'fashion/women_sneakers.jpg',
        'stock': 32,
        'category': 'fashion',
        'brand': 'Skechers',
        'model': 'Daily Walk',
        'rating': 4.6,
        'warranty': '3 Months',
        'specifications': 'Memory foam insole, breathable upper'
    },
    {
        'name': 'Men Hoodie Sweatshirt',
        'description': 'Warm fleece winter hoodie',
        'price': 1999,
        'image_url': 'fashion/hoodie.jpg',
        'stock': 26,
        'category': 'fashion',
        'brand': 'H&M',
        'model': 'Winter Warm',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': 'Fleece fabric, hooded, regular fit'
    },
    {
        'name': 'Women Leggings Pack',
        'description': 'Pack of 2 stretch leggings',
        'price': 999,
        'image_url': 'fashion/leggings.jpg',
        'stock': 60,
        'category': 'fashion',
        'brand': 'Jockey',
        'model': 'Stretch Pack',
        'rating': 4.2,
        'warranty': 'No Warranty',
        'specifications': 'Cotton Lycra, ankle length, pack of 2'
    },
    {
        'name': 'Men Leather Belt',
        'description': 'Genuine leather formal belt',
        'price': 1299,
        'image_url': 'fashion/belt.jpg',
        'stock': 55,
        'category': 'fashion',
        'brand': 'Allen Solly',
        'model': 'Classic Belt',
        'rating': 4.1,
        'warranty': '6 Months',
        'specifications': 'Genuine leather, metal buckle'
    },
    {
        'name': 'Women Saree Silk Blend',
        'description': 'Festive silk blend saree',
        'price': 3499,
        'image_url': 'fashion/saree.jpg',
        'stock': 18,
        'category': 'fashion',
        'brand': 'Pothys',
        'model': 'Festive Silk',
        'rating': 4.7,
        'warranty': 'No Warranty',
        'specifications': 'Silk blend, 6.3m length, blouse piece included'
    },
    {
        'name': 'Men Sports Cap',
        'description': 'Adjustable cotton sports cap',
        'price': 599,
        'image_url': 'fashion/cap.jpg',
        'stock': 70,
        'category': 'fashion',
        'brand': 'Nike',
        'model': 'Sport Cap',
        'rating': 4.3,
        'warranty': 'No Warranty',
        'specifications': 'Cotton fabric, adjustable strap'
    },
    {
        'name': 'Women Winter Jacket',
        'description': 'Quilted lightweight winter jacket',
        'price': 4299,
        'image_url': 'fashion/winter_jacket.jpg',
        'stock': 15,
        'category': 'fashion',
        'brand': 'Zara',
        'model': 'Quilted Warm',
        'rating': 4.6,
        'warranty': 'No Warranty',
        'specifications': 'Polyester fill, zip closure, insulated'
    },
    {
        'name': 'Men Casual Shorts',
        'description': 'Comfort cotton casual shorts',
        'price': 899,
        'image_url': 'fashion/shorts.jpg',
        'stock': 48,
        'category': 'fashion',
        'brand': 'US Polo',
        'model': 'Summer Comfort',
        'rating': 4.2,
        'warranty': 'No Warranty',
        'specifications': 'Cotton fabric, elastic waist, knee length'
    }
]

# with app.app_context():
#     existing = Product.query.filter_by(category='fashion').count()

#     if existing >= 15:
#         print(f'Fashion category already has {existing} products. Skipping insert.')
#     else:
#         for item in PRODUCTS:
#             product = Product(**item)
#             db.session.add(product)

#         db.session.commit()
#         print(f'Inserted {len(PRODUCTS)} fashion products successfully.')