from PIL import Image, ImageOps
import sys
format = [".jpg", ".jpeg", ".png"]
def check_valid_file(file):
    for i in format:
        if file.endswith(i):
            return True
    return False
def check_extension(file):
    for i in format:
        if file.endswith(i):
            return i
    return 1
if len(sys.argv) < 3:
    sys.exit("Too few command_line arguments")
if len(sys.argv) > 3:
    sys.exit("Too much command_line arguments")
if not check_valid_file(sys.argv[1]) or not check_valid_file(sys.argv[2]):
    sys.exit("Invalid input")
if check_extension(sys.argv[1]) != check_extension(sys.argv[2]):
    sys.exit("Input and output have different extensions")

try:
    image1 = Image.open(sys.argv[1])
    tocop = Image.open("shirt.png")

    size = tocop.size
    cut_image = ImageOps.fit(image1, size)
    cut_image.paste(tocop, tocop)

    cut_image.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
