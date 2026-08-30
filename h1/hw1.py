#problem 1
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



















#problem 2
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


















#problem 3
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


















    #AI TRASCRIPTS AND GOOGLE SEARCES:
#     google : lcm calc methods
# answer : https://www.calculatorsoup.com/calculators/math/lcm.php

# ❯ the code is @problem1.py question is question 1 on @EEE419_591_HW1_F26.pdf and when I test it, with set [0, 2, -1],
#   the output is PS C:\Users\supre\OneDrive - Arizona State University\EEE591 - Python\h1> python .\problem1.py
#   Error: Ignoring  0  number is must be non-zero and positive
#   Error: Ignoring  -1  number is must be non-zero and positive
#   None when i run just [0,1], its just showing as None, you can run, and can you let me know, what can be the bug
#   or origin of the bug
#   ⎿  Read problem1.py (29 lines)
#   ⎿  Read EEE419_591_HW1_F26.pdf (450.2KB)

# ● Read(C:\Users\supre\OneDrive - Arizona State University\EEE591 - Python\h1\EEE419_591_HW1_F26.pdf · pages 1-3)
#   ⎿  Error: pdftoppm is not installed. Install poppler-utils (e.g. `brew install poppler` or `apt-get install
#      poppler-utils`) to enable PDF page rendering.

# ● PowerShell(python -c "import pypdf, sys; r=pypdf.PdfReader(r'C:\Users\supre\OneDrive - Arizona State University\EEE591
#             - Python\h1\EEE419_591_HW1_F26.pdf'); print('\n'.join(p.extract_text() for p in r.pages[:3]))")
#   ⎿  EEE 419/591
#      Fall 2026
#      Homework 1
#      Solve the following three problems. Put them all into a single code named hw1.py and submit it
#      to the designated link on Canvas. If you upload a second attempt to Canvas and it renames your
#      file, ignore the renaming.
#      In this HW, only limited AI is allowed. Examples of allowed prompts on this HW:
#       What is a greatest common divisor of two numbers?
#       How do I write an if statement in python? Give me an example
#       How do I check if a number is integer in python?
#       I got this error message. How do I interpret it?
#      Examples of prohibited prompts on this HW:
#       Write me a code that calculates the greatest common divisor of a list of numbers in
#      python
#       I ran this code. [PASTE CODE HERE]. I got this error message. [PASTE THE ERROR
#      MESSAGE HERE]. How do I fix my code?
#      Do not forget to cite your AI chat if you used any. Check the Syllabus document for details.
#      Problem 1: Least Common Multiple
#      Write a code that takes a list of numbers and calculates the Least Common Multiple (LCM) of
#      them all. Do not use any built-in “least common multiple” or “lcm” functions from any Python
#      packages.
#      Your code should expect a list of numbers as an input on the form [x1, x2, x3, ... xN]
#      where xi is the ith number that could be any real number. Your code should print “The LCM is:”
#      followed by the least common multiple of the list passed to it by the user. If one of the numbers
#      is negative or zero, your code should display an error message, ignore that number, and find the
#      LCM of the remaining positive numbers. Keep in mind that a number formatted as float (e.g.,
#      12.0) can still be a valid positive integer.
#      An example of the output of your code is as follows:
#      Input a list of numbers: [-4, 12, 18.0, 0, 24]
#      Error: Ignoring -4, number must be positive
#      Error: Ignoring 0, number must be positive
#      The LCM of the valid integers in this list is: 72
#      Hint: start writing a code that works on a list of 2 numbers.
#      Problem 2: Perfect Square Checker
#      Write a code that takes a list of integers and outputs, for each number, whether it is a perfect
#      square (a whole number that is the square of an integer, such as 1, 4, 9, 16, 25). Do not use any
#      built-in “perfect square” checker or square-root functions from external Python packages (e.g.,
#      math.isqrt, or np.sqrt).
#      Your code should expect a single list of numbers (possibly not integers) as an input and print if
#      each number is a perfect square. If one of the numbers is negative or not an integer, your code
#      should skip that number and let the user know it is invalid. Keep in mind that a number
#      formatted as float (e.g., 16.0) does not mean it is not an integer.
#      Consider the following example:
#      Input a list of numbers: [49.0, 17, -9, 81.4, 36]
#      49 is a perfect square
#      17 is NOT a perfect square
#      -9 is negative. Skipping ...
#      81.4 is NOT an integer. Skipping ...
#      36 is a perfect square
#      Hint: A number 𝑁 is a perfect square if there exists an integer 𝑘 such that 𝑘ଶ =𝑁.
#      Problem 3: Pi Approximation via the Wallis Product
#      Write a code that calculates an approximation of 𝜋 using the Wallis Product formula for a
#      specific accuracy or number of terms. Your code should take a single integer as input
#      representing the number of product terms to compute, and output the resulting approximate value
#      of 𝜋 rounded to 6 decimal places, along with the number of terms used.
#      Do not use the built-in math.pi or np.pi constants or any special mathematical functions from
#      external Python packages.
#      Recall that the Wallis Product for approximating 𝜋 is given by:
#      𝜋=  2 ×ෑ ቆ 4𝑛ଶ
#      4𝑛ଶ −  1ቇ
#      ஶ
#      ௡ୀଵ


