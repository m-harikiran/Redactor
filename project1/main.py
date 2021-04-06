import argparse
import redactor
import os


def main(input_parameters):

    # Creating file to log redaction process
    redactor.statsFile(input_parameters.stats)

    # Reading the data from the input files
    docs_data = redactor.fetchDocs(input_parameters)

    # Redacting Phone numbers
    redact_phones = redactor.redactPhone(
        docs_data[0], input_parameters)

    # Redacting words related to gender
    redact_genders = redactor.redactGender(redact_phones, input_parameters)

    # Redacting Names
    redact_names = redactor.redactNames(redact_genders, args)

    # Redacting Dates
    redact_dates = redactor.redactDates(redact_names, args)

    # Redacting words with similar meaning
    redact_concept = redactor.redactConcept(redact_dates, args)

    print(args.concept, redact_concept)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # Creating an argument parser object
    parser.add_argument("--input", type=str, required=True, nargs="+", action="append",
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
    parser.add_argument("--concept", type=str, required=False, nargs="+", action="append",
                        help="Redact similar words to the given concept")  # Adding optinal argument --concept

    # Parsing the arguments to check if the condition if conditions is not met this will throw an error
    args = parser.parse_args()

    main(args)
