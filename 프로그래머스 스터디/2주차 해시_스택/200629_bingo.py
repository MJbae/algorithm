import collections


def solution(board, nums):
    SIZE = len(board)
    board_dict = {board[row][col]: [row, col] for row in range(SIZE) for col in range(SIZE)}
    check_row = {i: [] for i in range(SIZE)}
    check_col = {j: [] for j in range(SIZE)}
    check_diagonal_L = []
    check_diagonal_R = []
    answer = 0

    # nums 각 요소값이 board에서 갖는 인덱스를 활용하여 가로, 세로, 대각선 상에 체크한다
    for num in nums:
        row, col = board_dict[num]

        check_row[row].append(num)
        check_col[col].append(num)
        if row == col:
            check_diagonal_L.append(num)
        if row + col == SIZE - 1:
            check_diagonal_R.append(num)

    # 위에서 num의 위치를 체크한 자료형을 활용하여 빙고 여부 확인
    for i in range(SIZE):
        if len(check_row[i]) == SIZE:
            answer += 1
        if len(check_col[i]) == SIZE:
            answer += 1

    if len(check_diagonal_L) == SIZE:
        answer += 1
    if len(check_diagonal_R) == SIZE:
        answer += 1

    return answer