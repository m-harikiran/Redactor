import argparse
import os
import nltk
import re
import glob
from commonregex import CommonRegex
from nltk.corpus import wordnet
from project1 import redactor


def argParser():
    parser = argparse.ArgumentParser()  # Creating an argument parser object
    # Adding optinal argument --inputs
    parser.add_argument("--input", type=str, required=True,
                        nargs="+", action="append")
    # Adding optinal argument --names
    parser.add_argument("--names", required=False, action="store_true")
    # Adding optinal argument --dates
    parser.add_argument("--dates", required=False, action="store_true")
    # Adding optinal argument --phones
    parser.add_argument("--phones", required=False, action="store_true")
    # Adding optinal argument --genders
    parser.add_argument("--genders", required=False, action="store_true")
    # Adding optinal argument --output
    parser.add_argument("--output", type=str, required=False,
                        default="redacted_documents")
    parser.add_argument("--stats", type=str, required=False,
                        default="stdout")  # Adding optinal argument --stats
    # Adding optinal argument --concept
    parser.add_argument("--concept", type=str,
                        required=False, nargs="+", action="append")

    args = parser.parse_args(
        "--input hari kiran --input madi --output /hari --concept Jail dog".split())


# Testing creation of status file


def testStatusFile():

    # Calling the method to create testlog file
    redactor.statsFile('../test_project/testLog')

    # Verifying if the testlog file is created or not
    assert os.path.isfile('project_docs/test_project/testlog')
