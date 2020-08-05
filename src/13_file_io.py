"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt') as f:
    read_foo = f.read()
    print(read_foo)

# print(f.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

f = open("bar.txt", "w+")
f.write("Hi, I'm PJ \ni am cool \ni always want a nap")
f.close()

with open('bar.txt') as f:
    read_bar = f.read()
    print(read_bar)