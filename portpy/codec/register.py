from __future__ import (absolute_import, print_function,
                        division, unicode_literals)

import codecs, encodings
from ..portpy import Language


try:
    # Python 2
    from cStringIO import StringIO
except ImportError:
    # Python 3
    from io import StringIO


def search_function(encoding):
    if 'portpy' not in encoding:
        return None
    splitted = encoding.split('-')
    lang = Language(splitted[-1] if len(splitted) > 1 else 'pt')

    # Assume utf8 encoding
    utf_8 = encodings.utf_8
    utf8 = encodings.search_function('utf8')

    def portpy_decode(input, errors='strict'):
        if isinstance(input, memoryview):
            input = input.tobytes()
        input = StringIO(input).read()
        return utf8.decode(lang.translate(input), errors)

    class PortpyIncrementalDecoder(utf_8.IncrementalDecoder):
        def decode(self, input, final=False):
            return super(PortpyIncrementalDecoder, self).decode(
                    lang.translate(input), final=final)

    class PortpyStreamReader(utf_8.StreamReader):
        def __init__(self, *args, **kwargs):
            codecs.StreamReader.__init__(self, *args, **kwargs)
            text = self.stream.read()
            self.stream = StringIO(lang.translate(text))

    return codecs.CodecInfo(
        name = 'portpy',
        encode = utf8.encode,
        decode = portpy_decode,
        incrementalencoder = utf8.incrementalencoder,
        incrementaldecoder = PortpyIncrementalDecoder,
        streamreader = PortpyStreamReader,
        streamwriter = utf8.streamwriter)


codecs.register(search_function)
