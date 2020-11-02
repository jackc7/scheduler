import readchar

space = 0
m = 0
while True:
    print("\033c", space, m)
    char = readchar.readkey()
    if char == " ":
        m+=1
    elif char == "m":
        space+=1
        