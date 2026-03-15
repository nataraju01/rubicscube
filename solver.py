
import kociemba

def solve_cube(state):

    try:
        solution = kociemba.solve(state)
        return solution
    except:
        return "Invalid cube configuration"
