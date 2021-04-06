import os
import nltk
import re
import glob


# Function used to setup status file to log the redation process


def statsFile(args):

    statusLog = open(
        os.getcwd()+"/project_docs/redaction_logs/"+args, 'w')  # Opening a file
    statusLog.write(
        '************ Redaction Status of Documents ************\n')  # Writing a line to file
    statusLog.close()  # Closing the file
