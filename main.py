from panflute import *
import sys

headers = []


def pandoc_filter(elem, doc):
    if isinstance(elem, Header):
        if stringify(elem) in headers:
            sys.stderr.write(
                "Повторный заголовок: " + stringify(elem) + "\n")
        else:
            headers.append(stringify(elem))

    if type(elem) == Header:
        if elem.level <= 3:
            name = [Str(stringify(elem).upper())]
            return Header(*name, level=elem.level)

    if type(elem) == Str:
        if str(elem.text) == "BOLD":
            name = [Str(elem.text)]
            return Strong(*name)


def main(doc=None):
    return run_filter(pandoc_filter, doc=doc)


if __name__ == "__main__":
    main()
