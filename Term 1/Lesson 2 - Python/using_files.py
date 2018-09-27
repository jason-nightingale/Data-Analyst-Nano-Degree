"""You can open files with the open() function, if There
isn't a file, python will create one. 'r' is for read,
'w' os for write"""
f = open('test_file.txt', 'w')
f.write('Hello World')
f.close() # always close the file when done to free up resources

"""reading a file"""
f = open('test_file.txt', 'r')
file_data = f.read()
f.close()
print(file_data)

#reading a file with and auto close, do anything inside the 'with' block
with open('test_file.txt', 'r') as f:
    file_data = f.read()
"""in the .read() above you can give it a character count
.read(34) and will read up to that point and remain
there until ready to read again from that position in the
file

you can use .readline() to read entire lines to the \n
"""
print(file_data)
#creating a list by looping over lines in a files
camelot_lines = []
with open('camelot.txt') as f:
    for line in f:
        camelot_lines.append(line.strip())
print(camelot_lines)
#example output:
#["We're the knights of the round table", "We dance whenever we're able"]
