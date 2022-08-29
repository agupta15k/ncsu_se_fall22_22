# Operations test file

# Local import
from code.operations import Operations


class TestOperations:
    def test_inputAssignment(self):
        operation = Operations(1, 2)
        assert operation.num1 == 1
        assert operation.num2 == 2

    def test_additionInt(self):
        result = Operations(1, 2).addition()
        assert result == 3
    
    def test_additionFloat(self):
        result = Operations(1.2, 2.5).addition()
        assert result == 3.7
    
    def test_subtractionInt(self):
        result = Operations(4, 2).subtraction()
        assert result == 2
    
    def test_subtractionFloat(self):
        result = Operations(1.2, 2.4).subtraction()
        assert result == -1.2
    
    def test_multiplicationInt(self):
        result = Operations(4, 2).multiplication()
        assert result == 8
    
    def test_multiplicationFloat(self):
        result = Operations(1.2, 2.4).multiplication()
        assert result == 2.88
    
    def test_divisionInt(self):
        result = Operations(4, 2).division()
        assert result == 2
    
    def test_divisionFloat(self):
        result = Operations(1.2, 2.4).division()
        assert result == 0.5
