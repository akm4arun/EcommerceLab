
# seed_electronics.py

# from app import create_app
# from ecommerce import db
# from ecommerce.models.product import Product

# app = create_app()

PRODUCTS = [
    {
        'category': 'electronics',
        'name': 'Apple MacBook Air M4',
        'brand': 'Apple',
        'description': 'Apple MacBook Air with M4 chip, ultra-thin design and all-day battery life.',
        'price': 114900,
        'stock': 12,
        'image_url': 'electronics/macbook_air_m4.jpg',
        'rating': 4.8,
        'warranty': '1 Year Manufacturer Warranty',
        'specifications': 'Processor: Apple M4\nRAM: 16GB\nStorage: 512GB SSD\nDisplay: 13.6-inch Liquid Retina\nBattery: Up to 18 hours',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'Dell Inspiron 15 3530',
        'brand': 'Dell',
        'description': '15.6-inch laptop suitable for office work, coding, and daily productivity.',
        'price': 64990,
        'stock': 20,
        'image_url': 'electronics/dell_inspiron_3530.jpg',
        'rating': 4.4,
        'warranty': '1 Year Onsite Warranty',
        'specifications': 'Processor: Intel Core i5-1334U\nRAM: 16GB\nStorage: 512GB SSD\nDisplay: 15.6-inch FHD',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'Lenovo ThinkPad E16 Gen 2',
        'brand': 'Lenovo',
        'description': 'Business-class laptop with excellent keyboard and durability.',
        'price': 72990,
        'stock': 15,
        'image_url': 'electronics/thinkpad_e16.jpg',
        'rating': 4.6,
        'warranty': '1 Year Premier Support',
        'specifications': 'Processor: Intel Core Ultra 5\nRAM: 16GB\nStorage: 1TB SSD\nDisplay: 16-inch WUXGA IPS',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'HP Pavilion Plus 14',
        'brand': 'HP',
        'description': 'Premium thin-and-light laptop with high-resolution display.',
        'price': 81990,
        'stock': 10,
        'image_url': 'electronics/hp_pavilion_plus14.jpg',
        'rating': 4.5,
        'warranty': '1 Year Warranty',
        'specifications': 'Processor: Intel Core i7-1360P\nRAM: 16GB\nStorage: 1TB SSD\nDisplay: 14-inch 2.8K OLED',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'ASUS Vivobook S15 OLED',
        'brand': 'ASUS',
        'description': 'OLED laptop designed for creators and multimedia users.',
        'price': 76990,
        'stock': 14,
        'image_url': 'electronics/vivobook_s15_oled.jpg',
        'rating': 4.5,
        'warranty': '1 Year Global Warranty',
        'specifications': 'Processor: Intel Core Ultra 7\nRAM: 16GB\nStorage: 1TB SSD\nDisplay: 15.6-inch 3K OLED',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'LG 27US500 4K Monitor',
        'brand': 'LG',
        'description': '27-inch 4K IPS monitor with HDR10 support.',
        'price': 18999,
        'stock': 25,
        'image_url': 'electronics/lg_27us500.jpg',
        'rating': 4.6,
        'warranty': '3 Years Warranty',
        'specifications': 'Size: 27-inch\nResolution: 3840x2160\nPanel: IPS\nRefresh Rate: 60Hz',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'Samsung Smart Monitor M7 32',
        'brand': 'Samsung',
        'description': '4K smart monitor with built-in streaming apps.',
        'price': 29999,
        'stock': 18,
        'image_url': 'electronics/samsung_m7_32.jpg',
        'rating': 4.4,
        'warranty': '3 Years Warranty',
        'specifications': 'Size: 32-inch\nResolution: 4K UHD\nSmart TV Features: Yes\nConnectivity: HDMI, USB-C',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'Sony WH-1000XM5',
        'brand': 'Sony',
        'description': 'Industry-leading noise cancelling wireless headphones.',
        'price': 27990,
        'stock': 30,
        'image_url': 'electronics/sony_xm5.jpg',
        'rating': 4.9,
        'warranty': '1 Year Warranty',
        'specifications': 'Type: Over-ear Wireless\nNoise Cancellation: Yes\nBattery: Up to 30 hours',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'JBL Tune 770NC',
        'brand': 'JBL',
        'description': 'Wireless headphones with adaptive noise cancelling.',
        'price': 7999,
        'stock': 35,
        'image_url': 'electronics/jbl_770nc.jpg',
        'rating': 4.3,
        'warranty': '1 Year Warranty',
        'specifications': 'Type: Wireless\nNoise Cancellation: Yes\nBattery: Up to 50 hours',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'Logitech MX Master 3S',
        'brand': 'Logitech',
        'description': 'Premium productivity mouse for developers and creators.',
        'price': 9995,
        'stock': 40,
        'image_url': 'electronics/mx_master_3s.jpg',
        'rating': 4.8,
        'warranty': '1 Year Warranty',
        'specifications': 'Connectivity: Bluetooth/USB Receiver\nDPI: 8000\nButtons: 7',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'Logitech K380 Keyboard',
        'brand': 'Logitech',
        'description': 'Compact multi-device Bluetooth keyboard.',
        'price': 3495,
        'stock': 50,
        'image_url': 'electronics/k380_keyboard.jpg',
        'rating': 4.5,
        'warranty': '1 Year Warranty',
        'specifications': 'Type: Bluetooth Keyboard\nDevices: 3 simultaneous devices',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'Canon PIXMA G3010',
        'brand': 'Canon',
        'description': 'All-in-one Wi-Fi ink tank printer.',
        'price': 13990,
        'stock': 22,
        'image_url': 'electronics/canon_g3010.jpg',
        'rating': 4.2,
        'warranty': '1 Year Warranty',
        'specifications': 'Functions: Print/Scan/Copy\nConnectivity: Wi-Fi, USB',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'WD My Passport 2TB',
        'brand': 'Western Digital',
        'description': 'Portable external hard drive with hardware encryption.',
        'price': 6499,
        'stock': 60,
        'image_url': 'electronics/wd_mypassport_2tb.jpg',
        'rating': 4.6,
        'warranty': '3 Years Warranty',
        'specifications': 'Capacity: 2TB\nInterface: USB 3.2',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'Seagate Expansion 1TB SSD',
        'brand': 'Seagate',
        'description': 'Portable SSD with high-speed data transfer.',
        'price': 6999,
        'stock': 45,
        'image_url': 'electronics/seagate_ssd_1tb.jpg',
        'rating': 4.5,
        'warranty': '3 Years Warranty',
        'specifications': 'Capacity: 1TB\nType: Portable SSD\nInterface: USB-C',
        'is_active': True
    },
    {
        'category': 'electronics',
        'name': 'TP-Link Archer AX55 Wi-Fi 6 Router',
        'brand': 'TP-Link',
        'description': 'Dual-band Wi-Fi 6 router for high-speed home networking.',
        'price': 5999,
        'stock': 28,
        'image_url': 'electronics/tplink_ax55.jpg',
        'rating': 4.4,
        'warranty': '3 Years Warranty',
        'specifications': 'Wi-Fi Standard: Wi-Fi 6\nBands: Dual Band\nPorts: Gigabit Ethernet',
        'is_active': True
    }
]

# with app.app_context():
#     existing = Product.query.filter_by(category='electronics').count()

#     if existing > 0:
#         print(f'Electronics category already has {existing} products. Skipping insert.')
#     else:
#         for item in PRODUCTS:
#             product = Product(**item)
#             db.session.add(product)

#         db.session.commit()
#         print(f'Inserted {len(PRODUCTS)} electronics products successfully.')

