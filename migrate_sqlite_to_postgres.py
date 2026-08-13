import sqlite3
from sqlalchemy import create_engine, text

SQLITE_DB = 'instance/ecommerce.db'

POSTGRES_URL = (
    'postgresql+psycopg2://pgadmin:B%40blu%4030592@'
    'ecommercelab-pg.postgres.database.azure.com:5432/'
    'ecommercelab?sslmode=require'
)

sqlite_conn = sqlite3.connect(SQLITE_DB)
sqlite_conn.row_factory = sqlite3.Row
sqlite_cur = sqlite_conn.cursor()

engine = create_engine(POSTGRES_URL)

tables = ['users', 'products', 'orders', 'order_items']

with engine.begin() as pg_conn:
    for table in tables:
        rows = sqlite_cur.execute(f'SELECT * FROM {table}').fetchall()

        if not rows:
            print(f'No rows in {table}')
            continue

        columns = rows[0].keys()
        col_list = ', '.join(columns)
        placeholders = ', '.join([f':{c}' for c in columns])

        for row in rows:
            data = dict(row)

            if table == 'products' and 'is_active' in data:
                data['is_active'] = bool(data['is_active'])

            pg_conn.execute(
                text(f'INSERT INTO {table} ({col_list}) VALUES ({placeholders})'),
                data
            )

        print(f'Migrated {len(rows)} rows from {table}')

print('Migration completed successfully.')