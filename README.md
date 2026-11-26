# Bond Pricer

Prices fixed-rate bonds with annual coupons by discounting each cash flow
at the market rate and calculates the yield to maturity value using the bond price using bisection. 
Written from scratch in Python and validated with pytest.


## Validation
- Premium bond (5% coupon, 4% market rate) checked against a hand calculation
- Discount bond (5% coupon, 6% market rate) checked against a hand calculation
- Round-trip test confirms ytm recovers each rate (1%, 4%, 7%, 15%) within 1e-5
- Impossible-price confirms ytm raises a ValueError when the price exceeds the total of all payments
- Matches QuantLib's `FixedRateBond` price to within 1e-5 at face values of 100 and 1000

## What I found
My first QuantLib comparison passed at face value 100 but failed at 1000.
QuantLib quotes bond prices per 100 of face value, while my function returns
the dollar price. The two only agree when face is 100, so the test converts
QuantLib's quote to dollars before comparing.

My first version of ytm crashed with a RecursionError when given the price of $150. 
The price is higher than the total payments over 3 years ($100 + $5 + $5 + $5 = $115), 
which requires a negative yield but the solver only checks yields from 0% to 100%. 
ytm now raises a ValueError if the price is higher than the total of the payments.

## Run it
pip install -r requirements.txt
pytest