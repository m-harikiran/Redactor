import argparse
import os
from project1 import redactor


# Testing creation of status file


def testStatusFile():

    # Calling the method to create testlog file
    redactor.statsFile('../test_project/testLog')

    # Verifying if the testlog file is created or not
    assert os.path.isfile('project_docs/test_project/testlog')


# Testing the method used to updated status log

def testUpdateStatusLog():
    # Message to be writted to status log
    message = 'Testing status updating method'

    # Updating the status log
    redactor.updateStatusLog(message, '../test_project/testLog')

    assert open(
        'project_docs/test_project/testlog').read().splitlines()[-1] == message  # Verifying the updated message

# Testing the method used to write data to redacted files


def testRedactedDoc():

    # Data to writted in redacted file and it's name
    message = ('\u2588 Testing redactedDoc method \u2588', 'test')

    redactor.redactedDoc(message, 'test_project')  # Calling method redactedDoc

    # Verifying if the file with .redacted extension id created or not
    assert os.path.isfile('project_docs/test_project/test.redacted')

    assert open(
        'project_docs/test_project/test.redacted').read().splitlines()[-1] == message[0]  # Verifying the contents of the redacted file


# Testing the method to fetch or read data from the input files.

def testFetchDocs():
    parser = argparse.ArgumentParser()  # Creating an argument parser object
    # Adding optinal argument --inputs
    parser.add_argument("--input", type=str, required=True,
                        nargs="+", action="append")
    parser.add_argument("--stats", type=str, required=False,
                        default="stdout")  # Adding optinal argument --stats
    args = parser.parse_args(
        "--input ../tests/test.txt --stats ../test_project/testLog".split())

    # Calling the method to fetch data from documents
    global data
    data = redactor.fetchDocs(args)

    # Verifying if the the return type of method is list or not
    assert type(data) == list
    assert len(data[0][0]) > 1  # Verifying if the read file has data
    # Verifying the name of the file from which data is read
    assert data[0][1] == 'test'

# Testing the method used to redact Names


def testRedactNames():
    parser = argparse.ArgumentParser()  # Creating an argument parser object
    parser.add_argument("--names", required=False, action="store_true")
    parser.add_argument("--stats", type=str, required=False,
                        default="stdout")  # Adding optinal argument --stats
    args = parser.parse_args(
        "--names --stats ../test_project/testLog".split())

    redactor.redactNames(data[0][0], args)

    # log file must be updated with this message as there are 9 names to be redacted in test document
    expected = 'Sucessfully redacted 9 Names'

    assert open(
        'project_docs/test_project/testLog').read().splitlines()[-1] == expected  # Verifying the contents of the log file w.r.t expected

# Testing the method used to redact Phone Numbers


def testRedactPhones():
    parser = argparse.ArgumentParser()  # Creating an argument parser object
    parser.add_argument("--phones", required=False, action="store_true")
    parser.add_argument("--stats", type=str, required=False,
                        default="stdout")  # Adding optinal argument --stats
    args = parser.parse_args(
        "--phones --stats ../test_project/testLog".split())

    redactor.redactPhone(data[0][0], args)

    # log file must be updated with this message as there are 8 numbers to be redacted in test document
    expected = 'Sucessfully redacted 8 phone numbers'

    assert open(
        'project_docs/test_project/testLog').read().splitlines()[-1] == expected  # Verifying the contents of the log file w.r.t expected


# Testing the method used to redact gender related words

def testRedactGenders():
    parser = argparse.ArgumentParser()  # Creating an argument parser object
    parser.add_argument("--genders", required=False, action="store_true")
    parser.add_argument("--stats", type=str, required=False,
                        default="stdout")  # Adding optinal argument --stats
    args = parser.parse_args(
        "--genders --stats ../test_project/testLog".split())

    redactor.redactGender(data[0][0], args)

    # log file must be updated with this message as there are 17 words related to gender in test document
    expected = 'Sucessfully redacted 17 words related to gender identity'

    assert open(
        'project_docs/test_project/testLog').read().splitlines()[-1] == expected  # Verifying the contents of the log file w.r.t expected


# Testing the method used to redact dates

def testRedactDates():
    parser = argparse.ArgumentParser()  # Creating an argument parser object
    parser.add_argument("--dates", required=False, action="store_true")
    parser.add_argument("--stats", type=str, required=False,
                        default="stdout")  # Adding optinal argument --stats
    args = parser.parse_args(
        "--dates --stats ../test_project/testLog".split())

    redactor.redactDates(data[0][0], args)

    # log file must be updated with this message as there are 8 dates in test document
    expected = 'Sucessfully redacted 8 Dates'

    assert open(
        'project_docs/test_project/testLog').read().splitlines()[-1] == expected  # Verifying the contents of the log file w.r.t expected

# Testing the method used to redact sentences containing the words related to concept


def testRedactConcept():
    parser = argparse.ArgumentParser()  # Creating an argument parser object
    # Adding optinal argument --concept
    parser.add_argument("--concept", type=str,
                        required=False, nargs="+", action="append")
    parser.add_argument("--stats", type=str, required=False,
                        default="stdout")  # Adding optinal argument --stats
    args = parser.parse_args(
        "--concept shot --stats ../test_project/testLog".split())

    redactor.redactConcept(data[0][0], args)

    # log file must be updated with this message as there are 4 sentences in test document containing the words related to concept 'shot'
    expected = 'Sucessfully redacted 4 sentences where words related to concept are present'

    assert open(
        'project_docs/test_project/testLog').read().splitlines()[-1] == expected  # Verifying the contents of the log file w.r.t expected
