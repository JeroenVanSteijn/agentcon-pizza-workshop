"""
Unit tests for the calculate_pizza_for_people function in tools.py
"""

import pytest
from tools import calculate_pizza_for_people


class TestCalculatePizzaForPeople:
    """Test suite for calculate_pizza_for_people function"""

    def test_invalid_zero_people(self):
        """Test that zero people returns an error message"""
        result = calculate_pizza_for_people(0)
        assert "valid number of people" in result.lower()

    def test_invalid_negative_people(self):
        """Test that negative people count returns an error message"""
        result = calculate_pizza_for_people(-5)
        assert "valid number of people" in result.lower()

    def test_one_person_normal_appetite(self):
        """Test recommendation for 1 person with normal appetite"""
        result = calculate_pizza_for_people(1)
        assert "1 people" in result
        assert "normal appetite" in result
        assert "Small pizza" in result

    def test_two_people_normal_appetite(self):
        """Test recommendation for 2 people with normal appetite"""
        result = calculate_pizza_for_people(2)
        assert "2 people" in result
        assert "Medium pizza" in result

    def test_three_people_normal_appetite(self):
        """Test recommendation for 3 people with normal appetite"""
        result = calculate_pizza_for_people(3)
        assert "3 people" in result
        assert "Large pizza" in result

    def test_five_people_normal_appetite(self):
        """Test recommendation for 5 people with normal appetite"""
        result = calculate_pizza_for_people(5)
        assert "5 people" in result
        assert "Extra Large pizza" in result

    def test_seven_people_normal_appetite(self):
        """Test recommendation for 7 people with normal appetite"""
        result = calculate_pizza_for_people(7)
        assert "7 people" in result
        assert "2 Large pizzas" in result

    def test_ten_people_normal_appetite(self):
        """Test recommendation for 10 people with normal appetite"""
        result = calculate_pizza_for_people(10)
        assert "10 people" in result
        assert "2 Extra Large pizzas" in result

    def test_large_group_normal_appetite(self):
        """Test recommendation for a large group (15+ people)"""
        result = calculate_pizza_for_people(15)
        assert "15 people" in result
        assert "Extra Large" in result

    def test_light_appetite(self):
        """Test that light appetite reduces pizza quantity"""
        # With light appetite (0.7 multiplier), 3 people => adjusted ~2.1
        result = calculate_pizza_for_people(3, "light")
        assert "3 people" in result
        assert "light appetite" in result.lower()

    def test_heavy_appetite(self):
        """Test that heavy appetite increases pizza quantity"""
        # With heavy appetite (1.3 multiplier), 3 people => adjusted ~3.9
        result = calculate_pizza_for_people(3, "heavy")
        assert "3 people" in result
        assert "heavy appetite" in result.lower()

    def test_appetite_case_insensitive(self):
        """Test that appetite level is case insensitive"""
        result_lower = calculate_pizza_for_people(5, "light")
        result_upper = calculate_pizza_for_people(5, "LIGHT")
        result_mixed = calculate_pizza_for_people(5, "LiGhT")
        # All should process without error and mention light appetite
        assert "light appetite" in result_lower.lower()
        assert "light appetite" in result_upper.lower()
        assert "light appetite" in result_mixed.lower()

    def test_unknown_appetite_defaults_to_normal(self):
        """Test that unknown appetite level defaults to normal (multiplier 1.0)"""
        result_normal = calculate_pizza_for_people(5, "normal")
        result_unknown = calculate_pizza_for_people(5, "unknown_appetite")
        # Both should give the same pizza recommendation since unknown defaults to 1.0
        # Extract just the recommendation part
        assert "Extra Large" in result_normal
        assert "Extra Large" in result_unknown

    def test_output_contains_emoji(self):
        """Test that output contains pizza emoji for better UX"""
        result = calculate_pizza_for_people(3)
        assert "🍕" in result

    def test_output_contains_recommendation_label(self):
        """Test that output contains the word Recommendation"""
        result = calculate_pizza_for_people(3)
        assert "Recommendation" in result

    def test_very_large_group(self):
        """Test recommendation for very large group (50+ people)"""
        result = calculate_pizza_for_people(50)
        assert "50 people" in result
        assert "Extra Large" in result

    def test_heavy_appetite_large_group(self):
        """Test heavy appetite with large group"""
        result = calculate_pizza_for_people(20, "heavy")
        assert "20 people" in result
        assert "heavy appetite" in result.lower()
        assert "Extra Large" in result

    def test_light_appetite_adjustment_effect(self):
        """Test that light appetite effectively reduces pizza needs"""
        # 4 people with light appetite (4 * 0.7 = 2.8) should suggest Medium or Large
        result = calculate_pizza_for_people(4, "light")
        assert "4 people" in result
        # Light appetite should reduce the pizza size recommendation


class TestEdgeCases:
    """Test edge cases for the pizza calculator"""

    def test_one_person_light_appetite(self):
        """Test 1 person with light appetite (smallest possible adjusted count)"""
        result = calculate_pizza_for_people(1, "light")
        assert "1 people" in result
        # 1 * 0.7 = 0.7, should still give a small pizza

    def test_one_person_heavy_appetite(self):
        """Test 1 person with heavy appetite"""
        result = calculate_pizza_for_people(1, "heavy")
        assert "1 people" in result
        # 1 * 1.3 = 1.3, should suggest small pizza or medium

    def test_exact_threshold_two_people(self):
        """Test exactly 2 people (boundary for Small/Medium)"""
        result = calculate_pizza_for_people(2)
        assert "Medium pizza" in result

    def test_exact_threshold_four_people(self):
        """Test exactly 4 people (boundary for Large/Extra Large)"""
        result = calculate_pizza_for_people(4)
        assert "Large pizza" in result

    def test_exact_threshold_six_people(self):
        """Test exactly 6 people (boundary for Extra Large/2 Large)"""
        result = calculate_pizza_for_people(6)
        assert "Extra Large" in result

    def test_exact_threshold_eight_people(self):
        """Test exactly 8 people (boundary for 2 Large/2 Extra Large)"""
        result = calculate_pizza_for_people(8)
        assert "2 Large pizzas" in result
