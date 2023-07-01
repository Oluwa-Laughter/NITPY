def add_numbers(*nums) -> int:
    """
    This function takes any number of numbers as arguments and returns the sum of those numbers.
    """
    sum = 0
    for i in nums:
        sum += i
    return sum


print(add_numbers(1, 2, 3, 4, 5))


def find(nums: "list[int]", num: int) -> int:
    """
    This function takes an ordered list of number,
    and a number, and returns the index of that number within the list.
    The function should return [-1] if the number is not found
    """
    for i in range(len(nums)):
        if nums[i] == num:
            return i
    return -1


print(
    find(
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
        ],
        7,
    )
)
