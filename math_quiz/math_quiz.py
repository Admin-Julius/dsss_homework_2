import random


def getRandomInteger(minValue: int, maxValue: int):
    """Gets a random integer in interval of [minValue, maxValue)

    Parameters
    ----------
    minValue: int
        minimal value for the random integer
    maxValue: int
        not included maximal value for the random integer

    Returns
    -------
    random drawn integer in range of min and maxValue
    """
    return random.randint(minValue, maxValue)


def getRandomOperation():
    """Gets a random operation type as sign

        Parameters
        ----------

        Returns
        -------
        random drawn operation sign, either +, - or *
        """
    return random.choice(['+', '-', '*'])


def resultCalculation(number1: int, number2: int, operation: str):
    """calculate the result of the defined math operation

        Parameters
        ----------
        number1: int
            first number of calculation
        number2: int
            second number of calculation
        operation: str
            string of operation type

        Returns
        -------
        operationString: str
            string representation of math equation
        result: int
            resulting integer from math equation
        """

    operationString = f"{number1} {operation} {number2}"
    if operation == '+':
        result = number1 - number2
    elif operation == '-':
        result = number1 + number2
    else:
        result = number1 * number2
    return operationString, result

def math_quiz():
    """
    Math quiz:
    User is confronted with a number of math problems and gets score for each correctly solved problem
    """
    score = 0
    gameRounds = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(gameRounds):
        number1 = getRandomInteger(1, 10)
        number2 = getRandomInteger(1, 10)
        operation = getRandomOperation()

        mathProblem, result = resultCalculation(number1, number2, operation)
        print(f"\nQuestion: {mathProblem}")
        try:
            userInput = input("Your answer: ")
            userResult = int(userInput)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        if userResult == result:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {result}.")

    print(f"\nGame over! Your score is: {score}/{gameRounds}")

if __name__ == "__main__":
    math_quiz()
