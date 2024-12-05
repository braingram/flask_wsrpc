#!/usr/bin/env python

from base64 import b64encode
from io import BytesIO
import os

import numpy
from PIL import Image

import wsrpc


def image_to_string(im):
    im = Image.fromarray(im.astype('u1'))
    io = BytesIO()
    im.save(io, format='png')
    io.seek(0)
    return b64encode(io.read()).decode('ascii')


class Imager(object):
    def __init__(self):
        self.msg = ''
        self.i = 0

    def next_image(self):
        im = numpy.zeros((64, 64), dtype='u1') + self.i
        self.i += 10
        while self.i > 255:
            self.i -= 256
        s = image_to_string(im)
        return s


spec = {
    'object': Imager(),
    'name': 'imager',
    'static_folder': os.path.abspath('static'),
    'template_folder': os.path.abspath('templates'),
    'template': open('templates/imager.html', 'r').read(),
}
print(spec)
wsrpc.serve.register(spec)
wsrpc.serve.serve()
