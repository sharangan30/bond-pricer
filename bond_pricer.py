def bond_price(face, coupon_rate, market_rate, years):
    value = 0
    payment = face*coupon_rate
    for i in range(1, years):
        value += payment/(1+ market_rate)**i

    value += (face + payment)/(1 + market_rate)**years
    return value


def ytm(price, face, coupon_rate, years, low = 0.0, high = 1.0):
    # if (price > bond_price(face, coupon_rate, 0, years)):
    #     raise ValueError("price is not achievable unless market rate is lower than 0")
    mid = (low + high)/2
    value = bond_price(face, coupon_rate, mid, years)
    if abs(value - price) < 1e-8:
        return mid
    elif (value < price):
        return ytm(price, face, coupon_rate, years, low, mid)
    else:
        return ytm(price, face, coupon_rate, years, mid, high)

if __name__ == "__main__":

    # print(bond_price(100, 0.05, 0.04, 3))
    # print(bond_price(100, 0.05, 0.06, 3))

    ytm(102.7751, 100, 0.05, 3)
    ytm(150, 100, 0.05, 3)

    
