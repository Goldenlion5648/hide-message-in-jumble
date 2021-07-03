from write_text_on_image import write_text
from convert_to_data import get_data
from disguise_letters_in_image import disguise, diguise_multiple
import random
# if __name__ == '__main__':
    # file = "from_main"
    # text = "SOLVE"
    # password = "python"
file = "multiple"
message = "this is cool right man"
message = "does this work?"
message = "the answer no"
filenames = []
random.seed(5648)
for i, word in enumerate(message.split()):
    cur = file+f"_{i}"
    # print(type(cur))
    x_off = random.randint(0+i*3, 7+i*3)
    y_off = random.randint(-1+i, 4+i)
    write_text(word, cur)
    # write_text(word, cur, x_off, y_off)
    get_data(cur)
    extended = cur + "_as_data.txt"
    filenames.append(extended)
diguise_multiple(filenames)
    # break
    # disguise(file, password)
# print("test")
