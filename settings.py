from os import system


import pyfiglet

def clear():
    system("clear")


# break line
def break_line(dashes):
    print('-' * dashes)


class banner:
    def __init__(self, name, header, message):
        self.name = name
        self.header = header
        self.message = message
        self.display = pyfiglet.print_figlet(title)


title = 'Python Scanner'
description = 'Python Scanner is a simple port scanning application written in python'


ban = banner('Main Banner', title, description)









