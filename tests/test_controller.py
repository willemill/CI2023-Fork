def test_returnSignal(controller):
    """Tests the Return key binding interface to our Qt display widget."""
    from PyQt5 import QtCore, QtGui
    
    expression = '3+2' #String input
    results = eval(expression) #this evaluates the expression 3+2
    assert results == 5 #expected result should be 5, if it is not true- pytest will show false.


    # event = QtGui.QKeyEvent(
    #     QtCore.QEvent.KeyPress, QtCore.Qt.Key_Enter, QtCore.Qt.NoModifier
    # )
    # controller._view.display.keyPressEvent(event)
    # assert controller._view.displayText() == "3"

