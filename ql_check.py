import QuantLib as ql

def ql_bond_price(face, coupon_rate, market_rate, years):

    today = ql.Date(23, 11, 2026)
    ql.Settings.instance().evaluationDate = today

    maturity = today + ql.Period(years, ql.Years)
    schedule = ql.Schedule(today, maturity, ql.Period(ql.Annual), ql.NullCalendar(),
                        ql.Unadjusted, ql.Unadjusted, ql.DateGeneration.Backward, False)

    dc = ql.Thirty360(ql.Thirty360.BondBasis)
    bond = ql.FixedRateBond(0, face, schedule, [coupon_rate], dc)

    return bond.cleanPrice(market_rate, dc, ql.Compounded, ql.Annual)

