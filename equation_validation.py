'''
Equation Validation
Given a string representing a math equation, determine whether it is correct.

The left side may contain up to three positive integers and the operators +, -, *, and /.
The equation will be given in the format: "number operator number = number" (with two or three numbers on the left). For example: "2 + 2 = 4" or "2 + 3 - 1 = 4".
The right side will always be a single integer.
Follow standard order of operations: multiplication and division are evaluated before addition and subtraction, from left-to-right.

'''

def is_valid_equation(equation):
    left_side, right_side = equation.split('=')
    right_value = int(right_side.strip())
    
    # Evaluate the left side using standard order of operations
    def evaluate_expression(expr):
        tokens = expr.split()
        # First handle multiplication and division
        i = 0
        while i < len(tokens):
            if tokens[i] in ('*', '/'):
                operator = tokens[i]
                left_operand = int(tokens[i - 1])
                right_operand = int(tokens[i + 1])
                if operator == '*':
                    result = left_operand * right_operand
                else:
                    result = left_operand // right_operand  # Use integer division
                tokens[i - 1] = str(result)
                del tokens[i:i + 2]  # Remove the operator and the right operand
            else:
                i += 1
        
        # Now handle addition and subtraction
        result = int(tokens[0])
        i = 1
        while i < len(tokens):
            operator = tokens[i]
            operand = int(tokens[i + 1])
            if operator == '+':
                result += operand
            else:
                result -= operand
            i += 2
        
        return result
    
    return evaluate_expression(left_side.strip()) == right_value