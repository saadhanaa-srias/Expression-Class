class Expression:
  def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

  def sum(self):
        print(self.num1+self.num2+self.num3)

total= Expression(2,6,19)

total.sum()