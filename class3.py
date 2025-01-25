class ExtendedEuclideanAlgorithm(EuclideanAlgorithm):
    def is_coprime(self):
        return self.compute_gcd() == 1 # Check if GCD is 1, meaning numbers are coprime

    def display_results(self):
        gcd_result = self.compute_gcd() # Calculate GCD
        coprime_status = "are" if self.is_coprime() else "are not" # Determine coprime status
        print(f"GCD of {self.x} and {self.y} is {gcd_result}")  # Display GCD
        print(f"{self.x} and {self.y} {coprime_status} coprime.") # Display coprime status
if __name__ == "__main__":
    EuclideanAlgorithmInput.run()