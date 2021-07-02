from write_text_on_image import write_text
from convert_to_data import get_data
from disguise_letters_in_image import disguise, diguise_multiple
import random
# if __name__ == '__main__':
    # file = "from_main"
    # text = "SOLVE"
    # password = "python"
file = "multiple"
message = "does this work?"
message = "this is all the same"
filenames = []
random.seed(5648)
for i, word in enumerate(message.split()):
    cur = file+f"_{i}"
    # print(type(cur))
    write_text(word, cur)
    get_data(cur)
    extended = cur + "_as_data.txt"
    filenames.append(extended)
diguise_multiple(filenames, message, num_letters_per=2)
    # break
    # disguise(file, password)
# print("test")
