import pytest
from MyCalc import MyCalc

class TestMyCalc:

    @pytest.mark.parametrize("num1, num2, expected", [
        (5, 3, 8),
        (-2, 4, 2),
        (10, -5, 5),
        (0, 0, 0),
    ])
    def test_number_add_number(self, num1, num2, expected):
        calculator = MyCalc()
        calculator.add(num1)
        calculator.add(num2)
        assert calculator.ans == expected
#hg345 10/16/2023 Test case used for verifying Addition
    @pytest.mark.parametrize("num1, num2, expected", [
        (5, 3, 2),
        (-2, 4, -6),
        (10, -5, 15),
        (0, 0, 0),
    ])
    def test_number_sub_number(self, num1, num2, expected):
        calculator = MyCalc()
        calculator.ans = num1
        calculator.subtract(num2)
        assert calculator.ans == expected
#hg345 10/16/2023 Test case used for verifying Subtraction
    @pytest.mark.parametrize("num1, num2, expected", [
        (5, 3, 15),
        (-2, 4, -8),
        (10, -5, -50),
        (0, 0, 0),
    ])
    def test_number_mult_number(self, num1, num2, expected):
        calculator = MyCalc()
        calculator.ans = num1
        calculator.multiply(num2)
        assert calculator.ans == expected
#hg345 10/16/2023 Test case used for verifying Multiplication

    @pytest.mark.parametrize("num1, num2, expected", [
        (10, 2, 5),
        (-12, -3, 4),
        (20, 4, 5),
        (4, 2, 2),
    ])
    def test_number_div_number(self, num1, num2, expected):
        calculator = MyCalc()
        calculator.ans = num1
        calculator.divide(num2)
        assert calculator.ans == expected
#hg345 10/16/2023 Test case used for verifying Division
    @pytest.mark.parametrize("num1, num2, expected", [
        (5, 3, 8),
        (-2, 4, 2),
        (10, -5, 5),
        (0, 0, 0),
    ])
    def test_ans_add_number(self, num1, num2, expected):
        calculator = MyCalc()
        calculator.add(num1)
        calculator.add(num2)
        calculator.add(calculator.ans)
        assert calculator.ans == expected + expected
#hg345 10/16/2023 Test case used for verifying ans Addition
    @pytest.mark.parametrize("num1, num2, expected", [
        (5, 3, 2),
        (-2, 4, -6),
        (10, -5, 15),
        (0, 0, 0),
    ])
    def test_ans_sub_number(self, num1, num2, expected):
        calculator = MyCalc()
        calculator.ans = num1
        calculator.subtract(num2)
        calculator.subtract(calculator.ans)
        assert calculator.ans == expected - expected
#hg345 10/16/2023 Test case used for verifying ans Subtraction
    @pytest.mark.parametrize("num1, num2, expected", [
        (5, 3, 15),
        (-2, 4, -8),
        (10, -5, -50),
        (0, 0, 0),
    ])
    def test_ans_mult_number(self, num1, num2, expected):
        calculator = MyCalc()
        calculator.ans = num1
        calculator.multiply(num2)
        calculator.multiply(calculator.ans)
        assert calculator.ans == expected * expected
#hg345 10/16/2023 Test case used for verifying ans Multiplication
    @pytest.mark.parametrize("num1, num2, expected", [
        (10, 2, 5),
        (-12, -3, 4),
        (20, 4, 5),
        (4, 2, 2),
    ])
    def test_ans_div_number(self, num1, num2, expected):
        calculator = MyCalc()
        calculator.ans = num1
        calculator.divide(num2)
        calculator.divide(calculator.ans)
        assert calculator.ans == expected / expected
#hg345 10/16/2023 Test case used for verifying ans Division
    
