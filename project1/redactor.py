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
            if j[-4:] == '.txt':  # Verifying if the input file is text or not
                # Reading data from text files
                docs_data.append(open(j).read())
                message = "Successfully read data from '{}'".format(
                    j[13:])  # Updating status log
                updateStatusLog(message, args.stats)
            else:
                # Updating status log if we cannot read file
                message = "Cannot read data from '{}'".format(j[13:])
                updateStatusLog(message, args.stats)
    return docs_data


# Function to redact phone numbers.


def redactPhone(data, args):
    matched_phones = []

    if args.phones:
        # Regex Pattern to find phone numbers
        pattern = '\\b[+]?[0-9]{0,3}[ ]?[(]?[0-9]{3}[)]?[- ]?[0-9]{3}[- ]?[0-9]{4}\\b'
        # Finding all the phone numbers
        matched_phones = re.findall(pattern, data)

        for i in matched_phones:

            data = re.sub('\\b{}\\b'.format(
                re.escape(i.strip())), '\u2588'*len(i), data)  # Replacing the phone numbers with block

    message = 'Sucessfully redacted {} phone numbers'.format(
        len(matched_phones))  # Updating status log
    updateStatusLog(message, args.stats)

    return data


# Function to redact words related to gender

def redactGender(data, args):
    gender_list = ['HE', 'SHE',	'HIM', 'HER', 'HIS', 'HERS', 'HIMSELF', 'HERSELF', 'BOYFRIEND',
                   'GIRLFRIEND', 'HUSBAND', 'WIFE', 'SISTER', 'BROTHER', 'SON', 'DAUGHTER', 'GIRL',
                   'BOY', 'MALE', 'FEMALE', 'MAN', 'MEN', 'WOMAN', 'WOMEN', 'MOTHER', 'FATHER']  # List of gender related words
    count = 0

    if args.genders:
        tokenized_data = nltk.word_tokenize(data)  # Splitting data into words
        for words in tokenized_data:
            if words.upper() in gender_list:
                data = re.sub('\\b{}\\b'.format(words),
                              '\u2588'*len(words), data)  # Replacing gender related words with block
                count += 1

    message = 'Sucessfully redacted {} words related to gender identity'.format(
        count)  # Updating the status log
    updateStatusLog(message, args.stats)
    return data

# Function to redact Names


def redactNames(data, args):

    count = 0

    if args.names:
        tokenized_data = nltk.word_tokenize(
            data)       # Splitting data into words

        # Generationg the parts of speech of each word
        pos_tokenized_data = nltk.pos_tag(tokenized_data)

        # Chunking the tagged words using named entity chunker
        chk_tagged_tokens = nltk.chunk.ne_chunk(pos_tokenized_data)

        for chk in chk_tagged_tokens.subtrees():

            if chk.label().upper() == 'PERSON':  # Extracting the words with tag PERSON

                # Extracting first and last name
                name = ' '.join([i[0] for i in chk])
                # print(name)
                data = re.sub('\\b{}\\b'.format(name),
                              '\u2588'*len(name), data)  # Replacing the names with block character
                count += 1
    message = 'Sucessfully redacted {} Names'.format(
        count)  # Updating the redaction status in log
    updateStatusLog(message, args.stats)
    return data
