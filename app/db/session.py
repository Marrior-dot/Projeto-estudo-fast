memory_db = {
    "fruits": [
        {"name": "Apple", "color": "Red"},
        {"name": "Banana", "color": "Yellow"},
        {"name": "Orange", "color": "Orange"},
        {"name": "Grape", "color": "Purple/Green"},
        {"name": "Watermelon", "color": "Green/Red"},
        {"name": "Strawberry", "color": "Red"},
        {"name": "Mango", "color": "Yellow/Orange"},
        {"name": "Pineapple", "color": "Yellow/Brown"},
        {"name": "Kiwi", "color": "Brown/Green"},
        {"name": "Peach", "color": "Pink/Orange"},
    ]
}

def fruit_exists(name: str) -> bool:
    return {"name": name} in memory_db["fruits"] if True else False

def get_fruits():
    return memory_db["fruits"]