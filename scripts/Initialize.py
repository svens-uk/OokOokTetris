code = "-"
code += ">" * 200
code += "+["
code += "+" * 33
code += "<+]"

with open("initialize.b", "w") as file:
    file.write(code)