#type:ignore
import pytest
from src.inventory import Inventory


@pytest.fixture
def inventory():
    return Inventory()

def test_add_item(inventory):
    inventory.add_item("apple", 10)
    assert inventory.get_quantity("apple") == 10

def test_negative_quantity(inventory):
    with pytest.raises(ValueError, match="Quantity must be a positive integer."):
        inventory.add_item("banana", -5)

def test_remove_item(inventory):
    inventory.add_item("cherry", 20)
    inventory.remove_item("cherry", 5)
    assert inventory.get_quantity("cherry") == 15
    inventory.remove_item("cherry", 15)
    assert "cherry" not in inventory.items

def test_remove_item_not_found(inventory):
    with pytest.raises(KeyError, match="cherry not found in inventory."):
        inventory.remove_item("cherry", 5)

def test_remove_item_insufficient_quantity(inventory):
    inventory.add_item("durian", 5)
    with pytest.raises(ValueError, match="Not enough durian(s) in inventory."):
        inventory.remove_item("durian", 10)