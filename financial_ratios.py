
"""
OpenFinance India
Basic Financial Ratio Calculator

Educational financial calculations.
"""


def calculate_net_profit_margin(net_profit, revenue):
    if revenue <= 0:
        raise ValueError("Revenue must be greater than zero.")

    return (net_profit / revenue) * 100


def calculate_roe(net_profit, average_equity):
    if average_equity <= 0:
        raise ValueError("Average equity must be greater than zero.")

    return (net_profit / average_equity) * 100


def calculate_debt_to_equity(total_debt, shareholders_equity):
    if shareholders_equity <= 0:
        raise ValueError("Shareholders' equity must be greater than zero.")

    return total_debt / shareholders_equity


def calculate_current_ratio(current_assets, current_liabilities):
    if current_liabilities <= 0:
        raise ValueError("Current liabilities must be greater than zero.")

    return current_assets / current_liabilities


def calculate_gross_profit_margin(revenue, cost_of_goods_sold):
    """Calculate gross profit margin as a percentage."""
    if revenue <= 0:
        raise ValueError("Revenue must be greater than zero.")

    return ((revenue - cost_of_goods_sold) / revenue) * 100


def calculate_ebitda_margin(ebitda, revenue):
    """Calculate EBITDA margin as a percentage."""
    if revenue <= 0:
        raise ValueError("Revenue must be greater than zero.")

    return (ebitda / revenue) * 100


def calculate_roce(ebit, capital_employed):
    """Calculate return on capital employed as a percentage."""
    if capital_employed <= 0:
        raise ValueError("Capital employed must be greater than zero.")

    return (ebit / capital_employed) * 100


def calculate_interest_coverage(ebit, interest_expense):
    """Calculate the interest coverage ratio."""
    if interest_expense <= 0:
        raise ValueError("Interest expense must be greater than zero.")

    return ebit / interest_expense


def calculate_free_cash_flow(operating_cash_flow, capital_expenditure):
    """Calculate free cash flow. CapEx is entered as a positive outflow."""
    if operating_cash_flow < 0:
        raise ValueError("Operating cash flow cannot be negative.")

    if capital_expenditure < 0:
        raise ValueError("Capital expenditure must be non-negative.")

    return operating_cash_flow - capital_expenditure

