import streamlit as st # for the web app
import pandas as pd # for the data processing
import seaborn as sns
from PIL import Image
st.write('''
        # Media Files
''')
st.write('''
## Image
''')
st.image(Image.open('istockphoto-521375354-612x612.jpg'))
st.write('''
### Video
''')
st.video(open('y2mate.com - Snow Leopards 101  Nat Geo Wild_v144P.mp4','rb'))
st.write('''
### Audio
''')
st.audio(open('Snow Leopard Chuffs with Inhale - QuickSounds.com.mp3','rb'))
