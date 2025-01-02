# 연산자
# 1. 산술연산자(+,-,*,/,//,**,%)
# / : 나머지까지 출력
# // : 몫만 출력(자바 / 와 같은 개념)
a, b = 5, 3
print(a + b, a - b, a * b, a / b, a // b, a**b, a % b)

# 문자열 연결
s1, s2, s3 = "100", "100.123", "1234567"
print(s1 + s2 + s3)

# 문자열 + 정수 : 파이썬 에서는 오류 발생
print(s1 + str(1))

# 복합대입연산자
a = 10
a += 5  # a = a + 5  => 15
print(a)
a -= 5  # a = a - 5 => 10
print(a)
a *= 5  # a = a * 5 => 50
print(a)
a /= 5  # a = a / 5 => 10.0
print(a)
a //= 5  # a = a // 5 => 2.0
print(a)
a %= 5  # a = a % 5 => 2
print(a)

# 7,777원을 가지고 있다. 동전으로 교환하기
# 500원 : 15개, 100원 : 2개, 50원 : 1개, 10원 :2개, 나머지 돈 7원

# don500, don100, don50, don10 = 500, 100, 50, 10

# my %= don500
# print(my)
# my %= don100
# print(my)
# my %= don50
# print(my)
# my %= don10
# print(my)

my = 7777
don500, don100, don50, don10 = 0, 0, 0, 0

don500 = my // 500  # 500원으로 나눴을시
my %= 500
print(my)

don100 = my // 100  # 100원으로 나눴을시
my %= 100
print(my)

don50 = my // 50  # 50원으로 나눴을시
my %= 50
print(my)

don10 = my // 10  # 10원으로 나눴을시
my %= 10
print(my)

print("500원 : %d 개" % don500)
print("100원 : %d 개" % don100)
print("50원 : %d 개" % don50)
print("10원 : %d 개" % don10)
print("나머지 돈 : %d 원" % my)

# 관계(비교) 연산자 : 결과가 true or false
a, b = 10, 0
print("a == b", (a == b))
print("a == b", (a != b))
print("a == b", (a >= b))
print("a == b", (a <= b))

# 논리 연산자 : and, or, not
a, b, c = 100, 60, 15
print("a > b and b > c", a > b and b > c)
print("a < b or b < c", a > b or b > c)
print("not False", not False)
print("not b < c", not b < c)
