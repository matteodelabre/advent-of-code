import sys
nums = sys.stdin.readlines()
digits = len(nums[0])
oxy_nums = nums.copy()
co2_nums = nums.copy()

for i in range(digits):
    if len(oxy_nums) > 1:
        oxy_ones = sum(num[i] == "1" for num in oxy_nums)
        oxy_zeroes = sum(num[i] == "0" for num in oxy_nums)

        oxy_nums = [
            num for num in oxy_nums
            if num[i] == ("1" if oxy_ones >= oxy_zeroes else "0")
        ]

    if len(co2_nums) > 1:
        co2_ones = sum(num[i] == "1" for num in co2_nums)
        co2_zeroes = sum(num[i] == "0" for num in co2_nums)

        co2_nums = [
            num for num in co2_nums
            if num[i] == ("0" if co2_ones >= co2_zeroes else "1")
        ]

print(int(oxy_nums[0], 2) * int(co2_nums[0], 2))
