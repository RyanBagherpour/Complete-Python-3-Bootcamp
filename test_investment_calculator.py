"""
Unit tests for the Investment Compounding Calculator
"""

import unittest
import investment_calculator


class TestInvestmentCalculator(unittest.TestCase):
    """Test cases for the calculate_investment function"""
    
    def test_simple_calculation_no_contributions(self):
        """Test with only initial investment, no monthly contributions"""
        # $10,000 at 5% for 10 years
        result = investment_calculator.calculate_investment(10000, 0, 5, 10)
        expected = 10000 * ((1 + 0.05/12) ** (12 * 10))
        self.assertAlmostEqual(result, expected, places=2)
        self.assertAlmostEqual(result, 16470.09, places=2)
    
    def test_simple_calculation_with_contributions(self):
        """Test with initial investment and monthly contributions"""
        # $10,000 initial, $500/month at 7% for 20 years
        result = investment_calculator.calculate_investment(10000, 500, 7, 20)
        # Should be around $309,437
        self.assertGreater(result, 300000)
        self.assertLess(result, 320000)
    
    def test_zero_interest_rate(self):
        """Test with 0% interest rate (just sum of contributions)"""
        result = investment_calculator.calculate_investment(10000, 100, 0, 5)
        # 10000 + (100 * 12 * 5) = 10000 + 6000 = 16000
        expected = 16000
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_no_initial_investment(self):
        """Test with no initial investment, only monthly contributions"""
        result = investment_calculator.calculate_investment(0, 500, 6, 10)
        # Should be greater than just the sum of contributions
        total_contributions = 500 * 12 * 10
        self.assertGreater(result, total_contributions)
        # Should be around $81,939
        self.assertAlmostEqual(result, 81939.67, places=2)
    
    def test_one_year_investment(self):
        """Test with a short investment period of 1 year"""
        result = investment_calculator.calculate_investment(1000, 100, 5, 1)
        # Should be around 2265
        self.assertGreater(result, 2200)
        self.assertLess(result, 2300)
    
    def test_fractional_year(self):
        """Test with fractional years (e.g., 6 months = 0.5 years)"""
        result = investment_calculator.calculate_investment(5000, 200, 4, 0.5)
        # Should handle fractional years correctly
        self.assertGreater(result, 5000)
        self.assertLess(result, 7000)
    
    def test_high_interest_rate(self):
        """Test with a high interest rate"""
        result = investment_calculator.calculate_investment(10000, 1000, 15, 10)
        # High interest should result in significant growth
        self.assertGreater(result, 200000)
    
    def test_large_monthly_contribution(self):
        """Test with large monthly contributions"""
        result = investment_calculator.calculate_investment(5000, 5000, 8, 15)
        # Large contributions should dominate the final value
        total_contributions = 5000 + (5000 * 12 * 15)
        self.assertGreater(result, total_contributions)
    
    def test_negative_initial_investment_raises_error(self):
        """Test that negative initial investment raises ValueError"""
        with self.assertRaises(ValueError) as context:
            investment_calculator.calculate_investment(-1000, 100, 5, 10)
        self.assertIn("Initial investment cannot be negative", str(context.exception))
    
    def test_negative_monthly_contribution_raises_error(self):
        """Test that negative monthly contribution raises ValueError"""
        with self.assertRaises(ValueError) as context:
            investment_calculator.calculate_investment(1000, -100, 5, 10)
        self.assertIn("Monthly contribution cannot be negative", str(context.exception))
    
    def test_negative_interest_rate_raises_error(self):
        """Test that negative interest rate raises ValueError"""
        with self.assertRaises(ValueError) as context:
            investment_calculator.calculate_investment(1000, 100, -5, 10)
        self.assertIn("Interest rate cannot be negative", str(context.exception))
    
    def test_zero_years_raises_error(self):
        """Test that zero years raises ValueError"""
        with self.assertRaises(ValueError) as context:
            investment_calculator.calculate_investment(1000, 100, 5, 0)
        self.assertIn("Years must be greater than zero", str(context.exception))
    
    def test_negative_years_raises_error(self):
        """Test that negative years raises ValueError"""
        with self.assertRaises(ValueError) as context:
            investment_calculator.calculate_investment(1000, 100, 5, -10)
        self.assertIn("Years must be greater than zero", str(context.exception))
    
    def test_realistic_retirement_scenario(self):
        """Test a realistic retirement savings scenario"""
        # $25,000 initial, $500/month at 7% for 30 years
        result = investment_calculator.calculate_investment(25000, 500, 7, 30)
        # Should be substantial due to long time horizon
        self.assertGreater(result, 600000)
        self.assertLess(result, 850000)
    
    def test_small_values(self):
        """Test with small investment values"""
        result = investment_calculator.calculate_investment(100, 10, 3, 5)
        # Should handle small values correctly
        self.assertGreater(result, 100)
        self.assertLess(result, 1000)
    
    def test_consistency_across_different_periods(self):
        """Test that calculations are consistent across different time periods"""
        # 5 years should be less than 10 years with same parameters
        result_5_years = investment_calculator.calculate_investment(10000, 500, 7, 5)
        result_10_years = investment_calculator.calculate_investment(10000, 500, 7, 10)
        self.assertLess(result_5_years, result_10_years)


class TestInvestmentCalculatorEdgeCases(unittest.TestCase):
    """Test edge cases for the investment calculator"""
    
    def test_all_zeros_except_years(self):
        """Test with all zero inputs except years"""
        result = investment_calculator.calculate_investment(0, 0, 0, 5)
        self.assertEqual(result, 0)
    
    def test_only_initial_investment_no_interest(self):
        """Test with only initial investment and no interest"""
        result = investment_calculator.calculate_investment(5000, 0, 0, 10)
        self.assertEqual(result, 5000)
    
    def test_very_small_interest_rate(self):
        """Test with very small interest rate"""
        result = investment_calculator.calculate_investment(10000, 100, 0.01, 5)
        # Should be slightly more than just contributions
        self.assertGreater(result, 16000)


if __name__ == '__main__':
    unittest.main()
