# Arithmetic Expression Evaluator

## Overview

This project implements a simple arithmetic expression evaluator in Python without using any external libraries or built-in evaluation functions such as `eval()`.

The evaluator supports:

- Signed decimal integers
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Nested parentheses (`(` and `)`)
- Whitespace between tokens

Expressions are evaluated **strictly left-to-right**, as required by the specification.

Execute using -$ pytest test_evaluator.py 