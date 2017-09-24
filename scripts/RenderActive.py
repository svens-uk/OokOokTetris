def move(offset):
    global code
    if offset > 0:
        code += "[-" + ">"*offset + "+" + "<"*offset + "]"
    else:
        code += "[-" + "<"*-offset + "+" + ">"*-offset + "]"


def moveXY(xOffset, yOffset):
    move(yOffset * 10 + xOffset)


def copy(offset):
    global code
    code += "[-" + ">"*offset + "+>+"
    code += "<"*(offset+1) + "]"
    code += ">"*(offset+1)
    move(-offset-1)
    code += "<"


# Start at 201.

code = ("+"*35 + ">")*3 + ">"*7
code += ">"+"+"*35+">"*9
code += ">"*10*18

code += ">>>"
copy(1)
code += "[<<<<"

for i in range(3):
    code += "<"*(200-i)
    move(200-i)
    code += ">"*(i*10 + 3-i)
    moveXY(i-3, i)
    code += ">"*((3-i)*10 - i)
    moveXY(i, i-3)
    code += "<"*(i*10 + 3-i)
    moveXY(3-i, i)
    code += ">"*(17+i)*10
    move((17+i)*-10)

code += "<"*189
move(189)
code += ">"
moveXY(-1, 0)
code += ">"*10
moveXY(0, -1)
code += "<"
moveXY(1, 0)
code += ">"*179
move(-179)

code += ">>>>-]"
code += "<<"
copy(2)
code += "[<<<<"+"+"*10+">>>>-]"
code += "<<<"
copy(3)
code += "[<<<<+>>>>-]<<<<"
code += "[<[-]" + "<[->+<]"*199 + ">"*200 + "-]"

# End at 401.

with open("graphics/renderActive.b", "w") as file:
    file.write(code)