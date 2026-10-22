products = [
    "Laptop", "Smartphone", "Wireless Headphones", "Smartwatch", "Tablet",
    "Gaming Console", "Speaker", "External Hard Drive", "Monitor", "Keyboard",
    "Computer Mouse", "Printer", "Router", "Webcam", "Microphone",
    "VR Headset", "Fitness Tracker", "Drone", "Action Camera", "Electric Scooter"
]

def read_products(productslist):
    for product in productslist: 
        if product.startswith(('S', 's')): #or product.lower().startswith("s")
            yield product

for product in read_products(products):
    print(product)