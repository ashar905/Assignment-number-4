source_file = "word.txt"
new_file = "new_file.txt"

with open(source_file,"r") as a:
    content = a.read()

with open(new_file,"w") as b:
    b.write(content)