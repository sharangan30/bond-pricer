from bond_pricer import bond_price
from ql_check import ql_bond_price

def test_premium_bond():
    assert(abs(bond_price(100, 0.05, 0.04, 3) - 102.77) < 0.01)

def test_discount_bond():
    assert(abs(bond_price(100, 0.05, 0.06, 3) - 97.33) < 0.01)

def test_matches_quantlib():
    assert(abs(ql_bond_price(100, 0.05, 0.04, 3) - bond_price(100, 0.05, 0.04, 3)) < 0.00001)

def test_matches_quantlib_two():
    assert(abs(ql_bond_price(1000, 0.05, 0.04, 3)/100*1000 - bond_price(1000, 0.05, 0.04, 3)) < 0.00001)