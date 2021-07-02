from write_text_on_image import write_text
from convert_to_data import get_data
from disguise_letters_in_image import disguise

if __name__ == '__main__':
    file = "from_main"
    text = "SOLVE"
    password = "python"
    write_text(text, file)
    get_data(file)
    disguise(file, password)
