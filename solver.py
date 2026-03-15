from rubik_solver import utils


def solve_cube(state):

    try:
        solution = utils.solve(state, "Kociemba")

        moves = [str(m) for m in solution]

        return " ".join(moves)

    except Exception as e:
        return f"Invalid cube configuration: {e}"