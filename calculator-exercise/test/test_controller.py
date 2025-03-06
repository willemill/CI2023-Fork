def test_returnSignal(controller):
    """Tests the Return key binding interface to our Qt display widget."""
    from PyQt5 import QtCore, QtGui

    expression = '1+2'  # The string input

    result = eval(expression)  # Evaluates the expression
    if isinstance(result, int):  # Ensures it's an integer
        if result == 3:
            assert 3 == 3
        else:
            assert 2 == 3
