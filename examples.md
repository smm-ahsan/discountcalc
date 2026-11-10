# Examples

Real output from DiscountCalc, captured from actual runs.

## A discount - what you pay and what you save

Command:

```bash
python3 discountcalc.py --price 100 --discount 25
```

Output:

```
Original price: 100.00
Discount (25%): -25.00
Final price: 75.00
You save: 25.00
```

## Margin and markup on a sale

Command:

```bash
python3 discountcalc.py --cost 60 --price 100
```

Output:

```
Cost: 60.00
Selling price: 100.00
Profit: 40.00
Margin: 40.0%
Markup: 66.7%
```

Same 40.00 profit, two different percentages - margin is the profit as a share of the selling price, markup as a share of the cost.

## Both together - margin on the discounted price

Command:

```bash
python3 discountcalc.py --price 100 --discount 10 --cost 60
```

Output:

```
Original price: 100.00
Discount (10%): -10.00
Final price: 90.00
You save: 10.00
Margin on the discounted price:
Cost: 60.00
Selling price: 90.00
Profit: 30.00
Margin: 33.3%
Markup: 50.0%
```
