# turorial: error: https://github.com/data-sloth/uv-streamlit-setup/
import streamlit as st
from myproject.pkg2 import complex_fn
import matplotlib.pyplot as plt

def main():
    st.header("Hello from uv-setup-example!")

    val1 = st.number_input('Value 1')
    val2 = st.number_input('Value 2')
    val3 = st.number_input('Value 3')

    st.write(f"The square of ({val1} - {val2}) is {complex_fn.square_of_diff(val1, val2)}!")
    st.write(f"The square of {val3} is {complex_fn.square_of_diff(val3,  0)}!")

    # Create a simple plot using val1 and val2
    fig, ax = plt.subplots()
    ax.plot([val1, val2], [val1**2, val2**2], marker='o', label='Squared Values')
    ax.set_title("Simple Plot of Squared Values")
    ax.set_xlabel("Input Values")
    ax.set_ylabel("Squared Values")
    ax.legend()

    # Display the plot in Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()