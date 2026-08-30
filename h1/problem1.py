class LCM():
    
    def __init__(self, list_of_numbers):

        #we check, if it consists only of int, and convert all floats to int using map
        self.flag = 0
        try:
            self.list_of_numbers = list_of_numbers
            self.valid_nums = []
            self.list_of_numbers = list(map(int, self.list_of_numbers))
        except ValueError:
            print("Error: input must be a list of numbers, e.g. [4, 12, 18]")
            self.flag = 1
            self.main()

    def validator(self):
        #as the name suggests, we validate the numbers are non zero and +ve
        self.list_of_numbers.sort()
        for i in self.list_of_numbers[0: ]:
            if i == 0:
                # self.list_of_numbers.remove(i)
                print(f"Error: Ignoring {i}, number must be non-zero and positive")
            elif i < 0:
                # self.list_of_numbers.remove(i)
                print(f"Error: Ignoring {i}, number must be non-zero and positive")
            else:
                #print("Valid Numbers: ", i)
                self.valid_nums.append(i)
                # a = self.valid_nums
        return self.valid_nums

    #to calc gcd, and then we do a*b//gcd
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a%b
        return a

    def lcm_computer(self, a, b):
        return (a * b) // self.gcd(a, b)

    def lcm_list_compiler(self):
        numbers = self.validator()
        result = numbers[0]
        for val in numbers[1 : ]:
            result = self.lcm_computer(result, val)
        return result

    def main(self):

        if self.flag == 0:
            return self.lcm_list_compiler()
        else:
            return "Exiting Program"


list1 = [2, 3, 0, -9, -9.909090]
lcm = LCM(list1)
a = lcm.main()
print(a)