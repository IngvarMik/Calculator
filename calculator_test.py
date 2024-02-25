import pytest
from calculator import Calculator

calculator = Calculator()


def test_sum_positiv_nums():
    calculator = Calculator()
    res = calculator.sum( 4 , 5)
    assert res == 9 # assert это проверь  , что res == 9

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum( -10 , -6)
    assert res == -16

def test_sum_positiv_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum( -6 , 6)
    assert res == 0

def test_sum_float_num():
    calculator = Calculator()
    res = calculator.sum( 5.6 , 4.3)
    res = round( res , 1) # округление - 1 - это до какого знака округлять - питон считает тучу знаков после запятой
    assert res == 9.9

def test_sum_zero_num():
    calculator = Calculator()
    res = calculator.sum( 10 , 0)
    assert res == 10

"""деление"""

def test_div_positive_nums(): # div - деление
    calculator = Calculator()
    res = calculator.div( 10, 2 )
    assert res == 5

def test_div_by_zero_nums():
    calculator = Calculator()

    with pytest.raises(ArithmeticError):
         calculator.div( 10, 0 )
    

"""среднее"""

def test_avg_empty_list(): # avg среднее
    calculator = Calculator()
    numbers = [] # пустой список
    res = calculator.avg( numbers)
    assert res == 0

def test_avg_positive():
    calculator = Calculator()
    numbers = [ 1 , 2,3,4,5,6,7,8,9,5]
    res = calculator.avg( numbers)
    assert res == 5

print("finish")

