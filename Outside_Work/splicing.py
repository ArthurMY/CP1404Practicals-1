SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

name = "?name=Bob&age=99&day=Wed"

names = name.split("&")
for i in range(0, len(names)):
    names[i] = names[i].lstrip("?")
    names[i] = names[i].split("=")
    for j in range(0, len(names[i])):
        if names[i][j].isdigit():
            names[i][j] = int(names[i][j])
    names[i] = tuple(names[i])
print(names)