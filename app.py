import streamlit as st

def calculate_ibw(height, gender):
    if gender == 'Male':
        ibw = 50.0 + 2.3 * (height - 60)
    else:
        ibw = 45.5 + 2.3 * (height - 60)
    return ibw

# Set up the blue text box style
blue_text_box = """
<style>
    .blue-textbox {
        background-color: MediumSlateBlue;
        padding: 10px;
        border-radius: 5px;
    }
</style>
"""
midnight_blue_text_box = """
<style>
    .midnight-blue-textbox {
        background-color: MidnightBlue;
        padding: 10px;
        border-radius: 5px;
    }
</style>
"""

# Welcome message
st.title("Welcome to the Health Application")

st.success("This is a project to learn Streamlit")
st.info("This website will can tell Body Mass index and Ideal Body Weight")
st.markdown("Creator's [GitHub](https://github.com/srikta)")
# Sidebar options
option = st.sidebar.radio("Select Calculator", ["BMI CALCULATOR", "Ideal Body Weight Calculator"])

if option == "BMI CALCULATOR":
    # Body Mass Index (BMI) Calculator title
    st.header("Body Mass Index (BMI Calculator)")

    # Information messages
    st.info("Hello! This is a BODY MASS INDEX (BMI) calculator.")
    st.info('This tool will tell you whether you need to gain weight, lose weight, or maintain your current weight.')

    # Display the blue text box with the message
    st.markdown(blue_text_box, unsafe_allow_html=True)
    st.markdown('<div class="blue-textbox">Please fill up the required information</div>', unsafe_allow_html=True)

    # Requesting user input
    name = st.text_input("Name:")
    age = st.number_input("Age:", min_value=0,max_value=120, step=1, format="%d")  # Ensure age is an integer

    # Choose height unit
    height_unit = st.radio("Choose Feet or Meter:", ('Feet', 'Meter'))

    # If feet is selected, ask for height in feet and inches
    if height_unit == 'Feet':
        feet = st.number_input("Height in feet:", min_value=0, step=1, format="%d")  # Ensure height in feet is an integer
        inches = st.number_input("Inches:", min_value=0, step=1, format="%d")  # Ensure inches is an integer
        total_height_inches = feet * 12 + inches
        height = total_height_inches * 0.0254  # converting inches to meters
    # If meter is selected, ask for height in meters
    elif height_unit == 'Meter':
        height = st.number_input("Height in meters:", min_value=0.0, step=0.01, format="%f")  # Ensure height in meters is a float
    else:
        st.error("Invalid input for height unit. Please enter 'f' for feet or 'm' for meters.")
        st.stop()

    # Request weight input
    weight = st.number_input("Weight in kilograms:", min_value=0,max_value=1000,step=1, format="%d")  # Ensure weight is an integer

    # Button to trigger analysis
    if st.button("Analyze"):
        if height == 0 or weight == 0:  # Check if height or weight is zero
            st.error("Height and weight cannot be zero. Please provide valid values.")
        else:
            # Calculate BMI
            BMI = weight / (height ** 2)

            # Display BMI result in a midnight blue text box
            st.markdown(midnight_blue_text_box, unsafe_allow_html=True)
            st.markdown(f'<div class="midnight-blue-textbox">BMI: {BMI:.2f}</div>', unsafe_allow_html=True)

            # Interpret BMI
            st.write("Following the BMI calculation, the analysis is as follows:")
            if BMI <= 18.5:
                st.write("You are underweight. You should eat more to gain weight")
            elif 18.5 <= BMI < 25:
                st.write("You are of normal weight. Maintain your current weight")
            elif 25 <= BMI < 30:
                st.write("You are overweight. You should lose some weight through proper diet and exercise")
            else:
                st.write("You are obese. See your doctor on how to lose weight effectively")

            # Thank you message
            st.success(f"Thanks for using this app, {name}! Always strive to be healthy!")

elif option == "Ideal Body Weight Calculator":
    # Ideal Body Weight Calculator title
    st.header('Ideal Body Weight Calculator')

    height_unit = st.radio("Choose Feet or Meter:", ('Feet', 'Meter'))

    if height_unit == 'Feet':
        feet = st.number_input("Height in feet:", min_value=0, step=1, format="%d")  # Ensure height in feet is an integer
        inches = st.number_input("Inches:", min_value=0, step=1, format="%d")  # Ensure inches is an integer
        total_height_inches = feet * 12 + inches
        height = total_height_inches 

    elif height_unit == 'Meter':
        height = st.number_input("Height in meters:", min_value=0.0, step=0.01, format="%f")  # Ensure height in meters is a float
        height = height * 3.28084 * 12
    else:
        st.error("Invalid input for height unit.")
        st.stop()

    gender = st.radio("Select Gender: ", ('Male', 'Female'))

    if st.button('Analyze'):
        ibw = calculate_ibw(height, gender)
        st.info('Your ideal weight is: {:.2f} kg'.format(ibw))

    st.markdown("IBW Equation: [Source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4841935/)")
    st.markdown("Creator's [GitHub](https://github.com/srikta)")
