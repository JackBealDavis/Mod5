class Calculator:
    def __init__(self, a ,b):
        self.a = a
        self.b = b

        self.jack = 2.45
    
    def get_sum(self):
        return self.a + self.b
    
    def get_minus(self):
        return self.a - self.b

if __name__ == "__main__":
   myCalc = Calculator(a=5,b=6)
   print(myCalc.get_sum())
   print(myCalc.get_minus())

