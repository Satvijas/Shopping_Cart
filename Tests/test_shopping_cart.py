from unittest.mock import Mock
from shopping_cart import ShoppingCart
import pytest


@pytest.fixture
def cart():
    # All setup for the cart here...
    return ShoppingCart(5)


def test_can_add_item_to_cart(cart):
    cart = ShoppingCart(5)
    cart.add("apple")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart = ShoppingCart(5)
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart):
    cart = ShoppingCart(5)
    for _ in range(5):
        cart.add("apple")

    with pytest.raises(OverflowError):
        cart.add("apple")