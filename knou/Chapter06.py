# 제 06강. 선택 구조


# 비교 연산 예시.
print(3 < 6)
print(3 == 6)

# 논리 연산 예시.
temperature = 20
weather = "summer"

print(temperature > 20 and weather == "spring")
print(temperature > 20 or weather == "summer")
print(not temperature == 20)


# 원뿔의 부피와 겉넓이를 출력하는 프로그램.
# 반지름과 높이 값 입력받기.
radius = int(input("원뿔 반지름의 값을 입력하세요: "))
height = int(input("원뿔 높이의 값을 입력하세요: "))

# 반지름과 높이 값이 양수일 경우 실행.
if radius > 0 and height > 0:
    # 부피와 겉넓이 계산 및 출력.
    volume = 1 / 3 * 3.14 * radius ** 2 * height
    surface = 3.14 * radius ** 2 + 3.14 * radius * height
    print("부피의 값은 ", volume, "입니다.", sep="")
    print("겉넓이의 값은 ", surface, "입니다.", sep="")
# 모두 음수일 경우 에러 메시지 출력.
else:
    print("반지름과 높이 값을 모두 양수로 입력하세요.")
    

# 가장 큰 수를 찾는 프로그램.
# a, b, c 입력받기.
a = int(input("a 입력: "))
b = int(input("b 입력: "))
c = int(input("c 입력: "))

# a, b, c 중 가장 큰 수 출력.
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)