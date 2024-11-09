import sys
import random
from pyfiglet import Figlet
if len(sys.argv) == 3:
    figlet = Figlet()
    all_fonts = figlet.getFonts()
    if sys.argv[1] == '-f':
        if sys.argv[2] in all_fonts:
            figlet.setFont(font= sys.argv[2])
            text = input("Input: ")
            print(f"Output: {figlet.renderText(text)}")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    figlet = Figlet()
    fontchoice = random.choice(figlet.getFonts())
    figlet.setFont(font= fontchoice)
    text = input("Input: ")
    print(f"Output: {figlet.renderText(text)}")
else:
    sys.exit("Invalid usage")

