# DiscountCalc

A tiny command line calculator for prices, discounts, margins and markups - for buyers checking a deal and sellers checking their numbers.

**Margin vs markup:** margin is the profit as a share of the selling price, markup is the profit as a share of the cost.
The same profit gives two different percentages - margin is always the smaller one, and mixing them up quietly overstates what you earn.

## Requirements

- Python 3
- Standard library only - nothing to install

## Usage

Discount - what you actually pay, and what you save:

```bash
python3 discountcalc.py --price 100 --discount 25
```

Margin and markup - give cost and selling price:

```bash
python3 discountcalc.py --cost 60 --price 100
```

Both together - the margin is worked out on the discounted price:

```bash
python3 discountcalc.py --price 100 --discount 10 --cost 60
```

See `examples.md` for real output.

## License

MIT - see `LICENSE`.
