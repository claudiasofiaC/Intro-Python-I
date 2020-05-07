"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

f = open('foo.text', "r")
print(f.read())
f.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

text = [
    "I’m old, Gandalf.\n",
    "I know I don’t look it but I’m beginning to feel it in my heart.\n",
    "I feel thin… sort of stretched, like butter scraped over too much bread."
]

f = open('bar.txt', "w")
for line in text:
    f.write(line)
f.close()

f = open('bar.txt', "r")
print(f.read())    
