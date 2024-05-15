# 제 12강. 파일


# Khan.txt 파일을 읽고 출력하는 프로그램.
# Kahn.txt 파일을 읽기 모드로 연다.
khan_fp = open("Khan.txt", "r")

# 텍스트 파일을 10줄씩 읽는다.
print(khan_fp.read(10))
print(khan_fp.readline(10))

# 텍스트 파일을 1줄씩 읽고 출력한다.
for motto_str in khan_fp.readlines():
    print(motto_str.strip()) # 개행 문자를 제거한다.

# 파일을 닫는다.
khan_fp.close()


# Khan.txt 파일을 수정하는 프로그램.
# Khan.txt 파일을 덧붙이기 모드로 연다.
khan_fp = open("Khan.txt", "a")

# 파일 끝에 텍스트를 추가하고 닫는다.
khan_fp.write("\n")
khan_fp.write(format("-칭기스 칸-", ">50s"))
khan_fp.close()


# Hamlet_by_Shakespeare.txt 파일에 포함된 단어의 출현 횟수를 출력하는 프로그램.
# Hamlet_by_Shakespeare.txt 파일을 읽기 모드로 연다.
h_fp = open("Hamlet_by_Shakespeare.txt", "r")

# 단어와 횟수를 담을 딕셔너리를 생성한다.
word_dict = dict()

# 단어의 특수문자를 제거하고 소문자로 바꾸어 딕셔너리에 단어:횟수 형식으로 저장한다.
for line in h_fp.readlines():
    for word in line.strip().split():
        word = word.strip(" .,:;-?![]\"\'").lower()
        if word_dict.get(word) is not None:
            count = word_dict[word]
        else:
            count = 0
        word_dict[word] = count + 1

# 딕셔너리를 출력한다.
for key in word_dict:
    print("[" + key + "]", str(word_dict[key]) + "회")

# 파일을 닫는다.
h_fp.close()

# 딕셔너리를 값을 기준으로 정렬한다.
# 키와 값이 교체된 딕셔너리를 생성한다.
word_exchange_dict = {v:k for (k, v) in word_dict.items()}

# 딕셔너리를 정렬하고 원본 딕셔너리로 변경한다.
word_dict = {k:v for (v, k) in sorted(word_exchange_dict.items(), reverse=True)}

# 100 회 이상 등장하는 단어만 출력한다.
for key in word_dict:
    if word_dict[key] >= 100:
        print("[" + key + "]", str(word_dict[key]) + "회")