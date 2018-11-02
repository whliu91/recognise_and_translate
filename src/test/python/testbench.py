import os, sys
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(SCRIPT_PATH, "..", "..")))
from main.python import utils

def main():
    image_path = os.path.join(SCRIPT_PATH, "..", "resources", "test.jpg")
    ret = utils.image_to_string(image_path)
    print(ret)

if __name__ == "__main__":
    main()