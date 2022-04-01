path = r"C:\Users\user\Desktop\pp2.lab\PP2_21B030907\lab6\dir and files\Files for 26 letters"
for i in range(65, 91): # all upper letters
    k = chr(i) + ".txt" 
    s = f"\{k}"
    with open(path + s, "w") as fil:
        fil.write("") # empty files
