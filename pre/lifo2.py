
def lifo(temp):
    stack = []
    answer = [0] * len(temp)
    for Cur_index, Cur_temp in enumerate(temp):
        while stack and stack[-1][1] < Cur_temp:
            Prev_index, _ = stack.pop()
            answer[Prev_index] = Cur_index - Prev_index
        stack.append((Cur_index, Cur_temp))
    return answer


lifo([73, 74, 75, 71, 69, 72, 76, 73])

print(lifo([73, 74, 75, 71, 69, 72, 76, 73])
      )
