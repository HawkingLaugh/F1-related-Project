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
    print("ソフトウェア開発の定番ツールとなったGitHubは今や世界中の企業で採用されており、チームでプロジェクトを進めるさいには欠かせないものとなりました。")

if __name__ == "__main__":
    main()