from main import main


def test_calculate_profit():
    expected_profit = -170.42

    assert round(main.calculate_profit(1000, 4, 1000), 2) == expected_profit
