import os, sys
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(SCRIPT_PATH, "..", "..")))
from main.python import utils

def main():
    image_path = os.path.join(SCRIPT_PATH, "..", "resources", "test.jpg")
    eng = utils.image_to_string(image_path)
    eng_list = [x.replace(" ", "") for x in eng.split("\n")]
    filtered_eng_list = [x for x in eng_list if x]
    for item in filtered_eng_list:
        ret = utils.eng_to_zhcn(item)
        print("translate result: \n{fromstr}\n{tostr}\n".format(fromstr=item, tostr=ret))

if __name__ == "__main__":
    main()