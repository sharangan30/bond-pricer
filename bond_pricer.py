def bond_price(face, coupon_rate, market_rate, years):
    value = 0
    payment = face*coupon_rate
    for i in range(1, years):
        value += payment/(1+ market_rate)**i

    value += (face + payment)/(1 + market_rate)**years
    return value

if __name__ == "__main__":

    print(bond_price(100, 0.05, 0.04, 3))
    print(bond_price(100, 0.05, 0.06, 3))
