linkPath = "./links.txt"
links = []

with open(linkPath, 'r', encoding='utf-8') as file:
    lines = file.readlines()  

    for line in lines:
        links.append(line)

