import sys
from src import imageparser


if __name__ == "__main__":
    working_directory = sys.argv[1]
    image_parser = imageparser.ImageParser(working_directory)
    image_parser.get_image()
