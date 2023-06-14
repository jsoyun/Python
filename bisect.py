
# 이진탐색 모듈화
import bisect

def binary_search(array, target):
    # bisect_left() 함수를 사용하여 배열에서 target의 삽입 위치를 찾는다
    # bisect_left() 함수는 이미 정렬된 배열에서 target이 들어갈 적절한 위치(왼쪽 끝)를 반환
    index = bisect.bisect_left(array, target)
    print("index",index)
    print("target:",target)
    
    # 만약 index가 배열의 길이를 초과하지 않고, 해당 위치에 있는 값이 target과 같다면
    if index < len(array) and array[index] == target:
        # 해당 위치(index)를 반환
        return 1
    else:
        # 그렇지 않으면, target이 배열에 없으므로 -1을 반환
        return -1

array = [4,1,5, 2, 3]
print(binary_search(array , 5))
print(map())