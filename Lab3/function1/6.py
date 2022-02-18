def f(st):
    for i in st:

        st1.append(i)

    return st1 

st = input().split()

st = []

st1 = []

for i in range(len(s)):
    st.append(s[i])
    
st.reverse()

print(*(f(st)))