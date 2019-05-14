from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, his CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# we don't need to truncate because opening with 'w' does this for us
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write("%r\n%r\n%r\n" % (line1, line2, line3))
target.close()

readable = open(filename, "r")
print("Let me read that back...")
print(readable.read())
print("That was neat!")

print("And finally, we close it.")
readable.close()