# 제 09강. 함수


# 원뿔의 부피를 출력하는 프로그램 1.
# 원뿔 부피를 출력하는 함수 정의.
def print_cone_volume_1(radius, height):
    if radius > 0 and height > 0:
        # 반지름과 높이가 모두 양수 일 때
        volume = 1 / 3 * 3.14 * radius ** 2 * height
        print("원뿔의 부피는", volume, "입니다.")
    else:
        # 반지름 또는 높이가 음수일 때
        print("반지름과 높이는 양수여야 합니다.")

# 함수를 호출하여 결과 출력.
radius = 20
height = 30
print_cone_volume_1(radius, height)


# 숫자를 입력받고 역순으로 출력하는 프로그램.
# 자릿수를 역순으로 출력하는 함수 정의.
def print_number_reverse(number):
    while number > 0:
        digit = number % 10
        number = number // 10
        print(digit, end="")

# 함수를 호출하여 결과 출력.
number = 1234
print_number_reverse(number)


# 원뿔의 부피를 출력하는 프로그램 2.
# 원뿔 부피를 반환하는 함수 정의.
def return_cone_volume_2(radius, height):
    if radius > 0 and height > 0:
        # 반지름과 높이가 모두 양수 일 때
        volume = 1 / 3 * 3.14 * radius ** 2 * height
        return volume
    else:
        # 반지름 또는 높이가 음수일 때
        print("반지름과 높이는 양수여야 합니다.")

# 함수를 호출하여 결과 출력.
print()
print(format(return_cone_volume_2(10, 20), "<20.3f"), "입니다.")


# 원뿔의 부피와 겉넓이를 출력하는 프로그램 1.
def return_cone_volume_surface_1(radius, height):
    if radius > 0 and height > 0:
        # 반지름과 높이가 모두 양수 일 때
        volume = 1 / 3 * 3.14 * radius ** 2 * height
        surface = 3.14 * radius ** 2 + 3.14 * radius * height
        return volume, surface # 변수를 동시 반환.
    else:
        # 반지름 또는 높이가 음수일 때
        print("반지름과 높이는 양수여야 합니다.")

# 함수를 호출하여 결과 출력.
# 변수에 결과값을 동시 할당.
volume, surface = return_cone_volume_surface_1(50, 100)
print(volume, "입니다.")
print(surface, "입니다.")


# 세 개의 사용자 입력을 오름차순으로 정렬하고 결과를 출력하는 프로그램.
# 세 숫자를 정렬하고 출력하는 함수.
def print_sort_3_number(number1, number2, number3):
    if number1 > number2:
        number1, number2 = number2, number1
    if number1 > number3:
        number1, number3 = number3, number1
    if number2 > number3:
        number2, number3 = number3, number2
    print(number1, number2, number3)

# 세 숫자를 입력받기.
number1 = int(input("첫번째 숫자를 입력하세요: "))
number2 = int(input("두번째 숫자를 입력하세요: "))
number3 = int(input("세번째 숫자를 입력하세요: "))

# 함수를 호출하여 결과 출력.
print_sort_3_number(number1, number2, number3)


# 변수의 스코프.
# 전역 x를 선언한다.
x = 1
print("x의 값은", x)

def increment_x(x):
    # 함수의 x 값을 변경한다.
    x = x + 1
    print("x의 값은", x)

# 함수 호출 후 x값은 변경되지 않는다.
increment_x(x)
print("x의 값은", x)


# 원뿔의 부피와 겉넓이를 출력하는 프로그램 2.
# 사용자 정의 함수의 매개변수 기본값을 설정할 수 있다.
def return_cone_volume_surface_2(radius = 20, height = 30):
    if radius > 0 and height > 0:
        # 반지름과 높이가 모두 양수 일 때
        return 1 / 3 * 3.14 * radius ** 2 * height, 3.14 * radius ** 2 + 3.14 * radius * height
    else:
        # 반지름 또는 높이가 음수일 때
        print("반지름과 높이는 양수여야 합니다.")

# 함수를 호출하여 결과 출력.
print(return_cone_volume_surface_2())


# 개수가 정해지지 않은 수의 합과 평균을 출력하는 프로그램.
# *는 가변 매개변수 앞에 붙인다.
def return_numbers_sum_average(*numbers):
    sum = 0
    count = 0
    for i in numbers:
        sum = sum + i
        count = count + 1
    return sum, sum / count

# 함수를 호출하여 결과 출력.
print(return_numbers_sum_average(10, 20, 30, 40))
print(return_numbers_sum_average(20, 25, 10, 85, 100, 150))