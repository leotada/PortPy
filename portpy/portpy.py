from __future__ import (absolute_import, print_function,
                        division, unicode_literals)

import sys
import json
import os
import tokenize
import argparse
from collections import OrderedDict
from pkg_resources import resource_string
from .cross_version import run


DEFAULT_LANGUAGE_PATH = "lang"


class Language(object):

    def __init__(self, name):
        filename = os.path.join(DEFAULT_LANGUAGE_PATH, name + ".txt")
        content = resource_string(__name__, filename).decode('utf8')
        self.data = json.loads(content, object_pairs_hook=OrderedDict)
        self.name = name
        self.data = OrderedDict(
            (key.encode('utf8'),[v.encode('utf8') for v in values])
            for key, values in self.data.items())

    def translate(self, script):
        for keyword, translations in self.data.items():
            for translation in translations:
                script = script.replace(translation, keyword)

        return script


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--language', nargs=1, default='pt')
    parser.add_argument('script', nargs=argparse.REMAINDER)

    args = parser.parse_args()

    language = Language(''.join(args.language))

    path = os.path.realpath(args.script[0])
    sys.path[0] = os.path.dirname(path)
    sys.argv = args.script

    import __main__
    __main__.__dict__.clear()
    __main__.__dict__.update({'__name__'    : '__main__',
                              '__file__'    : path,
                              '__builtins__': __builtins__,
                             })

    with open(path, 'rb') as _file:
        script = _file.read()

    script = language.translate(script)
    run(script)


if __name__ == "__main__":
    main()
