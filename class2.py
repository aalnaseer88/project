class EuclideanAlgorithmInput:
    @staticmethod
    def get_input():
        try:
            x = int(input("Enter the first positive integer: ")) #get first input from the user 
            y = int(input("Enter the second positive integer: "))#get second input from the user
            if x <= 0 or y <= 0:
                raise ValueError("Both numbers must be positive integers.") # Validate input
            return x, y #return valid inputs 
        except ValueError as e:
            print(f"Invalid input: {e}") # Display error message for invalid input
            return None

    @staticmethod
    def run():
        inputs = EuclideanAlgorithmInput.get_input() # Get user input
        if inputs:
            x, y = inputs
            gcd_calculator = EuclideanAlgorithm(x, y) # Create an instance of the GCD calculator
            result = gcd_calculator.compute_gcd() #calculate gcd 
            print(f"The GCD of {x} and {y} is {result}") #display result 