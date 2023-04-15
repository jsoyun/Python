def dict2(nums):
    # 가장긴 연속된변수를 여기다 저장할거임
    longest = 0
    dictionary = {}
    for num in nums:
        dictionary[num] = True
    for n in dictionary:
        # n보다 앞에 있는애가 있나?
        # 시작점 판별하는 조건문!
        if n-1 not in dictionary:
            cnt = 1  # 시작하면 일단 카운트1
            target = n + 1
            while target in n:  # 연속된 값있는지!
                target += 1  # 다음 수 찾아야돼서 +1
                cnt += 1
            longest = max(longest, cnt)

    return longest


nums = [100, 4, 200, 1, 3, 2]
print(dict2(nums))
