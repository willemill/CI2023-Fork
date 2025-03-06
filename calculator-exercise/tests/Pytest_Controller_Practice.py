# Description: Pytest practice for Controller class

expression = '1+2'  # String input

try:
    result = eval(expression)  # Evaluates the expression
    if isinstance(result, int):  # Evaluates for integer
        controller._view.setDisplayText(str(result))
    else:
        controller._view.setDisplayText("Error")  # Handle non-integer cases
except Exception:
    controller._view.setDisplayText("Invalid Input")  # Handle errors

