class Vector:
    def __init__(self, *n):
        self.n = n

    def __add__(self, other):
        return Vector(*[i + j for i, j in zip(self.n, other.n)])

    def __sub__(self, other):
        return Vector(*[i - j for i, j in zip(self.n, other.n)])

    def __mul__(self, other):
        return sum(i * j for i, j in zip(self.n, other.n))

    def scalar_mul(self, scalar):
        return Vector(*[i * scalar for i in self.n])

    def magnitude(self):
        return (sum(i ** 2 for i in self.n)) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*[i / mag for i in self.n])

    def __str__(self):
        return f"Vector{self.n}"

# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

option = int(input("""Choose an operation:
1 for addition
2 for subtraction
3 for dot product
4 for scalar multiplication
5 for magnitude
6 for normalization
7 for exit                   
                   
Enter your choice: """))
while option!=7:       
    if option == 1:
        print(v1 + v2)
    elif option == 2:
        print(v1 - v2)
    elif option == 3:
        print(v1 * v2)
    elif option == 4:
        scalar = int(input("Enter the scalar value: "))
        print(v1.scalar_mul(scalar))
    elif option == 5:
        print(v1.magnitude())
    elif option == 6:
        print(v1.normalize())
    else:
        print("Invalid input")
