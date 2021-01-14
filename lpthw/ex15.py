from sys import argv

# parses information from being run from command line, first is script name second is name of file to read
script, filename = argv

# open the file specified in variable filename
txt = open(filename)

# print contents of file
print(f"Here's your file {filename}:")
print(txt.read())

txt.close()

# get filename again
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()