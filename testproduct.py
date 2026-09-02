import pytest

from products import Product


def test_creating_prod():
    prod = Product("Macbook Prod",  125, 16)

    assert prod.name == "Macbook Prod"
    assert prod.price == 125
    assert prod.quantity == 16
    assert prod.is_active() == True

def test_creating_prod_invalid_details():
    with pytest.raises(ValueError):
        prod = Product("", 1250, -16)

def test_prod_becomes_inactive  ():
    prod = Product("Macbook Prod", 1250, 16)
    prod.set_quantity(0)

    assert prod.is_active() == False

def test_buy_modifies_quantity():
    prod = Product("Macbook Prod", 1250, 16)
    result = prod.buy(6)
    assert prod.quantity == 10
    assert result == 7500

def test_buy_too_much():
    prod = Product("Macbook Prod", 1250, 16)
    with pytest.raises(ValueError):
        prod.buy(17)