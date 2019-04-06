import copy
import pprint


def n_queens_brute_force(n):
    def is_valid(state):
        if (
            # All rows sum to one
            all(sum(row) <= 1 for row in state) and 
            # All columns sum to one
            all(sum(col) <= 1 for col in zip(*state))
        ):
            for i in range(n):
                # Check diagonal i below the principal diagonal
                if sum(row[j] for j, row in enumerate(state[i:])) > 1:
                    return False
                # Check diagonal i to the right of the principal diagonal
                if sum(row[j + i] for j, row in enumerate(state) if j + i < n) > 1:
                    return False

            flipped = [list(reversed(row)) for row in state]
            for i in range(n):
                # Check diagonal i below the principal diagonal
                if sum(row[j] for j, row in enumerate(flipped[i:])) > 1:
                    return False
                # Check diagonal i to the right of the principal diagonal
                if sum(row[j + i] for j, row in enumerate(flipped) if j + i < n) > 1:
                    return False

            return True

        return False

    def backtrack(state, i):
        for j in range(n):
            next_state = copy.deepcopy(state)
            next_state[i][j] = 1
            if is_valid(next_state):
                if i + 1 == n:
                    solutions.append(next_state)
                elif i + 1 < n:
                    backtrack(next_state, i + 1)

    solutions = []
    initial_state = [[0] * n for _ in range(n)]  # N x N board
    backtrack(initial_state, 0)
    return solutions


if __name__ == '__main__':
    pprint.pprint(n_queens_brute_force(1))
    pprint.pprint(n_queens_brute_force(2))
    pprint.pprint(n_queens_brute_force(3))
    pprint.pprint(n_queens_brute_force(4))
    pprint.pprint(n_queens_brute_force(5))
