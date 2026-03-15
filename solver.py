import kociemba

def solve_cube(state):
    try:
        solution = kociemba.solve(state)
        return solution
    except Exception as e:
        return f"Invalid cube configuration: {e}"