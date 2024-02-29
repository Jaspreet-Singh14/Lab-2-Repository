import sys

def command_line_arguments():
    script_name = sys.argv[0]
    variables_used = sys.argv[1:]
    
    print("Script:", script_name)
    print("Variables used:", variables_used)
    print("Script and Variables:", script_name, variables_used)

command_line_arguments()

def helloWorld():
    print('Hello World')

helloWorld()
