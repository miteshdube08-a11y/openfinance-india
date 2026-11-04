
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
