# 딕션어리 선언 및 초기화,키는 유일해야함! 값은 중복될 수 있어도
score = {
    'math': 97,
    'eng': 49,
    'kor': 89
}

print(score['math'])
# list 쓰는 것과 같음
# 덮어씌워짐
score['math'] = 88
score['sci'] = 100
print(score['sci'])

# d이 과목있나?
print('music' in score)

# in으로 하면 바로 찾을 수 잇어! O(1)
# 랜덤액세스 처럼 바로 접근해서 찾을 수 있돠~!
if 'music' in score:
    print(score['music'])
else:
    score['music'] = 0

    print(score['music'])
