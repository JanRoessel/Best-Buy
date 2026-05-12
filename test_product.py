import pytest
from products import Product


def test_create_normal_product():
    """Test that creating a normal product works."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()


def test_create_product_invalid_details():
    """Test that invalid product details raise an exception."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive_at_zero_quantity():
    """Test that a product becomes inactive when quantity reaches 0."""
    product = Product("MacBook Air M2", price=1450, quantity=1)
    assert product.is_active()

    product.set_quantity(0)

    assert product.get_quantity() == 0
    assert not product.is_active()


def test_product_purchase_modifies_quantity_and_returns_output():
    """Test that buying a product reduces quantity and returns the correct total price."""
    product = Product("MacBook Air M2", price=1450, quantity=100)

    total_price = product.buy(3)

    assert total_price == 1450 * 3
    assert product.get_quantity() == 97


def test_buying_more_than_available_raises_exception():
    """Test that buying more quantity than in stock raises an exception."""
    product = Product("MacBook Air M2", price=1450, quantity=5)

    with pytest.raises(Exception):
        product.buy(10)