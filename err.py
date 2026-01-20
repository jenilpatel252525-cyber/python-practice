file = open('c1.py','w')

try:
    file.write("hello")

finally:
    file.close()

with open('1st.py','w') as file:
    file.write("hello")