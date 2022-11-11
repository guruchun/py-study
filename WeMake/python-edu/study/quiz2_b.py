def validate_seq_number(nums):
    diff = []
    for i in range(len(nums) - 1):
        diff.append(nums[i] - nums[i+1])

    # check seq
    seq_count = 0
    for i in range(len(diff) - 1):
        if abs(diff[i]) == 1 and diff[i] == diff[i+1]:
            print("seq= %d, %d, %d" % (nums[i], nums[i+1], nums[i+2]))
            seq_count += 1
        else:
            seq_count = 0

        if seq_count >= 1:
            return False
    return True


def validate_same_number(nums):
    diff = []
    for i in range(len(nums) - 1):
        diff.append(nums[i] - nums[i+1])

    # check same
    seq_count = 0
    for i in range(len(diff) - 1):
        if diff[i] == diff[i+1] == 0:
            print("dup= %d, %d, %d" % (nums[i], nums[i+1], nums[i+2]))
            seq_count += 1
        else:
            seq_count = 0

        if seq_count >= 1:
            return False
    return True


def validate_same_pattern(nums):
    num_str = ''.join(str(x) for x in nums)
    print("input=", num_str)
    for i in range(len(num_str) - 2):
        cmp_width = 2
        while i + cmp_width*2 <= len(num_str):
            part1 = num_str[i:i+cmp_width]
            part2 = num_str[i+cmp_width:i+cmp_width*2]
            print("start=%d, width=%d, part1=%s, part2=%s" % (i, cmp_width, part1, part2))
            if part1 == part2:
                print("matching! start=%d, %s, %s" % (i, part1, part2))
                return False
            cmp_width += 1

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
