def validate_seq_number(nums):
    return True


def validate_same_number(nums):
    return True


def validate_same_pattern(nums):
    return True


# main body
def main():
    while True:
        input_str = input("input 4 numbers(콤마로 구분): ")
        numbers = input_str.split(',')
        for i in range(0, len(numbers)):
            numbers[i] = int(numbers[i].strip())

        ok = validate_same_number(numbers)
        if ok:
            ok = validate_seq_number(numbers)
        if ok:
            ok = validate_same_pattern(numbers)

        if ok:
            print("pass")
            break
        else:
            print("fail, try again...")


# start program
main()
