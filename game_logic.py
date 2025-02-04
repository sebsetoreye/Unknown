import random

# Function to generate a random target number and available numbers
def generate_target():
    target = random.randint(10, 100)
    available_numbers = [random.randint(1, 10) for _ in range(4)]
    return target, available_numbers


def check_solution(user_input, target):
    """
    Function to check if the user input matches the target.
    Example: user_input should be an integer, and the target is an integer as well.
    """
    try:
        # Check if the user input is a valid integer and compare it with the target
        user_input = int(user_input)
        if user_input == target:
            return True
        return False
    except ValueError:
        return False  # Return False if the input is not a valid integer
