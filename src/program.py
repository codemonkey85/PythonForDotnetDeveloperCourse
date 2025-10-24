def main():
    looptest4()

def looptest1():
    while True:
        name = input("What is your name? ")
        if not name:
            break
        print(f"Nice to meet you, {name}.")

def looptest2():
    nums = [1, 5, 8, 10, 7, 2]
    for n in nums:
        print(f"The next number is {n}.")

def looptest3():
    nums = [1, 5, 8, 10, 7, 2]
    for idx, n in enumerate(nums):
        print(f"The {idx} number is {n}.")

def looptest4():
    for n in range(1,6):
        print(f"Line {n}.")

if __name__ == "__main__":
    main()
