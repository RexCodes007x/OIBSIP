import streamlit as st

def bmiCal(h,w):
    try:
        res=round(w/(h/100)**2,2)
        if res<=18.5:
            health='Underweight'
        elif res<25 and res>18.5:
            health='Normal Weight'
        elif res<30 and res>=25:
            health='OverWeight'
        elif res<35 and res>=30:
            health='Obesity Class 1'
        elif res<40 and res>=35:
            health='Obesity Class 2'
        else:
            health='Obesity Class 3'


        return res,health

    except ZeroDivisionError:
        return 0,'Weight must be greater than 0'
    except ValueError:
        return 0,'Make sure you enter numeric values'


col1,col2=st.columns(2)
with col1:
    st.image("bg.jpeg")
with col2:
    st.title('FitStatus')
    st.header('A Simple way to know your BMI')
    w=st.number_input('Enter Your Weight In Kg')
    h=st.number_input('Enter Your Hieght In Cm')
    bmi,status=bmiCal(h,w)
    st.metric("Your BMI", bmi)
    if bmi==0:
        pass
    elif bmi<=25:
        st.success(f"Health Status: {status}")
    elif bmi>25 and bmi<=30:
        st.warning(f"Health Status: {status}")
    else:
        st.error(f"Health Status: {status}")


st.image('slider.jped')


st.info('developed by Raj. Mail me on - raiz99official@gmail.com')







