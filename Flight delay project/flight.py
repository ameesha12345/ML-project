import streamlit as st
import pickle
from PIL import Image

def set_bg_hack_url(url):
    st.markdown(
        f"""
         <style>
        .stApp {{
             background: url({url});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


def flight():
    tabs = ["Home", "Predict", "About"]
    tabs = st.sidebar.selectbox("Navigation", tabs)
    if tabs=="Home":
        set_bg_hack_url("https://w0.peakpx.com/wallpaper/894/165/HD-wallpaper-airplane-flying-over-beach-shore-sunset-airplane-planes-sunset-beach-shore-graphy.jpg")
        st.title(" AIRPLANE DELAY PREDICTION")

        st.write("WELCOME TO AIRPLANE DELAY PREDICTION APP")
        st.write("This app predicts the delay of an airplane based on various factors. Choose your flight accordingly.")
    elif tabs=="Predict":
        #set_bg_hack_url("https://img.freepik.com/free-photo/top-view-airplane-with-copy-space_23-2148608798.jpg?w=740&t=st=1719836977~exp=1719837577~hmac=6a30746e4ed793241f4964e3ae5a73312909e6f93bb3ea6bfaef557babd602b5")
        model=pickle.load(open("Airline_delay.sav","rb"))
        scaled=pickle.load(open("minmax.sav","rb"))

        st.header("PLEASE ENTER FLIGHT DETAILS")
        arr_flights=st.text_input("Number_of_arriving_flights","")
        carrier_ct=st.text_input("Carrier_count","")
        weather_ct=st.text_input("Weather_count","")
        nas_ct=st.text_input("NAS_count","")
        security_ct=st.text_input("Security_count","")
        late_aircraft_ct=st.text_input("Late_aircraft_count","")
        arr_cancelled=st.text_input("Number_of_flights_canceled","")
        arr_diverted=st.text_input("Number_of_flights_diverted","")
        arr_delay=st.text_input("Total_arrival_delay","")
        carrier_delay=st.text_input("Delay_attributed_to_the_carrier","")
        weather_delay=st.text_input("weather_delayDelay_attributed_to_weather","")
        nas_delay=st.text_input("Delay_attributed_to_the_NAS","")
        security_delay=st.text_input("Delay_attributed_to_security","")
        late_aircraft_delay=st.text_input("Delay_attributed_to_late_aircraft_arrival","")
        pred=st.button("PREDICT")
        if pred:
            try:
                prediction=model.predict(scaled.transform([[float(arr_flights),float(carrier_ct),float(weather_ct),float(nas_ct),float(security_ct),float(late_aircraft_ct),float(arr_cancelled),float(arr_diverted),float(arr_delay),float(carrier_delay),float(weather_delay),float(nas_delay),float(security_delay),float(late_aircraft_delay)]]))[0]
                minutes,second=divmod(prediction,1)
                minutes=int(minutes)
                second=int(round(second*60))
                st.write(f"The predicted delay is {minutes} Minute(s) {second} Second(s)")
            except ValueError:
                st.error("Invalid input values. Please enter numeric values only.")


    elif tabs=="About":
                image = Image.open("thank you.jpg")
                st.image(image, width=600)
                st.write("This app was developed by AMEESHA LAL.")
                st.write("The model was trained on a dataset of Flight Delay Data .")
                st.write("Link to my Colab Notebook : https://colab.research.google.com/drive/15_H4ravEuao7R4mH2NuAetr_rbXFnONg?usp=sharing")


flight()