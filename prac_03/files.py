OUTPUT_FILE = "name.txt"

out_file = open(OUTPUT_FILE, 'w')

name = input("Input name: ")
print(name, file=out_file)

out_file.close()