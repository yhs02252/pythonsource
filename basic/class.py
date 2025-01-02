# 클래스 정의
class User_info:
    def user_info(self):
        print("메소드 실행")


# 객체 생성
user1 = User_info()
user1.user_info()


class Car:
    # class 안에 있는 메서드들은 모드 self를 가지고 있어야함
    # self == this

    # 생성자
    def __init__(self):
        self.color = "Red"
        self.speed = 0

    def up_speed(self, value):
        self.speed += value

    def down_speed(self, value):
        self.speed -= value


car1 = Car()
car2 = Car()

car1.up_speed(100)
car1.down_speed(20)
print(f"car1 자동차 색상은 {car1.color}, 속력은 {car1.speed}")

car2.color = "black"
car2.up_speed(200)
print(f"car2 자동차 색상은 {car2.color}, 속력은 {car2.speed}")
