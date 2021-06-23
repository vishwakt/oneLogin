import re


class Solution:
    def produceFractionalResult(self, inputFraction: str) -> str:
        # Split operands and operator based on spaces
        operand1, operator, operand2 = inputFraction.split(' ')

        # Check if the operands are valid
        isValid = self.checkForValidOperands(operand1, operand2)

        if not isValid:
            raise ValueError("Invalid operands given")

        num1, den1 = self.getNumeratorAndDenominator(operand1)
        num2, den2 = self.getNumeratorAndDenominator(operand2)
        num3, den3 = '', ''
        if operator == '*':
            [num3, den3] = self.multiplyFraction(num1, den1, num2, den2)
        if operator == '+':
            [num3, den3] = self.addFraction(num1, den1, num2, den2)
        if operator == '-':
            [num3, den3] = self.subtractFraction(num1, den1, num2, den2)
        if operator == '/':
            [num3, den3] = self.divideFraction(num1, den1, num2, den2)

        result = self.getMixedFraction(num3, den3)
        return result

    '''
    Function to check if operands are valid
    '''
    def checkForValidOperands(self, operand1: str, operand2: str) -> bool:
        isValidOperand1 = re.search("^([1-9][0-9]*(?:(?:_[1-9][0-9]*)*\/[1-9][0-9]*)?)$", operand1)
        isValidOperand2 = re.search("^([1-9][0-9]*(?:(?:_[1-9][0-9]*)*\/[1-9][0-9]*)?)$", operand2)
        if isValidOperand1 and isValidOperand2:
            return True
        else:
            return False

    '''
    Function to return numerator an denominator for whole number or fraction or a mixed fraction
    '''
    def getNumeratorAndDenominator(self, operand: str) -> (int, int):
        # Operand is a mixed fraction
        if '_' in operand:
            whole, fraction = operand.split('_')
            numerator, denominator = fraction.split('/')
            numerator = (int(denominator) * int(whole)) + int(numerator)
        # Operand is a fraction
        elif '/' in operand:
            numerator, denominator = operand.split('/')
        # Operand is a whole number
        else:
            numerator = operand
            denominator = 1
        return numerator, denominator

    '''
    Function to calculate Greatest Common Divisor
    '''
    def gcd(self, denom1: int, denom2: int) -> int:
        if denom1 == 0:
            return denom2
        return self.gcd(denom2 % denom1, denom1)

    '''
    Function to sum fractions
    '''
    def addFraction(self, a, b: int, c, d: int) -> (int, int):
        b = int(b)
        d = int(d)
        num3 = (int(a) * int(d)) + (int(b) * int(c))
        den3 = (int(b) * int(d))
        return num3, den3

    '''
    Function to subtract fractions
    '''
    def subtractFraction(self, a, b: int, c, d: int) -> (int, int):
        b = int(b)
        d = int(d)
        num3 = (int(a) * int(d)) - (int(b) * int(c))
        den3 = (int(b) * int(d))
        return num3, den3

    '''
    Function to multiply fractions
    '''
    def multiplyFraction(self, a, b: int, c, d: int) -> (int, int):
        b = int(b)
        d = int(d)
        num3 = (int(a) * int(c))
        den3 = (int(b) * int(d))
        return num3, den3

    '''
    Function to divide fractions
    '''
    def divideFraction(self, a, b: int, c, d: int) -> (int, int):
        b = int(b)
        d = int(d)
        num3 = (int(a) * int(d))
        den3 = (int(b) * int(c))
        return num3, den3

    '''
    Function to get the final mixed fraction
    '''
    def getMixedFraction(self, num3, den3):
        common_factor = self.gcd(num3, den3)
        den3 = int(den3 / common_factor)
        num3 = int(num3 / common_factor)
        if den3 == 1:
            return str(num3)
        elif den3 > 0:
            q, r = divmod(num3, den3)
            if r > 0:
                return str(q) + "_" + str(r) + "/" + str(den3)
            else:
                return str(num3) + "/" + str(den3)


if __name__ == "__main__":
    s = Solution()
    inputString = str(input("Please input the operation in this format: ? (fraction1) (operator) (operand2)"))
    if inputString[0] != "?":
        raise ValueError("Invalid input. Must enter the operation in this format: ? (fraction1) (operator) (operand2)")
    inputFraction = inputString.split("?")[1].strip()
    result = s.produceFractionalResult(inputFraction=inputFraction)
    print('Result: ', result)
