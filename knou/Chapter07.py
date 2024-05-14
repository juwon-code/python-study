# 제 07강. 반복 구조


# num 까지의 총합을 계산하는 프로그램.
sum = 0
itr = 1
num = int(input("어디까지 더할까요? "))
while itr <= num:
    sum = sum + itr
    itr = itr + 1
print(sum)

# 구구단을 출력하는 프로그램.
itr = 1
num = int(input("출력할 단을 입력하세요: "))
while itr <= 9:
    print(num, " X ", itr, " = ", num * itr)
    itr = itr + 1


# 리스트를 생성하고 원소를 출력하는 프로그램.
list = [1, 4, 14, 26, 31]
for element in list:
    print(element)

# 원뿔의 부피와 겉넓이를 출력하는 프로그램 1.
# 높이를 담고 있는 리스트 생성.
height_list = [1, 5, 14, 26, 31]
radius = 10

# 리스트를 순회하여 결과 출력.
for height in height_list:
    # 부피와 겉넓이 계산 및 출력.
    volume = 1 / 3 * 3.14 * radius ** 2 * height
    surface = 3.14 * radius ** 2 + 3.14 * radius * height
    print("반지름", radius, "높이", height, "원뿔")
    print("부피의 값은 ", volume, "입니다.", sep = "")
    print("겉넓이의 값은 ", surface, "입니다.", sep = "")


# 원뿔의 부피와 겉넓이를 출력하는 프로그램 2.
# 반지름은 10씩 순차적으로 증가하는 리스트로 생성.
radius_list = range(10, 40, 10)
height_list = [1, 5, 14]

# radius와 height값을 순회하여 결과 출력.
# 여러 리스트 값을 가져오는 zip 함수 사용.
for radius, height in zip(radius_list, height_list):
    # 부피와 겉넓이 계산 및 출력.
    volume = 1 / 3 * 3.14 * radius ** 2 * height
    surface = 3.14 * radius ** 2 + 3.14 * radius * height
    print("반지름", radius, "높이", height, "원뿔")
    print("부피의 값은 ", volume, "입니다.", sep = "")
    print("겉넓이의 값은 ", surface, "입니다.", sep = "")


# 구구단 표를 출력하는 프로그램.
# 표 제목.
# format()를 사용하여 문자열을 정렬할 수 있다.
# >20s는 문자열을 20칸을 공백으로 오른쪽 정렬한다는 뜻.
print(format("구구단표", ">20s"))

# 표 머리.
# print()에서 end를 사용하여 개행을 막을 수 있다.
print("  |", end = "")
for i in range(1, 10):
    print("  ", i, end = "")

# 새로운 행 삽입.
# print()의 내용을 비워 개행한다.
print()
print("----------------------------------------")

# 구구단 표 출력.
for i in range(1, 10):
    print(i, "|", end="")
    for j in range(1, 10):
        print(format(i * j, ">4d"), end="")
    print()