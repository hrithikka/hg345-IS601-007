import pytest
from PumpkinMachine import PumpkinMachine
from PumpkinMachine import STAGE
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
# this is an example test showing how to cascade fixtures to build up state
@pytest.fixture
def machine():
    pm = PumpkinMachine()
    return pm
# sample fixture, can delete if not using

@pytest.fixture
def first_order(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("done")
    machine.handle_pay(10000, "10000")
    return machine

# sample fixture, can delete if not using

@pytest.fixture
def second_order(first_order):
    first_order.handle_pumpkin_choice("Large Pumpkin")
    first_order.handle_face_stencil_choice("Spooky Face")
    first_order.handle_face_stencil_choice("Toothy Face")
    first_order.handle_face_stencil_choice("next")
    first_order.handle_extra_choice("LED Candle")
    first_order.handle_extra_choice("Dry Ice")
    first_order.handle_extra_choice("done")
    # machine.handle_pay(10000,"10000")
    return first_order
# sample test case, can delete if not using
def test_production_line(second_order):
    for j in second_order.pumpkins:
        print(second_order.inprogress_pumpkin)
        if j.name.lower() == second_order.inprogress_pumpkin[0].name.lower():
            print(f"Pumkin {j.name.lower()} matches in progress \
                {second_order.inprogress_pumpkin[0].name.lower()}")
            assert True
            return

    assert False

# add required test cases below

#UCID:hg345 DATE:10/23/2023
#Test 1 - pumpkin must be the first selection (can't add face stencils or extrass without a pumpkin choice)
#This test case checks if the machine is selecting the Pumpkin first and it throws an AssertionError 
# when currently_selecting attribute is not in Pumpkin stage.
def test_first_selection(machine):
    assert machine.currently_selecting.name == STAGE.Pumpkin.name

#UCID:hg345 DATE:10/23/2023
#Test 2 - can only add face stencils if they're in stock
# This test case checks if there are face stencils in stock.
# The initial no of face stencils is set to 1 and when 2 
# face stencils are selected, it throws OutOfStockException. 
def test_face_stencils_in_stock(machine):
    machine.handle_pumpkin_choice("Small Pumpkin")  
    machine.face_stencils[0].quantity = 1 
    
    try:
        machine.handle_face_stencil_choice("Spooky Face")
        assert machine.face_stencils[0].quantity <= 1
    except OutOfStockException:
        assert False

#UCID:hg345 DATE:10/23/2023
# Test 3 - can only add extras if they're in stock
# This test case checks if there are extras in stock.
# The initial no of extras is set to 1 and when 2 face stencils are selected, it throws OutOfStockException.
def test_extras_in_stock(machine):
    machine.extras[0].quantity = 1
    machine.handle_pumpkin_choice("Medium Pumpkin")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Glitter") 
    try:
        machine.handle_extra_choice("Glitter")
        assert machine.extras[0].quantity == 1
    except OutOfStockException:
        assert False

# UCID:hg345 DATE:10/23/2023
# Test 4 - Can add up to 3 face stencils of any combination
# This test case is used so the face stencils are given a max value of 3.
# Thus the for loop only takes MAX_STENCILS-1 = 2 values and if the value > 2 and
# if we try to order another stencil it will throw ExceededRemainingChoicesException.
def test_max_face_stencils(machine):
    machine.face_stencils[0].quantity=3
    machine.handle_pumpkin_choice("Large Pumpkin")
    for stencils in range(machine.MAX_STENCILS - 1):
        machine.handle_face_stencil_choice("Happy Face")
    try:
        machine.handle_face_stencil_choice("Happy Face")
        assert machine.remaining_stencils == 0
    except ExceededRemainingChoicesException:
        assert False

# UCID:hg345 DATE:10/23/2023
# Test 5 - Can add up to 3 extras of any combination
#This test case is used so the EXTRAS are given a max value of 3.
def test_max_extras(machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("next")
    for scoop in range(machine.MAX_EXTRAS - 1):
        machine.handle_extra_choice("Paint Kit")
    try:
        machine.handle_extra_choice("Paint Kit")
        assert machine.remaining_extras == 0
    except ExceededRemainingChoicesException:
        assert False
#UCID:hg345 DATE:10/23/2023
# Test 6 - cost must be calculated properly based on the choices (check for currency format as part of this)
#  (test case should have a few permutations of at least 3 valid pumpkins [hint parameterized tests])
# Machine is INITIALLY reset using reset().
# This test case is used to calculate the total cost. all the steps which include choosing pumpkin,
#  stencils and extras are covered. And calculated accordingly

def test_total_cost(machine):
    machine.reset()
    machine.handle_pumpkin_choice("Large Pumpkin")
    machine.handle_face_stencil_choice("Spooky Face")
    machine.handle_face_stencil_choice("Toothy Face")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Spooky Sound Effects")
    machine.handle_extra_choice("done")
    assert machine.calculate_cost() == 7.25

#UCID:hg345 DATE:10/23/2023
# Test 7 - Total Sales (sum of costs) must be calculated properly (test case should have a few 
# permutations of at least 3 valid pumpkins [hint parameterized tests])
# Multiple orders calculations are checked, this test case goes through all the
#  steps which include choosing pumpkin, stencils and extras.then calculates the cost using calculate_cost function. handle_pay is used for pay.
#Here two or more orders are used 
def test_total_sales(machine):
# First order
    machine.handle_pumpkin_choice("Small Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("Spooky Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Glitter")
    machine.handle_extra_choice("Dry Ice")
    first_pumpkin_cost = float(machine.calculate_cost())
    machine.currently_selecting = STAGE.Pay
    machine.handle_pay(first_pumpkin_cost, str(first_pumpkin_cost))
# Second order
    machine.handle_pumpkin_choice("Medium Pumpkin")
    machine.handle_face_stencil_choice("Toothy Face")
    machine.handle_face_stencil_choice("Scream Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Sticker Pack")
    machine.handle_extra_choice("done")
    second_pumpkin_cost = float(machine.calculate_cost())
    machine.handle_pay(second_pumpkin_cost, str(second_pumpkin_cost))
    expected_total_sales = first_pumpkin_cost + second_pumpkin_cost
    assert machine.total_sales == expected_total_sales

#UCID: hg345 DATE:10/23/2023
# Test 8 - Total products variable should properly increment for each purchase
#this test case no.of products delivered by the Pumpkin machine is checked after each order's payment is completed
# It ensuring that it accurately counts the number of orders processed by the Pumpkin Machine.
def test_total_pumpkin(machine):
    machine.reset()
#First order
    machine.handle_pumpkin_choice("Large Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("Spooky Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("Spooky Sound Effects")
    machine.handle_extra_choice("Dry Ice")
    first_pumpkin_cost = float(machine.calculate_cost())
    machine.currently_selecting = STAGE.Pay
    machine.handle_pay(first_pumpkin_cost, str(first_pumpkin_cost))
    assert machine.total_products == 1
    machine.reset()
#Second order
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Spooky Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    second_pumpkin_cost = float(machine.calculate_cost())
    machine.currently_selecting = STAGE.Pay
    machine.handle_pay(second_pumpkin_cost, str(second_pumpkin_cost))
    assert machine.total_products == 2