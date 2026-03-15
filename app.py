import streamlit as st
from solver import solve_cube

st.title("Rubik's Cube Solver")

faces = ["U", "R", "F", "D", "L", "B"]
colors = ["W", "R", "B", "G", "Y", "O"]

# Initialize session state
if "cube_state" not in st.session_state:
    st.session_state.cube_state = {}

face = st.selectbox("Select Cube Face", faces)

st.subheader(f"Enter colors for face: {face}")

manual_colors = []

# create 3x3 grid
cols = st.columns(3)

for i in range(9):
    color = cols[i % 3].selectbox(
        f"Square {i+1}",
        colors,
        key=f"{face}_{i}"
    )
    manual_colors.append(color)

if st.button("Save Face"):
    st.session_state.cube_state[face] = "".join(manual_colors)
    st.success(f"{face} face saved")

st.subheader("Current Cube State")
st.write(st.session_state.cube_state)

if st.button("Solve Cube"):

    if len(st.session_state.cube_state) != 6:
        st.error("Please enter all 6 faces first")
    else:

        cube_string = ""

        order = ["U", "R", "F", "D", "L", "B"]

        for f in order:
            cube_string += st.session_state.cube_state[f]

        solution = solve_cube(cube_string)

        st.subheader("Solution")
        st.code(solution)