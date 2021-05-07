#function that takes a 2 integers and finds factorial (but prevents 0)
def safeMultiplication(low, high):
    if low > high:
        print("Invalid input")
        return 0
    elif low < 0 and high > 0:
        print("Invalid input")
        return 0
    elif low > 0 and high < 0:
        print("Invalid input")
        return 0
    elif low < high:
        sum = 1
        for i in range(low, high+1):
            sum = sum * i
        return sum
            

#Input for program

low = int(input(""))
high = int(input(""))
print(safeMultiplication(low,high))