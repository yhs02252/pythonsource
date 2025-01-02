# 클래스 정의
# self : 인스턴스 변수
# self 없이 사용 : 클래스 변수
class User_info:

    user_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User_info.user_count += 1

    def user_info(self):
        return f"name : {self.name}, age : {self.age}"
        # print("메소드 실행")

    def __del__(self):
        User_info.user_count -= 1

    # self가 없다면 클래스 메소드로 작동함
    def function1():
        print("function1 호출")

    @classmethod
    def function2(cls):
        print("function2 호출")

    # toString() 역할
    def __str__(self):
        return f"name : {self.name}, age : {self.age}"


# 객체 생성
user1 = User_info("홍길동", 30)
print(user1.user_info())
# print(user1.user_count)
print("유저2 생성전 : ", User_info.user_count)

user2 = User_info("성춘향", 30)
print(user2.user_info())

# static 변수와 같은 개념
print("유저2 생성 후 유저1.count : ", user1.user_count)
print(user2.user_count)
print(User_info.user_count)

del user1
print("user1 삭제 ", User_info.user_count)

print(user2)  # <__main__.User_info object at 0x00000124F0C04A50>
# __str__ 이 있을 경우 : name : 성춘향, age : 30
# print(user2.__str__) # <bound method User_info.__str__ of <__main__.User_info object at 0x000001A393AF4A50>>

# user2.function1()  # self를 안 줄 경우 에러가 뜸

User_info.function1()  # class로 불러야함
User_info.function2()
