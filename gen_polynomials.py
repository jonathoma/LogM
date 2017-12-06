def generate(n):
    var('z, c')
    f = z**2 + c
    prev = 0
    table = []
    for i in range(n + 1):
        prev = f(z=prev)
        table.append(prev)
    for i, result in enumerate(table):
        print("n = {0}: {1}".format(i, result.expand()))

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("This is the nth iteration of f_c^n(0): ", generate(n))

