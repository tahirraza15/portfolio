import streamlit as st

# Page settings
st.set_page_config(page_title="Tahir Raza Portfolio", page_icon="💻", layout="wide")

# Header
st.title("💻 Tahir Raza - Portfolio")
st.write("Welcome to my personal portfolio website")

# Navigation
menu = ["Home", "About", "Skills", "Projects", "Contact"]
choice = st.sidebar.selectbox("Navigation", menu)

# Home
if choice == "Home":
    st.header("Home")
    st.write("Hello! I am **Tahir Raza**.")
    st.write("I am a student of Embedded Systems (4th Sem) at University.")
    st.write("This portfolio showcases my skills, projects, and contact information.")

# About
elif choice == "About":
    st.header("ABOUT")
    st.write("""
**TAHIR RAZA**  
STUDENT OF EMBEDDED SYSTEM (4TH SEM) AT UNIVERSITY

Having had a keen interest in computers and IT from the start, I chose to specialize in Embedded Systems. This field is unique because it integrates both hardware and software components rather than focusing solely on programming.

**Email:** tahirbalti15@gmail.com
""")

# Skills
elif choice == "Skills":
    st.header("SKILLS")
    st.write("**Programming Languages:** C, C++, Python, Embedded C")
    st.write("**Microcontroller:** Arduino")
    st.write("**Circuit Design & Sensor Integration**")

# Projects
elif choice == "Projects":
    st.header("PROJECTS")
    st.subheader("FIREFIGHTER ROBOT")
    st.write("* Autonomous robot")
    st.write("* Language Used: Embedded C")
    st.write("* Technology Used: Arduino, Flame Sensor, Motor Driver, Ultrasonic Sensor")

# Contact
elif choice == "Contact":
    st.header("CONTACT")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")

    if st.button("Send"):
        st.success("Message sent successfully!")

    st.write("📧 Email: tahirbalti15@gmail.com")
    st.write("📱 Phone: +92 31234567")
    st.write("📍 Location: Skardu, Pakistan")