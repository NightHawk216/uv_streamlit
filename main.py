# turorial: error: https://github.com/data-sloth/uv-streamlit-setup/
import streamlit as st
from myproject.pkg2 import complex_fn

def main():
    st.header("Hello from uv-setup-example!")

    val1 = st.number_input('Value 1')
    val2 = st.number_input('Value 2')
    val3 = st.number_input('Value 3')

    st.write(f"The square of ({val1} - {val2}) is {complex_fn.square_of_diff(val1, val2)}!")
    st.write(f"The square of {val3} is {complex_fn.square_of_diff(val3,  0)}!")


if __name__ == "__main__":
    main()