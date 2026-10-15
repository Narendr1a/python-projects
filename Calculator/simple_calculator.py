import math
import statistics

def Calculator():
    while True:
        print("----- Simple Calculator -----")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo")
        print("6. Floor division")
        print("7. power")
        print("8. Logarithms and exponential")
        print("9. Trigonometry and statistics")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "10":
            print("Calculator closed")
            break
        try:
            if choice in ("1", "2", "3", "4", "5", "6", "7"):
                n1 = float(input("Enter your 1st number: "))
                n2 = float(input("Enter your 2nd number: "))

                match(choice):
                    case "1":
                        print("Result: ", n1+n2)
                    case "2":
                        print("Result: ", n1-n2)
                    case "3":
                        print("Result: ", n1*n2)
                    case "4":
                        if n2 == 0:
                            print("Cannot perform Divide by zero")
                        else:
                            print("Result: ", n1/n2)
                    case "5":
                        if n2 == 0:
                            print("Cannot perform modulo by zero")
                        else:
                            print("Result: ", n1%n2)
                    case "6":
                        if n2 == 0:
                            print("Cannot perform floor division by zero")
                        else:
                            print("Result: ", n1//n2)
                    case "7":
                        print("Result: ", n1**n2)

            elif choice == "8":
                print("1. Log")
                print("2. Natural log")
                print("3. Exponential")

                sub1 = input("Enter your sub choice: ")

                if sub1 in ("1", "2", "3"):
                    n = float(input("Enter a number: "))

                    if sub1 in ("1", "2") and n <= 0:
                        print("Logarithms require a number greater than zero.")
                    else:
                        match(sub1):
                            case "1":
                                print("Result: ", math.log10(n))
                            case "2":
                                print("Result: ", math.log(n))
                            case "3":
                                print("Result: ", math.exp(n))
                else:
                    print("Invalid choice!! please try again.")

            elif choice == "9":
                print("1. sin")
                print("2. cos")
                print("3. tan")
                print("4. square root")
                print("5. power")
                print("6. mean")
                print("7. median")
                print("8. mode")
                print("9. variance")
                print("10. standard deviation")

                sub2 = input("Enter your 2nd subchoice: ")

                if sub2 in ("1", "2", "3"):
                    angle = float(input("Enter a degree: "))
                    radian = math.radians(angle)

                    match(sub2):
                        case "1":
                            print("Result: ", math.sin(radian))
                        case "2":
                            print("Result: ", math.cos(radian))
                        case "3":
                            print("Result: ", math.tan(radian))

                elif sub2 == "4":
                    n = float(input("Enter the number: "))
                    if n < 0:
                        print("Error: Square root requires a non-negative number.")
                    else:
                        print("Result: ", math.sqrt(n))

                elif sub2 == "5":
                    a = float(input("Enter the number: "))
                    b = float(input("Enter the number: "))
                    print("Result: ", math.pow(a, b))

                elif sub2 in ("6", "7", "8", "9", "10"):
                    nums = list(map(float, input("Enter the numbers: ").split()))

                    if not nums:
                        print("Please! enter atleast one number")
                    elif sub2 == "6":
                        print("Result: ", statistics.mean(nums))
                    elif sub2 == "7":
                        print("Result: ", statistics.median(nums))
                    elif sub2 == "8":
                        try:
                            print("Result: ", statistics.mode(nums))
                        except statistics.StatisticsError:
                            print("No unique values were found !!")
                    elif len(nums)<2 and sub2 in ("9", "10"):
                            print("Atleast 2 numbers are required.")
                    elif sub2 == "9":
                        print("Result: ", statistics.variance(nums))
                    elif sub2 == "10":
                        print("Result: ", statistics.stdev(nums))
                    else:
                        print("Invalid function sub2 choice! please try again.")
                else:
                    print("Invalid choice!! please try again.")
            else:
                print("Invalid choice!! please try again.")

        except (ValueError, OverflowError) as e:
            print("Invalid input or choice", e)
    


if __name__ == '__main__':
    Calculator()
