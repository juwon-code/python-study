# 제 13강. 실전 프로젝트 2


# 틱택토 게임 설계
# 1. 2차원 리스트를 사용하여 게임판을 생성하고 빈칸으로 초기화.
# 2. 게임판에 빈칸이 남아있는지 확인.
# 3. 둘 중 한 플레이어가 승리했는지 확인.
# 4. 게임판의 현재 상태를 출력.
# 5. 게임 시작.
# - 무작위로 선공할 플레이어 선택.
# - 게임 루프를 기동.
# - 게임판의 현재 상태를 출력하고 다음 플레이어가 빈칸 선택.
# - 플레이어가 선택할 빈칸의 위치(행과 열 번호)를 입력받음.
#     - 사용자일 경우 사용자 입력을 통해 행과 열 번호를 입력.
#     - 컴퓨터일 경우 무작위로 행과 열 번호를 선택.
# - 플레이어가 선택한 위치에 기호를 표시하고 게임판을 업데이트.
# - 현재 플레이어가 승리했는지 확인.
# - 게임판에 빈칸이 남아있는지 확인.
#     - 게임판이 가득찬 경우, 무승부 메시지를 출력하고 루프를 종료.

# 랜덤 모듈 임포트.
import random as rd

# 틱택토 클래스 생성.
class TicTacToe:
    # 게임판 생성
    def __init__(self):
        self.board = []

    # 게임판 초기화.
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('*')
            self.board.append(row)

    # 첫 플레이어 선택.
    def select_first_player(self):
        if rd.randint(0, 1):
            return 'X'
        else:
            return 'O'

    # 기호 표시.
    def mark_spot(self, row, col, player):
        self.board[row][col] = player

    # 승리 상태 확인.
    def is_winner(self, player):
        n = len(self.board)
        # 행 확인.
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win == True:
                return win
        # 열 확인.
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win == True:
                return win
        # 대각선 확인.
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win == True:
            return win
        # 역대각선 확인.
        win = True
        for i in range(n):
            if self.board[i][n - i - 1] != player:
                win = False
                break
        if win == True:
            return win
        return False

    # 잔여 빈칸 여부 확인.
    def is_board_full(self):
        for row in self.board:
            for item in row:
                if item == "*":
                    return False
        return True

    # 플레이어 변경.
    def next_player(self, player):
        if player == 'O':
            return 'X'
        else:
            return 'O'

    # 현재 게임판 출력.
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    # 게임 시작.
    def start(self):
        # 새 게임판 생성.
        self.create_board()
        self.show_board()
        # 첫 플레이어 선택.
        player = self.select_first_player()
        # 게임 루프 시작.
        while True:
            if player == 'X':
                print("컴퓨터 차례입니다.")
            else:
                print("사용자 차례입니다.")
            # 현재 게임판 출력.
            self.show_board()
            # 컴퓨터일 경우 랜덤 위치 반환.
            if player == 'X':
                while True:
                    row, col = rd.randint(1, 3), rd.randint(1, 3)
                    if self.board[row - 1][col - 1] == "*":
                        break
                print("컴퓨터가 행 " + str(row) + ", 열 " + str(col) + "을/를 선택했습니다.")
                print()
            else:
                row, col = list(map(int, input("선택할 빈칸의 위치를 입력하세요: ").split()))
                print("사용자가 행 " + str(row) + ", 열 " + str(col) + "을/를 선택했습니다.")
                print()
            # row, col 입력값이 0,0 인경우 종료.
            if row == 0 and col == 0:
                break
            # 입력된 위치 표시.
            self.mark_spot(row - 1, col - 1, player)
            self.show_board()
            # 현재 플레이어가 이겼는지 확인.
            if self.is_winner(player) == True:
                if player == 'X':
                    print("컴퓨터가 이겼습니다. 다시 도전하세요.")
                else:
                    print("사용자가 이겼습니다. 축하합니다.")
                break
            # 게임판 가득참 확인. 빈칸 여부 확인
            if self.is_board_full() == True:
                print("무승부입니다. 다시 도전하세요.")
                break
            # 플레이어 변경
            player = self.next_player(player)
        # 최종 게이판 출력
        print()
        self.show_board()


# 게임 생성.
TTT = TicTacToe()

# 게임 시작.
TTT.start()