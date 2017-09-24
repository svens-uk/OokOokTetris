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


code = "[-]" + "+"*33 + "."*12
code += "-"*23 + "."
for y in range(20):
    code += "+"*23 + "."
    code += ">" * y * 10
    for x in range(10):
        code += ">"
        copy(404-y*10-x)
        code += "<"*(204-y*10-x)
        move(204-y*10-x)
        code += ">"*(204-y*10-x)
        code += ".[-]"
        code += "<"*(404-y*10-x)
    code += "<"*10*(y + 1)
    code += "." + "-"*23 + "."
code += "+"*23 + "."*12
code += "-"*23 + "."
with open("graphics/render.b", "w") as file:
    file.write(code)