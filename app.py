import streamlit as st
import cv2
import numpy as np
from color_detector import extract_colors
from solver import solve_cube

st.title("Rubik's Cube Solver")

faces = ["U", "R", "F", "D", "L", "B"]

color_options = ["W", "R", "B", "G", "Y", "O"]

if "cube_state" not in st.session_state:
    st.session_state.cube_state = {}

face = st.selectbox("Select Cube Face", faces)

st.subheader("Capture Face")

camera = st.camera_input("Take a picture")

detected_colors = None

if camera is not None:

    file_bytes = camera.getvalue()
    npimg = np.frombuffer(file_bytes, np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    detected_colors = extract_colors(frame)

    st.write("Detected Colors:")
    st.write(detected_colors)

st.subheader("Manual Color Correction")

manual_colors = []

cols = st.columns(3)

for i in range(9):

    default = "W"

    if detected_colors and i < len(detected_colors):
        default = detected_colors[i]

    color = cols[i % 3].selectbox(
        f"Square {i+1}",
        color_options,
        index=color_options.index(default),
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
        st.error("Capture all 6 faces first")
    else:

        cube_string = ""

        order = ["U", "R", "F", "D", "L", "B"]

        for f in order:
            cube_string += st.session_state.cube_state[f]

        solution = solve_cube(cube_string)

        st.subheader("Solution")

        st.code(solution)