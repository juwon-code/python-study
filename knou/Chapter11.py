# 제 11강. 모듈


# 수학 모듈 임포트.
import math


# 원뿔 클래스 생성.
class Cone:
    # 원뿔 클래스 생성자 메소드.
    def __init__(self, radius = 20, height = 30):
        self.radius = radius
        self.height = height

    # 부피를 반환하는 메소드.
    def get_volume(self):
        return 1 / 3 * math.pi * self.radius ** 2 * self.height # math 모듈에서 제공하는 원주율 값으로 대체.

    # 겉넓이를 반환하는 메소드.
    def get_surface(self):
        return math.pi * self.radius ** 2 + math.pi * self.radius * self.height


# 삼각형 넓이를 계산하는 프로그램.
# 두변의 길이와 끼인각이 주어질 때, 삼각형의 넓이를 구하는 프로그램.
from math import sin, radians # from을 사용하여, 모듈명을 제외할 수 있다.
a, b = 10, 20
area = 1 / 2 * a * b * sin(radians(60))
print(area)


# 로또 추첨 프로그램.
# 1 ~ 45 숫자 6개를 입력받아 당첨 숫자와 비교하는 프로그램.
# 랜덤 모듈 임포트.
import random

# 숫자를 입력받고 리스트에 삽입한다.
goal_str = input("1~45 번호 6개를 쉼표+스페이스로 분리하여 입력하세요: ").split(", ")
goal_list = list()
for i in goal_str:
    goal_list.append(int(i))

# 1 ~ 45 개의 랜덤 숫자 6개를 리스트 형태로 받아온다.
lotto_list = random.sample(range(1, 46, 1), 6)
print("당첨 번호는", goal_list, "입니다.")
print("추첨 번호는", lotto_list, "입니다.")

# 당첨 리스트와 랜덤 리스트의 원소들의 일치횟수를 출력한다.
hit_count = 0
for goal_int in goal_list:
    if goal_int in lotto_list:
        hit_count = hit_count + 1
print("축하합니다" + str(hit_count) + "개 맞았습니다.")


# 스무고개 프로그램.
# 20번의 기회 안에 1 ~ 1000 사이의 숫자를 맞추는 프로그램.
# 1 ~ 1000 사이의 랜덤 숫자를 받는다.
hit_number = random.randint(1, 1001)

# 20 횟수 동안 일치 여부를 검사한다.
is_success = False
for i in range(1, 21, 1):
    guess_number = int(input("숫자를 맞혀보세요(" + str(i) + "번째 시도): "))
    if guess_number == hit_number:
        is_success = True
        break
    elif guess_number < hit_number:
        print(str(guess_number) + "보다 큽니다.", end="")
    else:
        print(str(guess_number) + "보다 작습니다.", end="")

# 결과를 출력한다.
if is_success:
    print("맞췄습니다. 축하합니다.")
else:
    print("모든 기회를 다 사용하셨습니다. 다음에 다시 도전하세요.")


# 소수 찾기 프로그램.
# 1 ~ 1000 사이의 소수를 찾고 실행시간을 출력하는 프로그램.
# 타임 모듈 임포트.
import time

# 시작 시간을 구한다.
start_time = time.time()

# 소수를 검사하는 함수.
def check_number_prime(x):
    # 2부터 x까지 검사하여 나누어 떨어질 경우 소수.
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# 2부터 1000까지 검사하여 소수 개수를 구한다.
prime_count = 0
for i in range(2, 1001):
    if check_number_prime(i):
        prime_count = prime_count + 1
        print(i, end=", ")

# 종료 시간을 구한다.
end_time = time.time()
print(end_time - start_time, "초 실행했습니다.")