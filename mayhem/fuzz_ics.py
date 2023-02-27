#!/usr/bin/env python3
import random

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=['ics']):
    from ics import Calendar

from ics.contentline import ParseError

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        Calendar(fdp.ConsumeRemainingString())
    except (ValueError, ParseError):
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
