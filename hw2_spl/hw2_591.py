import math
from scipy import integrate     # built-in integration package for Method 2

# class integration_method1_1():
#     def __init__(self, x = 4): #i put in a default so that, missing the command, wont cause a bug
#         self.expected = -4.0 #correction upto 1
#         self.upper = 1.0 #again correction upto 1
#         self.steps = 10_000_000 # number of steps 
#         self.lower = 1.0e-7 
#         self.x = x #thought to keep the name simple



#     def func(self, x): #the main function itself
#         return (math.log(x)) / (math.sqrt(x))


#     def trape(self):
#         height = (self.upper - self.lower) / self.steps
#         total = 0.5 * (self.func(self.lower) + self.func(self.upper))

#         for i in range(1, int(self.steps)):
#             total += self.func(self.lower + i * height)
#            # print(i)
#         return total * height

#     def result_reporter(self):
#         i3_method = self.trape()
#         diff = abs(i3_method - self.expected)
#         print(f"{i3_method:<15f}#  I3 Method 1")
#         print(f"{diff:<15f}#  Difference Method 1")


class integration_method1_2():
    def __init__(self, x = 4): #i put in a default so that, missing the command, wont cause a bug
        self.expected = -4.000 #correction upto 3
        self.upper = 1.000 #again correction upto 3
        self.steps = (19*6*2003) # number of steps 
        self.lower = 0.1 / self.steps
        self.x = x #thought to keep the name simple



    def func(self, x): #the main function itself
        return (math.log(x)) / (math.sqrt(x))


    def trape(self):
        height = (self.upper - self.lower) / self.steps
        total = 0.5 * (self.func(self.lower) + self.func(self.upper))

        for i in range(1, int(self.steps)):
            total += self.func(self.lower + i * height)
           # print(i)
        return total * height

    def result_reporter(self):
        i3_method = self.trape()
        diff = abs(i3_method - self.expected)
        print(f"{i3_method:<15f}#  I3 Method 1")
        print(f"{diff:<15f}#  Difference Method 1")



class integration_method2():
    def __init__(self, x = 4): #same default trick as above, a missing argument wont cause a bug
        self.expected = -4.000 #correction upto 3
        self.upper = 1.000 #again correction upto 3
        self.lower = 0.0 #quad handles the singularity itself, no need to nudge it off zero
        self.x = x #thought to keep the name simple



    def func(self, x): #the main function itself
        return (math.log(x)) / (math.sqrt(x))


    def quadrature(self):
        value, error = integrate.quad(self.func, self.lower, self.upper)
        return value

    def result_reporter(self):
        i3_method = self.quadrature()
        diff = abs(i3_method - self.expected)
        print(f"{i3_method:<20.8f}#  I3 Method 2")
        print(f"{diff:<20.16f}#  Difference Method 2")


# print("old method")
# integral1 = integration_method1_1()
# integral1.result_reporter()


print("\n"*2)
integral = integration_method1_2(4)
integral.result_reporter()
integral2 = integration_method2(4)
integral2.result_reporter()
