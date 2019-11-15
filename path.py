from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io

path = "scanned document.pdf"
pyocr_tools = pyocr.get_available_tools()[0]
language = pyocr_tools.get_available_languages()[0] # 0 for english

images_list = []
text_list = []

pdf_images = Image(filename = path,resolution = 500)
pdf_jpegs = pdf_images.convert('jpeg')

for image in pdf_jpegs.sequence:
    image_page = Image(image = image)
    images_list.append(image_page.make_blob('jpeg'))

pages_txt = ''
    
for image in images_list:
        pages_txt += pyocr_tools.image_to_string(PI.open(io.BytesIO(image)), \
                                        lang = language, \
                                        builder = pyocr.builders.TextBuilder())


print(pages_txt)
#print("".join(final_text))
print(len(pages_txt))
