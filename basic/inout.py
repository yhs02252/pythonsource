# 화면 입출력
print("T", "E", "S", "T")  # T E S T (자동 공백)

# sep= : 공백으로 인식할 부분 대체
print("T", "E", "S", "T", sep="")  # TEST

# print("Life is too short") => Life is too short
#                               You need Python

# end= : ""간의 공백 추가
# print("Life is too short", end="") # Life is too shortYou need Python
print("Life is too short", end=" ")
print("You need Python")

print("2024", "12", "20", sep="-")

# 문자열 포매팅
# %d : 정수, %f : 부동소수, %c : 문자 1개, %s : 문자열(어떤 형태든 사용 가능)
# I eat 3 apples
apple = 3
print("I eat", apple, "apples")
print("I eat %d apples" % apple)

# 변수 선언또한 가능
msg = "I eat %d apples" % apple
print(msg)

msg = "I eat %s apples" % apple
print(msg)

# %% : % 라는 문자
# print("Error is %d%" % 98)  # Error
print("Error is %d%%" % 98)

# 2개 이상일 때는 ()로 묶어서 명시
number = 10
day = "three"
msg = "I ate %d apples, so I was sick for %s days" % (number, day)
print(msg)


# 포맥코드와 숫자 함께 사용
print("%s" % "hi")
print("%10s" % "hi")  # 전체 길이가 10이고 오른쪽 정렬하고 나머지는 공백
print("%-10sjane" % "hi")  # 전체 길이가 10이고 왼쪽 정렬하고 나머지는 공백

# 소수점 4번째 자리까지 출력
# 0 : 길이에 상관하지 않음
# 10 : 총 10자리를 표현함(소수점 포함, 오른쪽 정렬)
print("%0.4f" % 3.0141592152)
print("%10.4f" % 3.0141592152)


# "".format()
msg = "I eat {} apples".format(apple)
print(msg)

msg = "I ate {} apples, so I was sick for {} days".format(number, day)
print(msg)

# f 문자열 포매팅
msg = f"I ate {number} apples, so I was sick for {day} days"
print(msg)

# ================================================================================
# 키보드 입력
# input()
# print("숫자입력")
# msg = input()
# print(msg)

msg = input("숫자 입력 : ")
print(msg)

# 숫자 2개를 입력 받은 후 연산 프로그램 작성
# 입력받은 값은 문자로 인식
num1 = int(input("첫번째 수 : "))
num2 = int(input("두번째 수 : "))
# print(num1 + num2)  # 1235
print(num1 + num2)
