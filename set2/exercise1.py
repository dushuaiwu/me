"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ["what", "does", "this", "line", "do", "?"]
# i think this will print what does this line do ?
for word in some_words:
    print(word)
# i think this will print what does this line do ?
for x in some_words:
    print(x)
# i think this will print [" what" "does" "this" "line" "do" "?"] by calling the print function.
print(some_words)
# i think this will print "some_words contains more than 3 words"by calling the print function
if len(some_words) > 3:
    print("some_words contains more than 3 words")

# i think this will print my system name and some details by calling the print function
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
