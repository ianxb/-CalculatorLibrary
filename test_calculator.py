import calculator


class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_addition1(self):
        assert 6 == calculator.add(5, 1)
