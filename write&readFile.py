file = open("sample.txt", "w")
file.write("Hello, this is a sample file>\n")
file.close()
file = open("sample.txt", "r")
content = file.read()
print("File content:\n", content)
print(content)
file.close()