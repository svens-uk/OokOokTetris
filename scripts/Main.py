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


code = "-"
code += ">" * 200
code += "+["
code += "+" * 33
code += "<+]"

code += ">"*402
code += "+++"
code += "<"*201
code += "{{graphics/renderActive}}"
code += "<"*401
code += "{{graphics/render}}"

code += "<+["
code += ">"*404
code += "-"*18 + "["
move(2)
code += ">>+<<]"
code += "+"*18
code += ">>"
move(-2)
code += "<"*204
code += "{{graphics/renderActive}}"
code += "<"*401
code += "{{graphics/render}}"
code += "<]"

with open("main.b", "w") as file:
    file.write(code)