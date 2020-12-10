def numb_input():
    input1 = input("give me a number ")
    input2 = input("give me another number ")
    return int(input1), int(input2)

def addup():
    num1, num2 = numb_input()
    sum = num1 + num2
    print(sum)

def main():
    addup()

if __name__ == "__main__":
    main()