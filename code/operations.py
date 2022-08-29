# Operations file

class Operations:
    def __init__(self, num1:float, num2:float) -> None:
        """
        A class for operations
        @num1: First number for operation
        @num2: Second number for operation
        """
        self.num1 = num1
        self.num2 = num2
    
    def addition(self) -> float:
        """
        Perform addition operation
        """
        return self.num1 + self.num2
    
    def subtraction(self) -> float:
        """
        Perform subtraction operation
        """
        return self.num1 - self.num2
    
    def multiplication(self) -> float:
        """
        Perform multiplication operation
        """
        return self.num1 * self.num2
    
    def division(self) -> float:
        """
        Perform division operation
        """
        return self.num1 / self.num2
    