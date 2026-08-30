class Sqrt_check():
    #we import the same validators as its only a few changes, and its tested, and im lazy to whip it out full again :)

    def __init__(self, list_of_numbers):

        #we check, if it consists only of int, and convert all floats to int using map
        self.flag = 0
        self.valid_nums = []

        try:
            self.list_of_numbers = list_of_numbers
            self.list_of_numbers_only_for_code_exit = list(map(int, self.list_of_numbers))
        except ValueError:
            print("Error: input must be a list of numbers, e.g. [4, 12, 18] and text is detected")
            self.flag = 1
            self.main()
            

    def validator(self):
        #as the name suggests, we validate the numbers are non zero and +ve
        self.list_of_numbers.sort()
        for i in self.list_of_numbers[0: ]:
            if isinstance(i, float):
                print(f"Error: Ignoring {i} number is not an integer, number must be an integer. skipping...")
            elif i < 0:
                print(f"Error: Ignoring {i} number is must be non-zero and positive")
            else:
                #print("Valid Numbers: ", i)
                self.valid_nums.append(i)
        return self.valid_nums

    #atp the code either has exited due to text, by which, we can say that, this part cannot run either ways
    #or the list is valid, and the validator has removed all the -ve integers, leaving only the +ve ones
    
    def is_it_a_square(self, a):
        if a < 2:
            return True
        
        low = 0
        high = a

        while low <= high:
            mid_val = (low + high) // 2
            square = mid_val * mid_val

            if square == a:
                return True #finally

            elif square < a:
                low = mid_val + 1
            else:
                high = mid_val - 1
        
        return False #last resort, it isnt a square

    def hot_dog_rollers(self): #unloops the list, like a hot dog roller
        for i in self.valid_nums:
            if self.is_it_a_square(i):
                print(i, "is a perfect square")
            else:
                print(i, "is not a perfect square")

    def main(self):

        if self.flag == 0:
            numbers = self.validator()
            self.hot_dog_rollers()
            return numbers
        else:
            return "Exiting Program"
            

list1 = [4.22, -9, -9, 81]
check = Sqrt_check(list1)
a = check.main()
print(a)