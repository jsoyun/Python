

def question(nums, target):
    dictionary = {}
    for v in nums:
        dictionary[v] = True
    for d in dictionary:
        value = target - d

        if value != d in dictionary:

            return True
    return False


nums = [4, 1, 9, 7, 5, 3, 16]


print(question(nums, target=14))
