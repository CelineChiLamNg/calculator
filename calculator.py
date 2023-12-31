class Calculator:

    # memory attribute set to 0 always. I could pass an argument "memory" if wanted to be able to change it
    def __init__(self):
        self.memory = 0


    def addition(self, number):
        self.memory += number    # altering internal state of calculator
        return self.memory    # return is not needed. However, it facilitates cases in Division and Root

    def subtraction(self, number):
        self.memory -= number
        return self.memory

    def multiplication(self, number):
        self.memory *= number
        return self.memory

    def division(self, number):    # division cannot be done with 0
        if number == 0:
            return "Error: Division by zero"
        else:
            self.memory /= number
            return self.memory

    def root(self, index):
        if index == 0:
            return "Error: Root index cannot be zero"
        else:
            self.memory **= (1/index)
            return self.memory

    def reset(self):
        self.memory = 0
