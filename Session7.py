num = 10

def show():
    global num          # GLOBAL KEYWORD

    num = 11
    num = num % 3
    print(">>1. num is:",num)

show()
print(">>2. num is:",num)

# Use Case
cart = []

def addProductToCart(product):

    global cart
    cart.append(product)