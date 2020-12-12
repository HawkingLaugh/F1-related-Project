def numb_input():
    input1 = input("give me a number ")
    input2 = input("give me another number ")
    input3 = input("third number please ")
    return int(input1), int(input2), int(input3)

def addup():
    num1, num2, num3 = numb_input()
    sum = num1 + num2 + num3
    print(sum)

def main():
    addup()
    print("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut suscipit purus finibus, rhoncus arcu sed, efficitur eros. Vestibulum scelerisque")

if __name__ == "__main__":
    main()