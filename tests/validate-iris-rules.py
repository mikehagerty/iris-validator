
from iris_validator import stationxml_validator
import os


def main():
    TEST_DIR = "/Users/mth/mth/python_pkgs/stationxml-validator/src/test/resources/"
    # Let the helper function do it:
    #validate_stationxml_file_vs_rules(os.path.join(TEST_DIR, 'Validator_Pass.xml'))

    # Or, if you want to capture the validator errors/warnings yourself:
    validator = stationxml_validator(os.path.join(TEST_DIR, 'Validator_Pass.xml'))
    #validator.validate_inventory()

    validator.validate_rule('402')

    print("[ERRORS]:\n")
    for error in validator.errors:
        print(error)
    print("\n[WARNINGS]:\n")
    for warning in validator.warnings:
        print(warning)

    return

if __name__ == "__main__":
    main()
