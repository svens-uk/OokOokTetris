code = "<-"
code += ">" * 200
code += "+["
code += "+" * 33
code += "<+]"

code += "+"*33 + "."*12
code += "-"*23 + "."
for i in range(20):
    code += "+"*23 + "."
    code += ">"*i*10
    code += ">."*10
    code += "<"*10*(i + 1)
    code += "." + "-"*23 + "."
code += "+"*23 + "."*12
print(code)