import calculator

class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)