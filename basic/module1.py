# 모듈 : 함수, 변수, 클래스를 모아놓은 파이썬 파일
#       .py 로 작성된 파일은 전부 모듈


# 파이썬에서 제공되는 기본 모듈 사용하기
# 모듈 불러오기

# import mod1

# print(mod1.add(5, 8))
# print(mod1.sub(4, 2))

# from mod1 import add as numberAddingMethod
from mod1 import *

print(add(7, 3))
print(sub(7, 3))
print()

from mod2 import prt1, prt2

prt1()
prt2()


import mod3

print(mod3.add(17, 5))

m = mod3.Math()
print(m.solv(6))

print(mod3.PI)
