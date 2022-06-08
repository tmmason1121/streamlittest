import streamlit as st
from PIL import Image

cbellaimage = Image.open('cbella.jpg')
realtorimage = Image.open('realtor.gif')
profilepic = Image.open('profile_pic_thomas_mason.jpg')
st.set_page_config(page_title='Thomas Mason, Realtor', page_icon=':house:', layout='wide')


#style
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style/style.css')

st.header(' ', anchor='main')
st.write(' ')
st.write(' ')

#sidebar
with st.sidebar:
    st.markdown('[Main](#main)', unsafe_allow_html=True)
    st.markdown("[Services](#services)", unsafe_allow_html=True)
    st.markdown("[Contact Me](#contact-me)", unsafe_allow_html=True)
    st.markdown("[About Me](#about-me)", unsafe_allow_html=True)
    st.write('[C. Bella Realty](https://www.cbellarealty.com)')

#header
with st.container():
    left_column, center_column, right_column = st.columns((1,5,3))
    with left_column:
        st.write(' ')
        st.write(' ')
        st.image(cbellaimage)
        st.image(realtorimage)
    with center_column:
        st.title('Thomas Mason, Realtor')
        st.subheader('C. Bella Realty')
    with right_column:
        st.write(' ')
        st.write(' ')
        st.write('Cell: 508-364-4279')
        st.write('tmason@cbellarealty.com')

#services
st.write('---')
st.header('Services')
st.subheader('Buyers')
st.write('I love working with people to help them figure out what they want in a new home,and then to help them find it.  Whether first time home buyers testing the market, or those with plenty of past purchases that still require the guidance of a seasoned real estate agent.')
st.subheader('Sellers')
st.write('I have great experience in helping clients getting their home prepared for hitting the market, and achieving them great results in their sales.  Selling your home can be a very stressful and emotional experience, and I strive to bring sellers the best information possible on what to expect from the process.')
st.subheader('Builders')
st.write('At C. Bella Realty, we have an exceptional and aggressive listing program for the builders and developers that we work with.  Please reach out for details on this program and I am sure that you will choose C. Bella to list your builds in the future.')

#contact
st.write('---')
st.header('Contact Me')
contact_form = """
<form action="https://formsubmit.co/tmason@cbellarealty.com" method="POST">
    <input type='hidden' name='_captcha' value='false>
    <input type="text" name="name" placeholder='Your Name2' required>
    <input type="text" name="name" placeholder='Your Name' required>
    <input type="email" name="email" placeholder='Your Email' required>
    <textarea name='message' placeholder='Your Message' required></textarea>
    <button type="submit">Send</button>
</form>"""
st.markdown(contact_form, unsafe_allow_html=True)

#about
st.write('---')
st.header('About Me')
st.write('I have been serving the Greater Boston area with a diverse range of clients since 2013.   I work hard to put my clients’ interests first, and always steer them in the right direction during a transaction.  I pride myself on going above and beyond to ensure that my clients are protected, informed, comfortable, and successful during what can be a tumultuous time in their lives.  I hold a BS in Business Management with a Minor in Economics from Fitchburg State, and currently reside in Attleboro with his wife Alicia, and my two sons Jacob and Michael.')
with st.container():
    leftimagecolumn, centerimagecolumn, rightimagecolumn = st.columns((1,1,1))
    with leftimagecolumn:
        st.write(' ')
    with centerimagecolumn:
        st.image(profilepic, width=300)
    with rightimagecolumn:
        st.write(' ')