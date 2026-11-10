#!/usr/bin/env python3
"""DiscountCalc - price, discount, margin and markup calculator.

For buyers checking a deal and sellers checking their numbers.
Standard library only.
"""

import argparse
import sys


def money(value):
    return f"{value:.2f}"


def pct_label(value):
    # Show 25 instead of 25.0, but keep 12.5 as 12.5.
    if value == int(value):
        return str(int(value))
    return f"{value:g}"


def discount_block(price, discount):
    amount = price * discount / 100.0
    final = price - amount
    print(f"Original price: {money(price)}")
    print(f"Discount ({pct_label(discount)}%): -{money(amount)}")
    print(f"Final price: {money(final)}")
    print(f"You save: {money(amount)}")
    return final


def margin_block(cost, selling):
    profit = selling - cost
    margin = profit / selling * 100.0
    markup = profit / cost * 100.0
    print(f"Cost: {money(cost)}")
    print(f"Selling price: {money(selling)}")
    print(f"Profit: {money(profit)}")
    print(f"Margin: {margin:.1f}%")
    print(f"Markup: {markup:.1f}%")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Calculate discounts, margins and markups."
    )
    parser.add_argument("--price", type=float,
                        help="Original price (discount mode) or selling price (margin mode)")
    parser.add_argument("--discount", type=float,
                        help="Discount percent, e.g. 25")
    parser.add_argument("--cost", type=float, help="Cost price")
    args = parser.parse_args(argv)

    price, discount, cost = args.price, args.discount, args.cost

    for name, value in (("--price", price), ("--discount", discount),
                        ("--cost", cost)):
        if value is not None and value < 0:
            parser.error(f"{name} cannot be negative")
    if discount is not None and discount > 100:
        parser.error("--discount cannot be over 100")

    discount_mode = price is not None and discount is not None
    margin_mode = cost is not None and price is not None

    if not discount_mode and not margin_mode:
        parser.error(
            "no usable combination: give --price with --discount, "
            "or --cost with --price (or all three)"
        )

    if margin_mode and cost == 0:
        parser.error("--cost cannot be 0 in margin mode")

    selling = price
    if discount_mode:
        selling = discount_block(price, discount)
        if margin_mode:
            print("Margin on the discounted price:")

    if margin_mode:
        if selling == 0:
            parser.error("selling price cannot be 0 in margin mode")
        margin_block(cost, selling)

    return 0


if __name__ == "__main__":
    sys.exit(main())
