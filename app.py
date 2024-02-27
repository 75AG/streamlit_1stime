

import streamlit as st

st.title ("Hello World")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
st.markdown("<h1 style= 'text-align :center;color:red;' > welcom to your application</h1>",unsafe_allow_html=True)
st.image("boss.jpeg", width=400,caption="Hi")
import pandas as pd
df=pd.read_csv('expected-years-of-living-with-disability-or-disease-burden.csv')
st.button('click')
st.button('predict')
st.button('submit')
st.table(df)
st.multiselect('chose a planet',['jupyter','mars','nepton'])
st.text_area('Description')
st.select_slider('Pick a mark',['Bad','Good','Excellent'])
st.slider('pick a number',0,50,step=10)
st.text_input('Email address')
num1=st.number_input('pick a number1',0,10)
num2=st.number_input('Pick a number2',0,10)
sum =num1+num2
st.write("sum",sum)
st.date_input('Travelling date')
st.time_input('school time')
st.file_uploader('upload a photo')
st.color_picker('choose your favorit color')

st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))
st.sidebar.title("this is the slider")
st.sidebar.header("header")
st.sidebar.button("button")
st.sidebar.checkbox("no")
st.sidebar.radio("pick your own gender:",['male','female'])
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#data = sns.load_dataset('iris')
#plot = sns.pairplot(data, hue='species')
#plot= plt.hist(data['sepal_length'])
#st.pyplot(plot)
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)

st.markdown("<h1 style='text-align: center; color:red;'>Matplotlib Figure</h1>",unsafe_allow_html=True)
st.pyplot(fig)



