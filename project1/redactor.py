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


# Function to extract data from the documents to be redacted.


def fetchDocs(args):

    docs_list = nltk.flatten(args.input)

    docs_data = []

    for i in docs_list:
        for j in glob.glob('project_docs/'+i):
            if j[-4:] == '.txt':
                docs_data.append(open(j).read())
                message = "Successfully read data from '{}'".format(j[13:])
                updateStatusLog(message, args.stats)
            else:
                message = "Cannot read data from '{}'".format(j[13:])
                updateStatusLog(message, args.stats)
    return docs_data


# Function to redact phone numbers.


def redactPhone(data, args):
    matched_phones = []

    if args.phones:
        pattern = '\\b[+]?[0-9]{0,3}[ ]?[(]?[0-9]{3}[)]?[- ]?[0-9]{3}[- ]?[0-9]{4}\\b'
        matched_phones = re.findall(pattern, data)

        for i in matched_phones:
            print(i)
            # data = data.replace(i, len(i)*'\u2588')
            data = re.sub('\\b{}\\b'.format(
                re.escape(i.strip())), '\u2588'*len(i), data)

    message = 'Sucessfully redacted {} phone numbers'.format(
        len(matched_phones))
    updateStatusLog(message, args.stats)

    return data
