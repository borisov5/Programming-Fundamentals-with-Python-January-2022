def data_types(type, text):
    if type == "int":
        return int(text) * 2
    elif type == "real":
        return f"{float(text) * 1.5:.2f}"
    elif type == "string":
        return f"${text}$"

data_type = input()
data = input()
print(data_types(data_type, data))
