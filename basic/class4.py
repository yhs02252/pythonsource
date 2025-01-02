# 상속


class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init__ 호출")

    def test(self):
        print("Parent 클래스의 test 호출")

    def func1(self):
        print("Parent func1() 입니다")


class Child(Parent):
    def __init__(self):
        # 부모 클래스 인스턴스 변수를 호출할 시 부모 클래스 정의가 필요함
        Parent.__init__(self)  # super() 역할
        print("Child 클래스의 __init__ 호출")

    # 오버라이딩 - function 덮어쓰기
    def func1(self):
        print("Child func1() 입니다")


child = Child()
child.test()
child.func1()

print(child.value)
