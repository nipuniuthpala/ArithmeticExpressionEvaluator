class Evaluator:
    """Recursive descent parser used to evaluate arithmetic expressions.
    Supported features:
    - Signed integers
    - Operators: +, -, *, /
    - Nested parentheses
    - Whitespace between tokens

    Expressions are evaluated strictly left-to-right as required by the exercise specification."""

    def __init__(self, expression):
        """Store the input expression and initialise the current parsing position."""
        self.expression = expression
        self.pos = 0

    def _return_current(self):
        """Return the current character without consuming it.Whitespace is skipped automatically so the parser only sees meaningful tokens."""
        self._skip_whitespace()

        if self.pos < len(self.expression):
            return self.expression[self.pos]

        return None

    def _use_current(self):
        """Consume and return the current character, advancing the parser position by one."""
        char = self._return_current()

        if char is not None:
            self.pos += 1

        return char

    def _skip_whitespace(self):
        """Move past any whitespace characters in the expression."""
        while (
            self.pos < len(self.expression)
            and self.expression[self.pos].isspace()
        ):
            self.pos += 1

    def parse_number(self):
        """Parse a signed integer.Returns:Integer value on success.None if a valid number cannot be parsed."""
        sign = 1

        char = self._return_current()

        # Handle optional sign
        if char in ('+', '-'):
            if self._use_current() == '-':
                sign = -1

        # A number must contain at least one digit
        char = self._return_current()

        if char is None or not char.isdigit():
            return None

        num_str = ""

        # Read all consecutive digits
        while self._return_current() is not None and self._return_current().isdigit():
            num_str += self._use_current()

        return int(num_str) * sign

    def parse_operand(self):
        """Parse a single operand.An operand can be:A signed integer or A parenthesised expression and Returns-Integer result on success.None on parsing error."""
        char = self._return_current()

        if char == '(':
            # Consume opening parenthesis
            self._use_current()

            # Recursively evaluate inner expression
            result = self.parse_expression()

            # Ensure matching closing parenthesis exists
            if self._use_current() != ')':
                return None

            return result

        return self.parse_number()

    def parse_expression(self):
        """Parse and evaluate an expression.Evaluation is performed strictly left-to-right.Returns Integer result on success.None on error."""
        # Parse first operand
        result = self.parse_operand()

        if result is None:
            return None

        # Continue processing operators until the expression ends or a closing parenthesis is reached
        while True:

            op = self._return_current()

            if op not in ('+', '-', '*', '/'):
                break

            # Consume operator
            self._use_current()

            # Parse right-hand operand
            right = self.parse_operand()

            if right is None:
                return None


            # left-to-right evaluation requirements
            if op == '+':
                result += right

            elif op == '-':
                result -= right

            elif op == '*':
                result *= right

            elif op == '/':
                # Prevent division by zero
                if right == 0:
                    return None

                # Truncate towards zero
                result = int(result / right)

        return result


def evaluate(expression):
    """Public entry point required by the exercise.Returns-Integer result if evaluation succeeds.None if the expression contains errors."""

    # Reject empty expressions
    if not expression or not expression.strip():
        return None

    parser = Evaluator(expression)

    result = parser.parse_expression()

    if parser._return_current() is not None:
        return None

    return result