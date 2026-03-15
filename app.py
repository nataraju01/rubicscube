
import streamlit as st
import cv2
from color_detector import extract_colors
from solver import solve_cube
import numpy as np

st.title("Rubik's Cube AI Solver")

st.write("Capture each face of the cube")

faces = ["U","R","F","D","L","B"]

if "cube_state" not in st.session_state:
    st.session_state.cube_state = {}

face = st.selectbox("Select Face", faces)

camera = st.camera_input("Take a picture")

if camera is not None:

    file_bytes = camera.getvalue()

    npimg = np.frombuffer(file_bytes, np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    colors = extract_colors(frame)

    st.write("Detected colors:", colors)

    if st.button("Save Face"):
        st.session_state.cube_state[face] = "".join(colors)
        st.success(f"{face} face saved")


st.write("Current cube data")
st.write(st.session_state.cube_state)


if st.button("Solve Cube"):

    if len(st.session_state.cube_state) != 6:
        st.error("Capture all 6 faces first")
    else:

        cube_string = ""

        order = ["U","R","F","D","L","B"]

        for f in order:
            cube_string += st.session_state.cube_state[f]

        solution = solve_cube(cube_string)

        st.subheader("Solution")
        st.write(solution)
