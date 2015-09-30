from __future__ import (absolute_import, print_function,
                        division, unicode_literals)

import json
import os
import tokenize
from collections import OrderedDict
from pkg_resources import resource_string


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
    from sys import argv

    if len(argv) == 0:
        raise Exception(("Please provide the name of the language file."
                         "If the file is cz.txt, for example, than type "
                         "'cz example.py'."))

    args = argv[1:]

    lang_name = 'pt'
    if len(args) > 1:
        lang_name = args[0]
        args = args[1:]

    language = Language(lang_name)

    script_path = args[0]
    with open(script_path, 'rb') as _file:
        script = _file.read()

    script = language.translate(script)
    exec(script)

if __name__ == "__main__":
    main()
