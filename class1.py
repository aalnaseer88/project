class EuclideanAlgorithm:
    def __init__(self, x, y):
        self.x = x  # Initialize the first number
        self.y = y  # Initialize the second number

    def compute_gcd(self):
        x, y = self.x, self.y  # Assign initial values
        while y != 0:  # Loop until b becomes 0
            x, y = y, x % y  # Update a and b using the Euclidean Algorithm
        return x #return the GCD
