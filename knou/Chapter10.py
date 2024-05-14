# 제 10강. 객체지향


# 원뿔 클래스 생성.
class Cone:
    # 원뿔 클래스 생성자 메소드.
    def __init__(self, radius = 20, height = 30):
        self.radius = radius
        self.height = height

    # 부피를 반환하는 메소드.
    def get_volume(self):
        return 1 / 3 * 3.14 * self.radius ** 2 * self.height

    # 겉넓이를 반환하는 메소드.
    def get_surface(self):
        return 3.14 * self.radius ** 2 + 3.14 * self.radius * self.height


# BMI 클래스 생성.
class BMI:
    # BMI 클래스 생성자 메소드.
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    # BMI 수치를 반환하는 메소드.
    def get_BMI(self):
        return self.weight / (self.height / 100) ** 2

    # 체중 상태를 반환하는 메소드.
    def get_status(self):
        BMI = self.get_BMI()
        if BMI >= 25:
            return "비만"
        elif BMI >= 23 and BMI < 25:
            return "과체중"
        elif BMI >= 18.5 and BMI < 23:
            return "정상"
        else:
            return "저체중"


# 원뿔 클래스의 활용.
# 반지름이 50, 높이가 100인 원뿔의 부피와 겉넓이를 출력하는 프로그램.
default_cone = Cone()
cone = Cone(50, 100)
print("기본 원뿔의 겉넓이는 ", default_cone.get_surface(), "부피는 ", default_cone.get_volume(), "이다.", sep="")
print("원뿔의 겉넓이는 ", cone.get_surface(), "부피는 ", cone.get_volume(), "이다.", sep="")


# BMI 클래스의 활용.
# 가상의 이름, 나이, 몸무게, 키로 BMI 객체를 사용하는 프로그램.
person = BMI("홍길동", 40, 78, 182)
print(person.name + "님(" + str(person.age) + "세)의 BMI 수치는", person.get_BMI(), "결과는", person.get_status(), "입니다.")


# 원뿔 클래스 개선.
class ConeImproved:
    # 원뿔 클래스 생성자 메소드.
    def __init__(self, radius=20, height=30):
        self.__radius = radius # __를 사용하여 private로 처리한다.
        self.__height = height

    # 부피를 반환하는 메소드.
    def get_volume(self):
        return 1 / 3 * 3.14 * self.__radius ** 2 * self.__height

    # 겉넓이를 반환하는 메소드.
    def get_surface(self):
        return 3.14 * self.__radius ** 2 + 3.14 * self.__radius * self.__height

    # 반지름을 반환하는 메소드.
    def get_radius(self):
        return self.__radius

    # 반지름을 설정하는 메소드.
    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius

    # 높이를 반환하는 메소드.
    def get_height(self):
        return self.__height

    # 높이를 설정하는 메소드.
    def set_height(self, height):
        if height > 0:
            self.__height = height


# BMI 클래스 개선.
class BMIImproved:
    # BMI 클래스 생성자 메소드.
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    # BMI 수치를 반환하는 메소드.
    def get_BMI(self):
        return self.__weight / (self.__height / 100) ** 2

    # 체중 상태를 반환하는 메소드.
    def get_status(self):
        bmi = self.get_BMI()
        if bmi >= 25:
            return "비만"
        elif 23 <= bmi < 25:
            return "과체중"
        elif 18.5 <= bmi < 23:
            return "정상"
        else:
            return "저체중"

    # 이름을 반환하는 메소드.
    def get_name(self):
        return self.__name

    # 이름을 설정하는 메소드.
    def set_name(self, name):
        if type(name) is str:
            self.__name = name

    # 나이를 반환하는 메소드.
    def get_age(self):
        return self.__age

    # 나이를 설정하는 메소드.
    def set_age(self, age):
        if age > 0:
            self.__age = age

    # 몸무게를 반환하는 메소드.
    def get_weight(self):
        return self.__weight

    # 몸무게를 설정하는 메소드.
    def set_weight(self, weight):
        if weight > 0:
            self.__weight = weight

    # 키를 반환하는 메소드.
    def get_height(self):
        return self.__height

    # 키를 설정하는 메소드.
    def set_height(self, height):
        if height > 0:
            self.__height = height