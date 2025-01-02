# 한줄 주석
""" 
여러줄 주석
사용
"""

# 변수 (파이썬에서는 기본적으로 타입을 명시하지 않음)
str1 = "Life is too short, You need Python"
str2 = "123"
num1 = 10
num2 = 10.5

# bool = True : False 표현 (대문자로 시작해야함)
flag = True

# type(변수) : 변수는 어떤 타입인가?
print(str1, type(str1))  # <class 'str'>
print(str2, type(str2))
print(num1, type(num1))  # 10 <class 'int'>
print(num2, type(num2))  # 10.5 <class 'float'>
print(flag, type(flag))  # True <class 'bool'>

# 두 개의 변수에 같은 값 대입
a = b = 3
print("a , b : ", a, b)

a, b = 10, 15
print(a, b)
a, b = b, a
print("교환 값 : ", a, b)

# str2 = str2 + 100  # TypeError: can only concatenate str (not "int") to str

# int() : int 타입 변환
str2 = int(str2) + 100
print(str2)

print("bool => int 변환", int(flag))
print("int(98.6) : ", int(98.6))

# float() 형변환
print("float(98.6) : ", float(98.6))
print("float(flag) : ", float(flag))

# str() 형변환
print("str(98.6) : ", str(98.6))

# bool() 형변환
print("bool(98.6) : ", str(98.6))


# 문자열 자료형
# "",'',"""""",''''''
str3 = "Python's favrite food id perl"
print(str3)

# "출력"
str3 = '"Python favrite food id perl"'
print(str3)
str3 = '"Python\'s favrite food id perl"'
print(str3)

multiline = """ 
Life is short
You need Python 
"""
print(multiline)
