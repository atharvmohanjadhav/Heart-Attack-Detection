import pandas as pd
import streamlit as st
df = pd.read_csv(r"Heart Attack.csv")
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["class"] = le.fit_transform(df["class"])

x = df.iloc[:,:-1]
y = df["class"]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()

dt.fit(x_train,y_train)

col1,col2,col3,col4 = st.columns(4)
with col1:
    age = st.selectbox("Select Age",sorted(df["age"].unique()))
with col2:
    gender = st.selectbox("Gender",[0,1])
with col3:
    impluse = st.selectbox("Impulse",sorted(df["impluse"].unique()))
with col4:
    pressurehight = st.selectbox("pressurehight",sorted(df["pressurehight"].unique()))
col5,col6 = st.columns(2)
with col5:
    pressurelow = st.selectbox("pressurelow",sorted(df["pressurelow"].unique()))
with col6:
    glucose = st.selectbox("glucose",sorted(df["glucose"].unique()))
col7,col8 = st.columns(2)
with col7:
    kcm = st.number_input("kcm")
with col8 :
    troponin = st.number_input("troponin")

if st.button("Check"):
    inp = [[age,	gender,	impluse,	pressurehight,	pressurelow,	glucose,	kcm,	troponin]]
    r = dt.predict(inp)
    if r == 0:
        st.header(":green[Positive]")
    else:
        st.header(":red[Negative]")


