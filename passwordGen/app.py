import random
import string
import streamlit as st

def generatePassword(passLen):
    # '''lets set the params for the password'''
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    symbol = string.punctuation

    # '''complete set of characters for the password to use'''
    passwordSetCharacters = lower + upper + number + symbol

    # '''
    # let me set some rules for the password
    # so a passwors must contain a digit an uppercase letter , a lowercase letter and a symbol
    # at least one of them has to be there for the password to be strong
    # '''

    password_chars=[]
    mendatory_rules=[random.choice(upper),random.choice(lower),random.choice(number),random.choice(symbol)]

    password_chars.extend(mendatory_rules)
    # print(password_chars)


    # '''creating remaining characters'''
    remaining_char=[]
    for i in range(passLen-4):
        password_chars.append(random.choice(passwordSetCharacters))

    random.shuffle(password_chars)
    password_chars=''.join(password_chars)
    return password_chars


# passLen=int(input('enter the password lenght'))
# print(generatePassword(passLen))


col1,col2=st.columns(2)

with col1:
    st.title('P@ssPop')
    st.markdown("**Create secure passwords with ease**")
    # text_area=st.empty()
    passlen=st.slider('Select Password Length',8,32)
    gen=st.button('generate')
    if gen:
        st.write('Generated password:')
        st.code(generatePassword(passlen))
        reset=st.button('reset')
        if reset:
            gen==False




with col2:
    st.image('bg.jpeg')

st.info('Developed By Raj Tadavi.')















