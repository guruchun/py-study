def validate_seq_number(nums):
    # check inc
    seq_count = 0
    for i in range(0, len(nums) - 1):
        if int(nums[i]) == (nums[i+1] + 1) % 10:
            seq_count += 1
            print("seq- %d, %d, %d" % (nums[i], nums[i+1], seq_count))
        else:
            seq_count = 0
            
        if seq_count >= 2:
            return False
        
    # check dec
    seq_count = 0
    for i in range(0, len(nums) - 1):
        if int(nums[i]) == (int(nums[i] + 1) - 1) % 10:
            seq_count += 1
            print("seq+ %d, %d, %d" % (nums[i], nums[i+1], seq_count))
        else:
            seq_count = 0
            
        if seq_count >= 2:
            return False
    return True


def validate_same_number(nums):
    seq_count = 0
    for i in range(0, len(nums)-1):
        if nums[i] == nums[i+1]:
            seq_count += 1
            print("dup= %d, %d, %d" % (nums[i], nums[i+1], seq_count))
        else:
            seq_count = 0
            
        if seq_count >= 2:
            return False
    return True


def validate_same_pattern(nums):
    print(nums)
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
