# IRIS-validator 

iris-validator is a small python module for validation
stationxml files against the IRIS StationXML Validation Rules found at:
https://github.com/iris-edu/stationxml-validator/wiki/StationXML-Validation-Rule-List

It has a limited API and a command-line script


## Installation

### Requirements

    obspy >= 1.2

These requirements should be automatically installed for you (see below).

### Install

Clone the repository and install:

    >git clone https@gitlab.isti.com:mhagerty/iris-validator.git 
    >cd iris-validator
    >pip install .


### Usage:

Once you have installed it, you should be able to run it as a python module from any directory.

    >iris-validator

    usage: iris-validator [-h] --infile // path-to StationXML file, e.g., --infile=/path/to/foo.xml
    iris-validator: error: the following arguments are required: --infile

### API
To use the module from within your own python script, follow the example
below:

    from iris_validator import stationxml_validator

    validator = stationxml_validator('path/to/some/stationxml.xml')

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

Note some other things you can do include:

    validator.validate_rule('420')          // You can test your stationxml file against one rule at a time
