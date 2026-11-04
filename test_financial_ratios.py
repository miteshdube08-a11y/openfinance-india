
import pytest

from financial_ratios import (
    calculate_net_profit_margin,
    calculate_roe,
    calculate_debt_to_equity,
    calculate_current_ratio,
)


def test_net_profit_margin():
    assert calculate_net_profit_margin(200, 1000) == 20


def test_roe():
    assert calculate_roe(150, 750) == 20


def test_debt_to_equity():
    assert calculate_debt_to_equity(500, 1000) == 0.5


def test_current_ratio():
    assert calculate_current_ratio(2000, 1000) == 2


def test_zero_revenue():
    with pytest.raises(ValueError):
        calculate_net_profit_margin(100, 0)


def test_zero_equity():
    with pytest.raises(ValueError):
        calculate_roe(100, 0)


def test_zero_liabilities():
    with pytest.raises(ValueError):
        calculate_current_ratio(2000, 0)


from financial_ratios import (
    calculate_gross_profit_margin,
    calculate_ebitda_margin,
    calculate_roce,
    calculate_interest_coverage,
    calculate_free_cash_flow,
)


def test_gross_profit_margin():
    assert calculate_gross_profit_margin(1000, 600) == 40


def test_ebitda_margin():
    assert calculate_ebitda_margin(200, 1000) == 20


def test_roce():
    assert calculate_roce(150, 750) == 20


def test_interest_coverage():
    assert calculate_interest_coverage(300, 100) == 3


def test_free_cash_flow():
    assert calculate_free_cash_flow(500, 150) == 350


def test_zero_capital_employed():
    with pytest.raises(ValueError):
        calculate_roce(100, 0)


def test_zero_interest_expense():
    with pytest.raises(ValueError):
        calculate_interest_coverage(100, 0)

