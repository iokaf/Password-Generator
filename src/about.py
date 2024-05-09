import streamlit as st

def about():
    st.markdown("# Chaotic Password Generator")
    st.write("This is a password generator that uses a chaotic map to generate a password.")
    st.write("The method was proposed in the paper")
    st.markdown("[\"A 1D coupled hyperbolic tangent chaotic map with delay and its application to password generation\"](https://link.springer.com/article/10.1007/s11042-022-13657-7)")
    
    # Add this as citation Kafetzis, I., Moysis, L., Tutueva, A., Butusov, D., Nistazakis, H., & Volos, C. (2023). A 1D coupled hyperbolic tangent chaotic map with delay and its application to password generation. Multimedia Tools and Applications, 82(6), 9303-9322.
    st.markdown("## Citation")
    st.write("Kafetzis, I., Moysis, L., Tutueva, A., Butusov, D., Nistazakis, H., & Volos, C. (2023). A 1D coupled hyperbolic tangent chaotic map with delay and its application to password generation. Multimedia Tools and Applications, 82(6), 9303-9322.") 
    

    st.markdown("## Developed by:")
    st.write("Dr. Ioannis Kafezis, ioanniskaf@gmail.com")


    st.markdown("## How to use")
    st.write("1. Choose the user name for which the password is generated.")
    st.write("2. Chose the platform for which the password is generated.")
    st.write("3. Add the answer to the security questions.")
    st.write("4. Select the length of the password.")
    st.write("5. Select characters to be included in the password.")
    st.write("6. Click the button to generate the password.")

    st.markdown("## Disclaimers:")
    st.write("The password generated is not stored.")
    st.write("The password generated is not transmitted to any server.")
    st.write("The password generated is not shared with any third party.")
    st.write("The password generated is not used for any other purpose than the one intended.")
    st.write("This is a proof of concept and should not be used to generate passwords for sensitive applications.")
    st.write("The results might vary from the ones presented in the paper due to implementation.")


