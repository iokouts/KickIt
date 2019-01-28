# image_formats.py
from wagtail.images.formats import Format, register_image_format

register_image_format(Format('center', 'Center', 'richtext-image center', 'width-800'))
