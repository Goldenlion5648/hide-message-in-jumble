from PIL import Image, ImageDraw, ImageFont

def write_text(text, save_loc_no_ext, x_offset=0, y_offset=0):
    # canvas size
    font_size =26
    fnt = ImageFont.truetype('arial', font_size)
    # fnt = ImageFont.load_default()
    # print("length", fnt.getsize("test123"))
    printed_size = fnt.getsize(text)
    # text_size = fnt.textlength(text)
    # print("text_size", text_size)
    # img = Image.new('RGB', (max((15+x_offset)*len(text), 56), int((font_size+y_offset) *1.2)), color=(255, 255, 255))
    offset = (2+x_offset*2, -3+y_offset*2)
    img = Image.new('RGB', (printed_size[0] + offset[0],
                            printed_size[1] + offset[1]), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    # x then y
    d.text(offset, text,
           font=fnt, fill=(0, 0, 0), spacing=5)
    # d.multiline_text((10,10), "Hello\nWorld", font=fnt, fill=(0, 0, 0))
    img.save(f'{save_loc_no_ext}.png')

# write_text("Cr")
