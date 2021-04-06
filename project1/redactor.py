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


# Function to update Redaction process and status


def updateStatusLog(message, args):
    statusLog = open(
        os.getcwd()+"/project_docs/redaction_logs/"+args, 'a')  # Opening a file to append data
    statusLog.write('{}\n'.format(message))  # Writing a line to file
    statusLog.close()  # Closing the file
