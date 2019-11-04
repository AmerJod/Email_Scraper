import argparse
import os.path
import re

# Regular expressions. / need more work to cover/handle more cases
regex_rules1 = (
    "([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*(@|\s@\s|\/at\/|\sat\s|\[at\]"
    "|\s\(at\)\s|\s\[at\]\s|\s\(\sat\s\)\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|\s\.\s|\/dot\/|\[dot\]"
    "|\sdot\s|\s\(dot\)\s|\s\[dot\]\s)|\s\(\sdot\s\)\s)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"
)

regex_rules= r'(\w+|(\s\w)+)\s*(@|\Wat\W)\s*(\w+|(\w\s)+)\s*(\.|\Wdot\W)\s*((\w\s)+|\w+)'

regex = re.compile(regex_rules)


def _file_content_to_str(file_path):
    """
    Converts a file content to a string.
    Args:
        file_path (str): the path of the file.
    Return:
        str: file content as string
    """

    with open(file_path) as file:
        return file.read()


def get_emails(string):
    """
    Returns a list of emails as string separated by coma.
    Args:
        string (str): file content as string
    Return:
        str: list of emails as string
    """

    # convert it the full text to lower case to prevent regex mismatches.
    string = string.lower()

    list_of_emails = re.finditer(regex, string)

    # Remove the duplications
    unique_emails = list(dict.fromkeys([email[0] for email in list_of_emails]))
    print(f"({len(unique_emails)}) emails have been found.")

    return ", ".join(unique_emails)


if __name__ == "__main__":

    # create the parser
    parser = argparse.ArgumentParser(
        description="script for a finding all the email in file :)"
    )

    # add the argument
    parser.add_argument("path", metavar="path", type=str, help="the path to file")
    args = parser.parse_args()

    try:
        if os.path.isfile(args.path):
            file_content_as_string = _file_content_to_str(args.path)
            emails = get_emails(file_content_as_string)
            print(emails)
        else:
            raise Exception

    except Exception:
        print(f"args {args.path} is not a file or a valid path.")
        parser.print_usage()
