# -*- coding: utf-8 -*-
"""streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y8Cf_LUuDqTywLpzuYo92_YSIUIZ30Qw
"""

!pip install streamlit

import streamlit as st
st.title('streamlit')

#input first,Second and third number
num1=int(input("Enter First Number"))
num2=int(input("Enter Second Number"))
num3=int(input("Enter Third Number"))
#Check if first number is greater than rest of the two numbers.
if (num1> num2 and num1> num3):
    print("The Largest number is", num1)
#Check if Second number is greater than rest of the two numbers.
elif (num2 > num1 and num2> num3):
    print ("The Largest number is", num2)
else:
    print ("The Largest number is", num3)



