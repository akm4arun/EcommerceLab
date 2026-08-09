# import ecommerce

# print("Imported module:", ecommerce)
# print("Module file:", ecommerce.__file__)
# print("Available attributes:", dir(ecommerce))

from ecommerce import create_app
from config import get_config

app = create_app(get_config())

# Register app config for templates BEFORE app.run()
@app.context_processor
def inject_config():
    return dict(app_config=app.config)

if __name__ == '__main__':
    app.run()