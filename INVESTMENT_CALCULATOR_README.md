# Investment Compounding Calculator

A Python-based investment calculator that computes the final investment amount based on compound interest with monthly contributions.

## Features

- Calculate future value of investments with compound interest
- Support for initial investment amount
- Monthly contribution calculations
- Yearly interest rate (compounded monthly)
- Flexible time horizons (including fractional years)
- Input validation and error handling
- Detailed breakdown of contributions vs. earnings

## Usage

### Running the Calculator

```bash
python3 investment_calculator.py
```

### Interactive Input

The calculator will prompt you for the following inputs:

1. **Initial Investment Amount ($)**: The starting amount you're investing
2. **Monthly Contribution ($)**: The amount you'll contribute each month
3. **Yearly Interest Rate (%)**: The annual interest rate (e.g., enter 7 for 7%)
4. **Time Horizon (years)**: How long you plan to invest (can be fractional, e.g., 0.5 for 6 months)

### Example Session

```
============================================================
Investment Compounding Calculator
============================================================

Enter initial investment amount ($): 10000
Enter monthly contribution ($): 500
Enter yearly interest rate (%): 7
Enter time horizon (years): 20

============================================================
RESULTS
============================================================
Initial Investment:      $10,000.00
Monthly Contribution:    $500.00
Yearly Interest Rate:    7.00%
Time Horizon:            20.0 years
------------------------------------------------------------
Final Investment Amount: $300,850.72
============================================================

Total Contributed:       $130,000.00
Total Earnings:          $170,850.72
Return on Investment:    131.42%
```

## Using the Function Programmatically

You can also import and use the calculator function in your own code:

```python
from investment_calculator import calculate_investment

# Calculate investment value
final_amount = calculate_investment(
    initial_investment=10000,    # $10,000 initial
    monthly_contribution=500,     # $500 per month
    yearly_interest_rate=7,       # 7% annual interest
    years=20                      # 20 years
)

print(f"Final amount: ${final_amount:,.2f}")
```

## How It Works

The calculator uses the compound interest formula with two components:

1. **Future Value of Initial Investment:**
   ```
   FV_initial = P × (1 + r/12)^(12×t)
   ```

2. **Future Value of Monthly Contributions (Ordinary Annuity):**
   ```
   FV_contributions = PMT × [((1 + r/12)^(12×t) - 1) / (r/12)]
   ```

Where:
- P = Initial investment amount
- PMT = Monthly contribution
- r = Annual interest rate (as decimal)
- t = Time in years

## Testing

The calculator includes comprehensive unit tests covering:
- Various investment scenarios
- Edge cases (zero interest, no contributions, etc.)
- Input validation
- Error handling

Run the tests:

```bash
python3 -m unittest test_investment_calculator.py
```

Run tests with verbose output:

```bash
python3 -m unittest test_investment_calculator.py -v
```

## Input Validation

The calculator validates all inputs and will raise `ValueError` for:
- Negative initial investment
- Negative monthly contribution
- Negative interest rate
- Zero or negative time horizon

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Examples

### Retirement Savings
- Initial: $25,000
- Monthly: $500
- Interest: 7%
- Years: 30
- **Result: ~$812,898**

### Short-term Savings
- Initial: $5,000
- Monthly: $200
- Interest: 4%
- Years: 5
- **Result: ~$18,449**

### Aggressive Growth
- Initial: $10,000
- Monthly: $1,000
- Interest: 10%
- Years: 25
- **Result: ~$1,418,258**
