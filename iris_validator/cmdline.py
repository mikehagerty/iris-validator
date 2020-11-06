import os
import re
import sys
import argparse

import logging as logger
logger.basicConfig(level=logger.WARN)

from iris_validator import stationxml_validator


def main():

    fname = 'iris-validator'

    args = process_cmd_line(fname)

    #TEST_DIR = "/Users/mth/mth/python_pkgs/stationxml-validator/src/test/resources/"
    # Let the helper function do it:
    #validate_stationxml_file_vs_rules(os.path.join(TEST_DIR, 'Validator_Pass.xml'))
    # Or, if you want to capture the validator errors/warnings yourself:
    #validator = stationxml_validator(os.path.join(TEST_DIR, 'Validator_Pass.xml'))

    validator = stationxml_validator(args.infile)

    validator.validate_inventory()
    print("[ERRORS]:\n")
    for msgs in validator.errors:
        for i, msg in enumerate(msgs):
            if i == 0:
                print(msg)
            else:
                print("%7s %s" % (' ', msg))
    print("\n[WARNINGS]:\n")
    for msgs in validator.warnings:
        for i, msg in enumerate(msgs):
            if i == 0:
                print(msg)
            else:
                print("%7s %s" % (' ', msg))
    return

def process_cmd_line(fname):

    parser = argparse.ArgumentParser()
    optional = parser._action_groups.pop()
    required = parser.add_argument_group("required arguments")

    parser._action_groups.append(optional) # 

    required.add_argument("--infile", type=str, metavar='// path-to StationXML file, e.g., --infile=/path/to/foo.xml',
                          required=True)
    #optional.add_argument("--preferred-eventtime", type=UTCDateTime)

    args, unknown = parser.parse_known_args()

    # Check that infile exists:
    if not os.path.isfile(args.infile):
        print("Unable to read infile=%s --> Exiting!" % args.infile)
        parser.print_help()
        exit(2)

    return args


if __name__ == "__main__":
    main()
