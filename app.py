# import ecommerce

# print("Imported module:", ecommerce)
# print("Module file:", ecommerce.__file__)
# print("Available attributes:", dir(ecommerce))

from ecommerce import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)