class wallis():
    def __init__(self, n_terms_approx):
        self.n_terms = n_terms_approx
        
    def wallis_product(self):
        product = 1
        for n in range(1, self.n_terms + 1):
            #the og wallis product as per question
            product = product * ((4 * n**2) / ((4 * n**2) - 1))
        return product * 2
    
    def validator(self):
        if(self.n_terms) < 0:
            print(f"Error: Number of terms must be a non-negative integer {self.n_terms}")
            return False
        
        elif isinstance(self.n_terms, float): #since its terms, idw to deal with floats
            print(f"Error: Number of terms must be an integer {self.n_terms}")
            return False
        else:
            return True
    
    def main(self):
        if self.validator():
            return self.wallis_product()
        else:
            return "Exiting Program"

#guard rails, for guys like me
try:
    n_term_approx = int(input("Enter a number: "))
    wallis = wallis(n_term_approx)
    a = wallis.main()
    print(a)
except ValueError:
    print("Error: Input must be an integer")
    exit()