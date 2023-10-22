from math_function import add


def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = add(data_1, data_2)

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()

from math_function import multiply, divide

result_multiply = multiply(5, 3)
print(f"5 * 3 = {result_multiply}")

result_divide = divide(10, 2)
print(f"10 / 2 = {result_divide}")
