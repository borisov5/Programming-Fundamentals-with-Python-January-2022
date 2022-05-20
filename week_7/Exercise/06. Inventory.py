class Inventory:

    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []
        self.__storage = __capacity

    def add_item(self, item: str):
        if self.__capacity > 0:
            self.items.append(item)
            self.__capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__storage

    def __repr__(self):
        items = ", ".join(s for s in self.items)
        return f"Items: {items}.\nCapacity left: {self.__capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
