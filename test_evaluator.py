from evaluator import evaluate


class TestEvaluator:

    def test_valid_expressions(self):
        assert evaluate("1 + 3") == 4
        assert evaluate("(1 + 3) * 2") == 8
        assert evaluate("(4 / 2) + 6") == 8
        assert evaluate("4 + (12 / (1 * 2))") == 10
        assert evaluate("1 + 3 * 4") == 16
        assert evaluate("-5 + 2") == -3

    def test_invalid_expressions(self):
        assert evaluate("(1 + (12 * 2)") is None
        assert evaluate("1 + * 4") is None
        assert evaluate("10 / 0") is None
        assert evaluate("abc") is None
        assert evaluate("") is None