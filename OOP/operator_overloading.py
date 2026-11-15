class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imag + other.imag
        )

    def display(self):
        print(self.real, "+", self.imag, "i")


c1 = Complex(3, 4)
c2 = Complex(2, 5)

c3 = c1 + c2

print("First Complex Number:")
c1.display()

print("Second Complex Number:")
c2.display()

print("Sum of Complex Numbers:")
c3.display()
