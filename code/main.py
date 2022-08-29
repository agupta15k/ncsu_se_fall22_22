# Main file

# Local imports
from operations import Operations


def performComputation(operation:str, num1:float, num2:float) -> float:
    """
    Perform the operation on the input numbers
    @operation: Operation to be performed. Like addition, subtraction, etc.
    @num1: First number for operation
    @num2: Second number for operation
    """
    try:
        print('\n\n\tGreat choices, let\'s perform the ' + operation + ' operation')
        # Call relevant function based on the input operation
        if operation == 'addition':
            result = Operations(num1, num2).addition()
        elif operation == 'subtraction':
            result = Operations(num1, num2).subtraction()
        elif operation == 'multiplication':
            result = Operations(num1, num2).multiplication()
        elif operation == 'division':
            result = Operations(num1, num2).division()
        print('\n\n\tThe result of the ' + operation + ' operation on (' + str(num1) + ', ' + str(num2) + ') is ' + str(result))
        return result
    except:
        print('\n\n\tSomething went wrong while performing the operation on the inputs, please try again.')
        exit()

def validateNum(operation:str, numId:str, num:str) -> bool:
    """
    Validate the input number
    @operation: Operation to be performed. Like addition, subtraction, etc.
    @numId: The id to verify if the input is first or second number. Required for input validation for division
    @num: Input number to check validity
    """
    try:
        convertedNum = float(num)
        if operation == 'division' and numId == 'second' and convertedNum == 0:
            print('\n\n\tDivision by 0 is invalid. Please enter a non-zero divisor')
            return False
        return True
    except:
        print('\n\n\tInvalid input! The input has to be a number, please try again')
        return False

def getNumber(operation:str, numId:str) -> float:
    """
    Get input number from user
    @operation: Operation to be performed. Like addition, subtraction, etc.
    @numId: The id to verify if the input is first or second number. Required for input validation for division
    """
    try:
        isValidNum = False
        while isValidNum != True:
            num = input('\n\n\tEnter the ' + numId + ' number for ' + operation + ' operation: ')
            isValidNum = validateNum(operation, numId, num)
        return float(num)
    except:
        print('Something went wrong processing the input number, please try again.')
        exit()

def getInputValuesForOperation(operation:str, lastResult = None) -> tuple:
    """
    Initiate the user input to capture two input numbers for computation
    @operation: Operation to be performed. Like addition, subtraction, etc.
    @lastResult: Result of last computation to re-use. Default value is None
    """
    try:
        num1 = lastResult
        if num1 == None:
            num1 = getNumber(operation, 'first')
        num2 = getNumber(operation, 'second')
        return (num1, num2)
    except:
        print('\n\n\tSomething went wrong while getting input values to perform the operation, please try again.')
        exit()

def getInputOperation() -> str:
    """
    Get operation name from user
    """
    try:
        print('\n\n\tWhich operation would you like to run? \n\n\t\t1. Addition\n\n\t\t2. Subtraction\n\n\t\t3. Multiplication\n\n\t\t4. Division') 
        userOption = input('\n\n\tEnter the operation name or the number corresponding to the operation. For eg: Enter addition or 1 for addition operation: ')
        operation = None
        # Match input with the available operations. Covers multiple input variations
        if userOption == '1' or userOption.lower() == 'addition' or userOption.lower() == 'add':
            print('\n\n\tCool. Let\'s get those numbers added!')
            operation = 'addition'
        elif userOption == '2' or userOption.lower() == 'subtraction' or userOption.lower() == 'subtract':
            print('\n\n\tSubtraction it is!')
            operation = 'subtraction'
        elif userOption == '3' or userOption.lower() == 'multiplication' or userOption.lower() == 'multiply':
            print('\n\n\tMultiplication, nice!')
            operation = 'multiplication'
        elif userOption == '4' or userOption.lower() == 'division' or userOption.lower() == 'divide':
            print('\n\n\tWoah Division, be careful about those 0s!')
            operation = 'division'
        else:
            print('\n\n\tUh oh! We couldn\'t find the specified operation. We understand that you need this computation, but this calculator only supports Addition, Subtraction, Multiplication, and Division. Please try again and use one of these options while we are working on adding more operations!')
        return operation
    except:
        print('\n\n\tSomething went wrong while reading the input operation, please try again.')
        exit()

def main():
    """
    Main function to trigger the input capture, validation, and computation
    """
    try:
        print('\n\n\tHello user, welcome to this basic version of a calculator.')
        print('\n\n\tCurrently we support addition, subtraction, multiplication, and division. More operations are on the way.')
        furtherComputation = 'y'
        lastResult = None
        # Loop to trigger further computation on last result
        while furtherComputation.lower() == 'y':
            operation = getInputOperation()
            if operation != None:
                (num1, num2) = getInputValuesForOperation(operation, lastResult)
                if num1 != None and num2 != None:
                    lastResult = performComputation(operation, num1, num2)
                    print('\n\n\tCurrently stored result: ' + str(lastResult)) if lastResult != None else 0
                    furtherComputation = input('\n\n\tDo you wish to perform another operation on this result? Enter y for yes and anything else to exit: ')
        print('\n\n\tThank you for using the calculator. We hope you liked it. For feedback, please open issues at https://github.com/agupta15k/ncsu_se_fall22_22/issues\n')
        return
    except:
        print('\n\n\tSomething went wrong in the main function or subfunctions. Please try again.')
        exit()

if __name__ == "__main__":
    main()