#      Since we cannot calculate an infinite product, your code will compute a finite product based on
#      the user's input 𝑁. Your code should output the result formatted as shown in the example below:
#      Input the number of terms: 5000
#      Pi approx = 3.141436 based on 5,000 terms
#      MANDATORY – Do not forget to add your mandatory citations as indicated on page 4 of the
#      syllabus document. If you have not used any AI/references in your document, you still need to
#      declare that as indicated in the syllabus document. This has 20% weight according to the rubric
#      in the syllabus.

# ● PowerShell(python -c "
#             xs=[0,2,-1]
#             for i in xs:
#                 print('loop sees:', i, ' list right now:', xs)
#                 if i<=0: xs.remove(i)
#             print('final:', xs)
#             ")
#   ⎿  loop sees: 0  list right now: [0, 2, -1]
#      loop sees: -1  list right now: [2, -1]
#      final: [2]

# ● First — a heads-up on the ground rules: the HW1 handout explicitly lists "I ran this code. [PASTE CODE HERE]... How do
#   I fix my code?" as a prohibited AI prompt (page 1). So I'll stay on the allowed side of that line: I'll explain the
#   two Python concepts that are biting you and show them on a throwaway example, but I won't rewrite problem1.py for you.
#   And whatever you do use, cite it — the citation is 20% of the rubric.

#   Concept 1: removing from a list while you're looping over it

#   for i in some_list: doesn't iterate over the values you saw at the start — it walks an internal index 0, 1, 2, …
#   against the list as it currently is. If you delete an element, everything after it shifts left by one, but the index
#   still moves forward. Result: elements get silently skipped.

#   Here's the effect on your exact input, with no class involved:

#   loop sees: 0    list right now: [0, 2, -1]
#   loop sees: -1   list right now: [2, -1]
#   final: [2]

#   The loop ran twice, not three times. After 0 was removed, index 1 no longer pointed at 2 — 2 had slid into slot 0 — so
#   index 1 landed on -1. 2 was never visited by the loop at all.

#   That's why your else branch never ran, which leads to:

#   Concept 2: a function that falls off the end returns None

#   In Python, if execution reaches the end of a function without hitting a return, the function hands back None
#   automatically. Your only return lives inside the else: branch. Since the loop never visited a valid number, that else
#   never executed, the loop ended, and validator fell off the bottom → None → main returns it → print(a) shows None.

#   Same story for [0, 1]: 0 is removed at index 0, 1 shifts into slot 0, the loop asks for index 1, there's nothing
#   there, loop ends, None.

#   Two more things worth looking at before you call it done

#   - Even once the skipping is fixed, return sits inside the loop. It fires on the first valid number, so nothing after
#     it gets checked. Think about where that return actually belongs relative to the loop.
#   - list.remove(x) removes the first element equal to x, not "the one I'm looking at." With duplicates like [-4, 12, -4]
#     that distinction matters.

#   The general pattern to read up on: "how do I build a new list of the items I want to keep, instead of deleting from
#   the one I'm iterating?" That's a fair thing to look up, and it sidesteps concept 1 entirely.

#   Also note the spec wants a couple of things your validator doesn't handle yet: 12.0 is a float but a valid positive
#   integer and must be accepted, and the final output line has a required format (The LCM of the valid integers in this
#   list is: 72). Your gcd is still pass — that's the real meat of the problem, and the handout's hint (start with two
#   numbers) is good advice.



# google question : self.list_of_numbers.replace(int(i))
# self.list_of_numbers = list(map(int, self.list_of_numbers))
