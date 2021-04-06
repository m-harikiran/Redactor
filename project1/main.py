import argparse
import redactor
import os


def main(input_parameters):
    # print(input_parameters)
    redactor.statsFile(input_parameters.stats)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # Creating an argument parser object
    parser.add_argument("--input", type=str, required=True, nargs="*", action="append",
                        help="Names of files to be redacted")  # Adding optinal argument --inputs
    parser.add_argument("--names", required=False, action="store_true",
                        help="Specify to redact names present in the documents")  # Adding optinal argument --names
    parser.add_argument("--dates", required=False, action="store_true",
                        help="Specify to redact dates present in the documents")  # Adding optinal argument --dates
    parser.add_argument("--phones", required=False, action="store_true",
                        help="Specify to redact phone numbers present in the documents")  # Adding optinal argument --phones
    parser.add_argument("--genders", required=False, action="store_true",
                        help="Specify to redact genders present in the documents")  # Adding optinal argument --genders
    parser.add_argument("--output", type=str, required=False, default="redacted_documents",
                        help="Path to store redacted documents")  # Adding optinal argument --output
    parser.add_argument("--stats", type=str, required=False, default="stdout",
                        help="Name of the status file")  # Adding optinal argument --stats

    # Parsing the arguments to check if the condition if conditions is not met this will throw an error
    args = parser.parse_args()

    main(args)
