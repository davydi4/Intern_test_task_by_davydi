from json import dump
d = [{"cat": 'Сугроб'}, {"employee": 'Петя', "company": 'Foxford'}]
with open("data.json", "w") as file:
    dump(d, file, ensure_ascii=False)
