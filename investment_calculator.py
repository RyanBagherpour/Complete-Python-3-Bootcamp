"""
Investment Compounding Calculator

This module provides a function to calculate the final investment amount
based on initial investment, monthly contributions, interest rate, and time horizon.
"""


def calculate_investment(initial_investment, monthly_contribution, yearly_interest_rate, years):
    """
    Calculate the final investment amount with compound interest.
    
    The calculation accounts for:
    - Initial investment
    - Monthly contributions
    - Yearly interest rate compounded monthly
    - Time horizon in years
    
    Formula:
    - Initial investment grows with compound interest: P * (1 + r/12)^(12*t)
    - Monthly contributions form an annuity: PMT * [((1 + r/12)^(12*t) - 1) / (r/12)]
    
    Args:
        initial_investment (float): The starting investment amount
        monthly_contribution (float): The amount contributed each month
        yearly_interest_rate (float): The annual interest rate as a percentage (e.g., 7 for 7%)
        years (float): The investment time horizon in years
    
    Returns:
        float: The final investment amount after the specified time period
    
    Raises:
        ValueError: If any input is negative or if years is zero or negative
    """
    # Validate inputs
    if initial_investment < 0:
        raise ValueError("Initial investment cannot be negative")
    if monthly_contribution < 0:
        raise ValueError("Monthly contribution cannot be negative")
    if yearly_interest_rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if years <= 0:
        raise ValueError("Years must be greater than zero")
    
    # Convert yearly interest rate from percentage to decimal
    annual_rate = yearly_interest_rate / 100
    
    # Calculate monthly interest rate
    monthly_rate = annual_rate / 12
    
    # Calculate total number of months
    total_months = years * 12
    
    # Calculate future value of initial investment
    if monthly_rate == 0:
        # If interest rate is 0, just add up the contributions
        future_value_initial = initial_investment
        future_value_contributions = monthly_contribution * total_months
    else:
        # Future value of initial investment with compound interest
        future_value_initial = initial_investment * ((1 + monthly_rate) ** total_months)
        
        # Future value of monthly contributions (ordinary annuity)
        # PMT * [((1 + r)^n - 1) / r]
        future_value_contributions = monthly_contribution * (
            ((1 + monthly_rate) ** total_months - 1) / monthly_rate
        )
    
    # Total future value
    total_future_value = future_value_initial + future_value_contributions
    
    return total_future_value


def main():
    """
    Main function to run the investment calculator interactively.
    Prompts user for inputs and displays the calculated result.
    """
    print("=" * 60)
    print("Investment Compounding Calculator")
    print("=" * 60)
    print()
    
    try:
        # Get user inputs
        initial_investment = float(input("Enter initial investment amount ($): "))
        monthly_contribution = float(input("Enter monthly contribution ($): "))
        yearly_interest_rate = float(input("Enter yearly interest rate (%): "))
        years = float(input("Enter time horizon (years): "))
        
        # Calculate final investment
        final_amount = calculate_investment(
            initial_investment,
            monthly_contribution,
            yearly_interest_rate,
            years
        )
        
        # Display results
        print()
        print("=" * 60)
        print("RESULTS")
        print("=" * 60)
        print(f"Initial Investment:      ${initial_investment:,.2f}")
        print(f"Monthly Contribution:    ${monthly_contribution:,.2f}")
        print(f"Yearly Interest Rate:    {yearly_interest_rate:.2f}%")
        print(f"Time Horizon:            {years:.1f} years")
        print("-" * 60)
        print(f"Final Investment Amount: ${final_amount:,.2f}")
        print("=" * 60)
        
        # Calculate total contributions and earnings
        total_contributions = initial_investment + (monthly_contribution * years * 12)
        total_earnings = final_amount - total_contributions
        
        print()
        print(f"Total Contributed:       ${total_contributions:,.2f}")
        print(f"Total Earnings:          ${total_earnings:,.2f}")
        print(f"Return on Investment:    {(total_earnings / total_contributions * 100):.2f}%")
        print()
        
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please enter valid numeric values.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
