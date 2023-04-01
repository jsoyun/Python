print("파이썬으로 코테할거야")
# 자료형 숫자, 문자열, 불
# 어떤값을 담는 자료구조: 변수, 리스트, 튜플, 딕셔너리, 집합
# 정수형 int
# 실수형 float
# 4.24e10 = 4.24 * 10의 10승

# 나누기할 때는 /
# 몫을 표현할때는 //
# **하면 제곱
# %하면 나머지


# 문자형 str

a = "life goes on"
print(a[-1])
# 슬라이싱

print(a[0:5:2])  # 이상, 미만, 간격
print(a[::2])  # 처음부터 끝까지 두칸간격
print(a[::-2])  # 뒤에서 시작해서 두칸씩

# 문자 포맷팅
b = "I eat %d apples." % 3
print(b)

mybaby = "쮜"
heart = 100
a = "나는 우리 %c 를 %d만큼 좋아해!!~!" % (mybaby, heart)
print(a)

# 문자열 포맷코드 따로 있구나!!
# %s 문자열 string
# %c 문자 1개 character
# %d 정수 int
# %f 부동 소수
# %o 8진수
# %x 16진수
# %% literal % 그거 그자체

c = "dfsfsdfsdfsd{name}안뇽헤".format(name="박박모")
print(c)
