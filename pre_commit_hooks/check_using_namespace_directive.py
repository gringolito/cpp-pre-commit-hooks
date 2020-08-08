# -*- coding: utf-8 -*-
import argparse
import re
import sys
from typing import Optional, Sequence

USING_DIRECTIVE = b"using namespace "
HEADER_FILES = r"\.(h|hh|hpp|hxx)$"


def _is_header_file(filename):
    return re.search(HEADER_FILES, filename) is not None


def main(argv: Optional[Sequence[str]] = None) -> int:
    """
    Check for `using namespace` directive on C++ files
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    parser.add_argument("--allow-in-source", action="store_true")
    args = parser.parse_args(argv)

    retcode = 0
    for filename in args.filenames:
        is_header = _is_header_file(filename)
        if not is_header and args.allow_in_source:
            continue

        with open(filename, "rb") as inputfile:
            for i, line in enumerate(inputfile):
                if USING_DIRECTIVE in line:
                    error_string = f"Directive using namespace found in {filename}:{i + 1} "
                    if is_header:
                        error_string += "and is forbidden in header files."
                    else:
                        error_string += "and is forbidden by Google C++ Style Guide."

                    print(error_string)
                    retcode = 1

    return retcode


if __name__ == "__main__":
    sys.exit(main())
