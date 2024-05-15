# 제 13강. 실전 프로젝트 1


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


# 틱택토 클래스 생성.
class TicTacToe:
    # 게임판 생성
    def __init__(self):

    # 게임판 초기화.
    def create_board(self):

    # 첫 플레이어 선택.
    def select_first_player(self):

    # 기호 표시.
    def mark_spot(self, row, col, player):

    # 승리 상태 확인.
    def is_winner(self, player):

    # 잔여 빈칸 여부 확인.
    def is_board_full(self):

    # 플레이어 변경.
    def next_player(self, player):

    # 현재 게임판 출력.
    def show_board(self):

    # 게임 시작.
    def start(self):
        while True:


# 게임 생성.
TTT = TicTacToe()

# 게임 시작.
TTT.start()