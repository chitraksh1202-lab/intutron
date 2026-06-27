num=input("enter a number:")
freq={}
for ch in num:
    freq[ch]=freq.get(ch,0)+1
for k in freq:
    print(k,"occurs",freq[k],"times")