"""This module contains a function that creates the streamlit window for the 
application."""

from src.code_generator import create_parameters
from src.map import chaotic_map
from src.prbg import PRBG


import streamlit as st

characters_keys = {
    "exclamation": "!",
    "at": "@",
    "hash": "#",
    "dollar": "$",
    "percent": "%",
    "caret": "^",
    "ampersand": "&",
    "numbers": "0123456789",
    "asterisk": "*",
    "parentheses": "()",
    "dash": "-",
    "underscore": "_",
    "plus": "+",
    "equals": "=",
    "semicolon": ";",
    "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "colon": ":",
    "period": ".",
    "angle_brackets": "<>",
    "comma": ",",
    "forward_slash": "/",
    "question_mark": "?",
    "space": " ",
    "lowercase": "abcdefghijklmnopqrstuvwxyz"
}

def create_window():
    """This function creates the streamlit window for the application."""
    st.title("Chaotic Password Generator")


    # Create a field where the user enters a username
    st.text_input(
        "Username", 
        key="username"
    )

    st.text_input(
        "Platform", 
        key="platform"
    )

    st.text_input(
        "Favorite Animal", 
        key="favorite_animal"
    )

    st.text_input(
        "Mother's Family Name", 
        key="mother_family_name"
    )

    st.text_input(
        "First Teacher's Name",
        key="first_teacher_name"
    )

    st.number_input(
        "Number of Digits",
        min_value=6,
        max_value=100,
        value=8,
        step=1,
        key="number_of_digits"
    )

    # Add an extendable section with the different types of characters that can 
    # be included in the password. Each character is a checkbox.
    with st.expander("Character Types"):
        # Create a 3 by 8 grid of checkboxes
        # The first row is for !, @, #, $, %, ^, &, and 0-9
        # The second row is for *, (), -, _, +, =, ; and A-Z
        # The third row is for :, ., <>, ,, /, ?, 'space' and a-z

        first_row = st.columns(8)
        second_row = st.columns(8)
        third_row = st.columns(8)

        # Create a checkbox for each character
        first_row[0].checkbox("!", key="exclamation", value=True)
        first_row[1].checkbox("@", key="at", value=True)
        first_row[2].checkbox("\#", key="hash", value=True)
        first_row[3].checkbox("$", key="dollar", value=True)
        first_row[4].checkbox("%", key="percent", value=True)
        first_row[5].checkbox("^", key="caret", value=True)
        first_row[6].checkbox("&", key="ampersand", value=True)
        first_row[7].checkbox("0-9", key="numbers", value=True)

        second_row[0].checkbox("\*", key="asterisk", value=True)
        second_row[1].checkbox("()", key="parentheses", value=True)
        second_row[2].checkbox("\-", key="dash", value=True)
        second_row[3].checkbox("_", key="underscore", value=True)
        second_row[4].checkbox("\+", key="plus", value=True)
        second_row[5].checkbox("=", key="equals", value=True)
        second_row[6].checkbox(";", key="semicolon", value=True)
        second_row[7].checkbox("A-Z", key="uppercase", value=True)

        third_row[0].checkbox(":", key="colon", value=True)
        third_row[1].checkbox(".", key="period", value=True)
        third_row[2].checkbox("<>", key="angle_brackets", value=True)
        third_row[3].checkbox(",", key="comma", value=True)
        third_row[4].checkbox("/", key="forward_slash", value=True)
        third_row[5].checkbox("?", key="question_mark", value=True)
        third_row[6].checkbox("space", key="space", value=True)
        third_row[7].checkbox("a-z", key="lowercase", value=True)


    if st.button("Generate Password"):
        password = generate_password()
        
        # Create a field where the user can see the generated password
        # but not edit it
        st.text_input(
            "Password",
            value=password,
            key="password",
            disabled=True
        )


def collect_user_input() -> dict:
    """This function collects the user input from the streamlit window."""
    
    user_input = {
        "username": st.session_state.username,
        "platform": st.session_state.platform,
        "favorite_animal": st.session_state.favorite_animal,
        "mother_family_name": st.session_state.mother_family_name,
        "first_teacher_name": st.session_state.first_teacher_name,
        "number_of_digits": st.session_state.number_of_digits,
    }

    return user_input


def get_admissible_characters() -> str:
    """This function returns a string containing all the characters that the 
    user has selected."""

    admissible_characters = ""

    for key, value in st.session_state.items():
        if value and key in characters_keys:
            admissible_characters += characters_keys[key]

    return admissible_characters

def get_admissible_ascii_codes() -> list:
    """This function returns a list containing all the ascii codes of the 
    characters that the user has selected."""

    admissible_characters = get_admissible_characters()
    admissible_ascii_codes = [ord(character) for character in admissible_characters]

    return admissible_ascii_codes


def generate_password():
    """Generates the password"""

    user_input = collect_user_input()
    parameters = create_parameters(user_input)

    init_1 = (parameters["x0"], parameters["y0"])
    init_2 = (parameters["x1"], parameters["y1"])

    map_pameters_1 = (parameters["a1"], parameters["b1"], parameters["Z1"])
    map_pameters_2 = (parameters["a2"], parameters["b2"], parameters["Z2"])

    # Skip the first 100 points for each map
    for _ in range(100):
        init_1 = chaotic_map.next_point(init_1, map_pameters_1)
        init_2 = chaotic_map.next_point(init_2, map_pameters_2)

    characters = get_admissible_characters()

    acceptable_ascii_codes = get_admissible_ascii_codes()

    password = ""
    while len(password) < user_input["number_of_digits"]:
        init_1 = chaotic_map.next_point(init_1, map_pameters_1)
        init_2 = chaotic_map.next_point(init_2, map_pameters_2)

        random_integer = PRBG(init_1[1], init_2[1])
        if random_integer in acceptable_ascii_codes:
            password += chr(random_integer)
    
    return password

