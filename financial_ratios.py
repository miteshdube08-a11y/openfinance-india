
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
