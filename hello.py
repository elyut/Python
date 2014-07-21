# import modules used here -- sys is a very standard one
import sys

# Gather our code in the main function
def main():
    print "Hello there, ", sys.argv[1]
    # Command line arguemnts are found in sys.argv, argv[0] is the script name



if __name__ == "__main__":
	main()
else:
	print "Error"

# If a python file (module) is run directly (e.g. $ python hello.py Elliot), the special variable __name__
# is set to "__main__", so the statement if __name__ == "__main__": is used to make the main function
# execute only when the python module is run directly, opposed to being imported.

