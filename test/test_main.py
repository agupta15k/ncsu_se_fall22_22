# Test file for unit testing main.py functions

# Local import
from code import main
from io import StringIO
from code.operations import Operations


def test_main(monkeypatch, capsys):
    def mockGetInputOperation():
        return 'addition'
    def mockGetInputValuesForOperation(operation, lastResult):
        return (1, 2)
    def mockPerformComputation(operation, num1, num2):
        return 3.0
    monkeypatch.setattr('code.main.getInputOperation', mockGetInputOperation)
    monkeypatch.setattr('code.main.getInputValuesForOperation', mockGetInputValuesForOperation)
    monkeypatch.setattr('code.main.performComputation', mockPerformComputation)
    monkeypatch.setattr('sys.stdin', StringIO('n\n'))
    main.main()
    out, err = capsys.readouterr()
    assert '3.0' in out
    assert err == ''

def test_getInputOperationAddition(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('addition\n'))
    result = main.getInputOperation()
    assert result == 'addition'

def test_getInputOperationSubtraction(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('subtraction\n'))
    result = main.getInputOperation()
    assert result == 'subtraction'

def test_getInputOperationMultiplication(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('multiplication\n'))
    result = main.getInputOperation()
    assert result == 'multiplication'

def test_getInputOperationDivision(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('division\n'))
    result = main.getInputOperation()
    assert result == 'division'

def test_getInputOperationAddition(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('test\n'))
    result = main.getInputOperation()
    assert result == None

def test_getInputValuesForOperationNoLastResult(monkeypatch):
    def mockGetNumber(operation, lastResult):
        return 3.7
    monkeypatch.setattr('code.main.getNumber', mockGetNumber)
    result = main.getInputValuesForOperation('addition')
    assert result == (3.7, 3.7)

def test_getInputValuesForOperationNoLastResult(monkeypatch):
    def mockGetNumber(operation, lastResult):
        return 3.7
    monkeypatch.setattr('code.main.getNumber', mockGetNumber)
    result = main.getInputValuesForOperation('addition', 4.2)
    assert result == (4.2, 3.7)

def test_getNumberValidInputInt(monkeypatch):
    def mockValidateNum(operation, numId, num):
        return True
    monkeypatch.setattr('sys.stdin', StringIO('1\n'))
    monkeypatch.setattr('code.main.validateNum', mockValidateNum)
    result = main.getNumber('addition', 'first')
    assert result == 1.0

def test_getNumberValidInputFloat(monkeypatch):
    def mockValidateNum(operation, numId, num):
        return True
    monkeypatch.setattr('sys.stdin', StringIO('1.5\n'))
    monkeypatch.setattr('code.main.validateNum', mockValidateNum)
    result = main.getNumber('addition', 'first')
    assert result == 1.5

def test_validateNumSuccess():
    result = main.validateNum('addition', 'first', '2')
    assert result == True

def test_validateNumFailNoDivision():
    result = main.validateNum('addition', 'first', 'a')
    assert result == False

def test_validateNumFailureDivisionByZero():
    result = main.validateNum('division', 'second', '0')
    assert result == False

def test_performComputationAddition(monkeypatch):
    def mockOperationsAddition():
        return 3
    monkeypatch.setattr(Operations(1, 2), 'addition', mockOperationsAddition)
    result = main.performComputation('addition', 1, 2)
    assert result == 3.0

def test_performComputationSubtraction(monkeypatch):
    def mockOperationsSubtraction():
        return 3
    monkeypatch.setattr(Operations(3, 1), 'subtraction', mockOperationsSubtraction)
    result = main.performComputation('subtraction', 3, 1)
    assert result == 2.0

def test_performComputationMultiplication(monkeypatch):
    def mockOperationsMultiplication():
        return 3
    monkeypatch.setattr(Operations(1, 2), 'multiplication', mockOperationsMultiplication)
    result = main.performComputation('multiplication', 1, 2)
    assert result == 2.0

def test_performComputationDivision(monkeypatch):
    def mockOperationsDivision():
        return 3
    monkeypatch.setattr(Operations(1, 2), 'division', mockOperationsDivision)
    result = main.performComputation('division', 1, 2)
    assert result == 0.5
