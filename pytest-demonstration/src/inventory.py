class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_name: str, quantity: int)->None:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.items[item_name] = self.items.get(item_name, 0) + quantity
        print(f"Added {quantity} {item_name}(s). New total: {self.items[item_name]}")
    
    def remove_item(self, item_name: str, quantity: int)->None:
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if item_name not in self.items:
            raise KeyError(f"{item_name} not found in inventory.")
        if self.items[item_name] < quantity:
            raise ValueError(f"Not enough {item_name}s in inventory.")
        self.items[item_name] -= quantity
        print(f"Removed {quantity} {item_name}(s). New total: {self.items[item_name]}")
        if self.items[item_name] == 0:
            del self.items[item_name]
        
    def get_quantity(self, item_name: str)->int:
        return self.items.get(item_name, 0)
    
    