import barcode
from barcode.writer import ImageWriter
from IPython.display import Image as IPImage, display

barcode_format = barcode.get_barcode_class('ean13')
barcode_number = input('Enter a Barcode Number (12 digits): ')
barcode_image = barcode_format(barcode_number, writer=ImageWriter())
barcode_filename = 'barcode_image'
barcode_image.save(barcode_filename)
display(IPImage(filename=f'{barcode_filename}.png'))