class BingoNumber:
    num: int
    state: bool

    def __init__(self, num):
        self.num = int(num)
        self.state = False

    def __str__(self):
        return str(f'{str(self.num).zfill(2)}{"x" if self.state else " "}')


def parse_line(line: []):
    return list(map(lambda x: BingoNumber(x), line.split()))


class Board:
    rows: []
    won = False

    def __init__(self, lines: []):
        self.rows = []
        for line in lines:
            self.rows.append(parse_line(line))

    def __str__(self):
        printout = ''
        for row in self.rows:
            for bn in row:
                printout += f"{bn} "
            printout += "\n"
        return printout

    def mark(self, num: int):
        if self.won:
            return
        for row in self.rows:
            for bn in row:
                if bn.num == num:
                    bn.state = True

    def cols(self, idx: int):
        for row_idx in range(5):
            yield self.rows[row_idx][idx]

    def is_winning(self):
        # check rows
        for row in self.rows:
            if sum(map(lambda r: r.state, row)) == 5:
                return True
        # check cols
        for idx in range(5):
            if sum(map(lambda r: r.state, self.cols(idx))) == 5:
                return True
        return False

    def score(self):
        return sum(map(lambda row: sum(map(lambda bn: 0 if bn.state else bn.num, row)), self.rows))


def get_numbers(line: []):
    return list(map(int, line.split(',')))


def get_boards(lines: []):
    boards = []

    start_idx = 0
    for idx in list(range(len(lines))):
        if lines[idx] == '' or idx == len(lines) - 1:
            end_idx = idx if idx != len(lines) - 1 else idx + 1
            boards.append(Board(lines[start_idx:end_idx]))
            start_idx = idx + 1

    return list(boards)


def get_winning_board(boards: []):
    for board in boards:
        if board.won:
            continue
        if board.is_winning():
            board.won = True
            yield board


def call_number(boards: [], number: int):
    for board in boards:
        board.mark(number)


def day4():
    with open('day4.txt') as data:
        lines = data.read().splitlines()
        boards = get_boards(lines[2:])
        numbers = get_numbers(lines[0])

        for number in numbers:
            call_number(boards, number)
            winning_boards = get_winning_board(boards)
            for winning_board in winning_boards:
                print('Winner!')
                print(winning_board)
                print(winning_board.score())
                print(winning_board.score() * number)


if __name__ == '__main__':
    day4()
