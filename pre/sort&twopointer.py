def twoSum(nums, target):
    nums.sort()  # 정렬
    l, r = 0, len(nums)-1
    # 조건에 따라서 반복문 계속돌거라서 while로 처리
    while l < r:
        if nums[l] + nums[r] > target:
            r = r-l  # 이것도 됨 r -= 1
        elif nums[l] + nums[r] < target:
            l = l+1  # l += 1
        elif nums[l] + nums[r] == target:
            return True
    return False


print(twoSum(nums=[4, 6, 1, 8, 5, 4, 1], target=13))
