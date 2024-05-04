# 제 05강. 순차 구조


# 삼각형 출력하기.
print("   *")
print("  ***")
print(" *****")
print("*******")


# 변수 값을 입력받기.
variable = input("변수의 값을 입력하세요: ")
print(variable)


# 원뿔의 부피와 겉넓이를 출력하는 프로그램.
# 반지름과, 높이 값 입력받기.
radius = int(input("원뿔 반지름의 값을 입력하세요: "))
height = int(input("원뿔 높이의 값을 입력하세요: "))

# 부피와 겉넓이 계산.
volume = 1 / 3 * 3.14 * radius ** 2 * height
surface = 3.14 * radius ** 2 + 3.14 * radius * height

# 부피와 겉넓이 출력.
# print()에서 파라미터는 ','로 분리할 수 있으며, sep 옵션을 변경하여 공백을 변경할 수 있다.
print("부피의 값은 ", volume, "입니다.", sep="")
print("겉넓이의 값은 ", surface, "입니다.", sep="")