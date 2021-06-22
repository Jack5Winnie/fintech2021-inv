# libraries
import streamlit as st
import qr_maker

st.title('Create Your Own QR Code')

# (1) Type in your hyperlink for your QR code
hyper_link  = st.text_input("Type in your hyperline for QR code such as:", "https://engineering.catholic.edu/eecs/index.html")
st.write("Test your link first:", hyper_link)

# (2) User's input: QR Code Size (inches)
qr_size = st.slider('Slide me', min_value = 6, max_value = 12, value = 6)
st.write("Your code size is", qr_size)

## (3.1) without logo
qr_name = qr_maker.qr_code(link=hyper_link, logo=False, size=qr_size)
st.image(qr_name, caption='Your QR.png')

# (3.2) without logo
# User's logo: upload the logo image(png, jpg types)
st.title('Add your personal Logo? ')
logo_file = st.file_uploader("click the botton to upload a picture", type=['png','jpeg','jpg'])
if logo_file:
    st.write("logo name", logo_file.name)
    open("./images/logo.png", "wb").write(logo_file.getbuffer())

    qr_name = qr_maker.qr_code(link=hyper_link, logo=True,  size=qr_size)
    st.image(qr_name, caption='Your QR-Logo.png')

st.title(" Enjoy! ")