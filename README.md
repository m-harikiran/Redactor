# Redaction of Sensitive Information

#### Author: Harikiran Madishetti

---

## About

In this project, we will learn to use NLTK and other packages to redact the sensitive information present in '.txt' files. Whenever sensitive information is shared with the public, the data must go through a redaction process. That is, all sensitive names, places, and other sensitive information must be hidden. Documents such as police reports, court transcripts, and hospital records all containing sensitive information. Redacting this information is often expensive and time-consuming.

## Packages Required

The below is the list of packages used in this project.

- re
- os
- commonregex
- regex
- argparse
- nltk
- glob
- pytest

Libraries such as argparse, re, os, and glob are standard libraries in python3. To install other libraries please use Command `pipenv install -r requirements.txt`

## Directions to Install and Use Pagkage

The below are the insturctions to be followed to download, install and run the package/project.

1. Create a directory and then cd into the directory
   **`mkdir Text_Project1 && cd Test_Project1`**
2. Download the project files from GitHub
   **`https://github.com/Harikiran-Madishetti/cs5293sp21-project1.git`**
3. Cd into project directory **cs5293sp21-project1**
   **`cd cs5293sp21-project1`**
4. Install python package pipenv to create a virtual enviromnent
   **`pip install pipenv`**
5. After successfully installing pipenv create a python3 virtual environment
   **`pipenv install --three`**
6. Install the dependencies listed in **requirements.txt** to start using the package
   **`pipenv install -r requirements.txt`**
7. After installing the dependencies successfully run unit tests
   **`pipenv run pytest`**
8. After running the unit tests successfully start using package (relpace URL with the URL of incidents list) using below command to fetch summary of the incidents by its nature
   **`pipenv run python project1/main.py --input '*.txt' '*.pdf' --input 'others/*.txt' --names --phones --genders --dates --concept 'shot' 'shackles' --stats 'redaction_status' --output 'redacted_documents''`**

## Assumptions

In this project I am using NLTK package to identify the names present in the documents, and custom regex patter to identify the phone numbers and using a library to identify the different dates present in the documents. Using these methods most of the data related to them is identifiend and redacted, but there might be edge cases where regex pattern might not be able to identify the dates, names, genders and phone numbers. The default folder where all the files related to project must be placed is **project_docs** as it is used as project default folder. The documents which are supposed to be redacted **project_docs**, redacted documents are placed in **redacted_documents** of **project_docs** and the redaction status logs will be placed in **project_docs/redaction_logs**. In case if you want to go up a directory **"../"** must be passed along with the input files path.

Example **"../redact.txt"** if the file you want redact is placed in default project directory (**cs5293sp21-project1**)

## Description

In this project I am reading the data present in '.txt' files and redacting the sensitive information like dates, phone numbers, genders, names and concept present in documents. To implement this the project package has two main files:
**1. main.py**
**2. redactor.py**
In order to test the package we also have **test_redactor.py**.

### 1. main.py

This file is invoked to process the data and output the results. This files takes the input parameters **-- inputs** as file names or its path where files to be redacted are placed, **--concept** as words or strings which are supposed to be redacted, **--stats** as string where redaction status logs must be placed and **--output** to specify the directory for redacted documents. It also takes the flags **--phones**, **--genders**, **--dates** to redact the content present in documents. All these command line agruments are handled using the library **agrparse**.

These input paramentrs are passed to the methods imported from **redactor.py** for reading, redacting and writing the redacted data. The below are different methods called by main function:

- Method **`redactor.statsFile(input_parameters.stats)`** is used to create redaction status log file
- Method **`redactor.fetchDocs(input_parameters)`** is used to read the data from the input files

The below methods are called for each input file

- Method **`redactor.updateStatusLog(message, input_parameters.stats)`** is used to log updates in redaction satus log file
- Method **`redactor.redactPhone(doc_data[0], input_parameters)`** is used to redact phone numbers
- Method **`redactor.redactGender(redact_phones, input_parameters)`** is used to redact gender identification words
- Method **`redactor.redactNames(redact_genders, input_parameters)`** is used to redact Names
- Method **`redactor.redactConcept(redact_dates, input_parameters)`** is used to redact words similar to concept
- Method **`redactor.redactedDoc((redact_concept, doc_data[1]), input_parameters.output)`** is used to write the redacted data into files with extension **'.redacted'**

### 2. redactor.py

This package is used by **main.py** to read, redact and write redacted data.

#### i. statsFile(args)

This method takes redaction status log file name as input parameters and creates a file with the given name in **'/project_docs/redaction_logs/'**.

#### ii. updateStatusLog(message, args)

This method takes message to be appened in redaction status log and status log file name as input parameters and then updated the status log with the message.

#### III. fetchDocs(args)

This method takes all the arguments passed from command line as parameters and then extracts the input file names or pattern to identify the the input files using **glob** library. The data from each fille and its name is added to tuple and this is appended to a list containing the data of all the files. If a file cannot be read the status is updated in status log file. Finally a list containing the tuples of data from file and it's name is returned.

```python
docs_list = nltk.flatten(args.input)
docs_data = []
for i in docs_list:
    for j in glob.glob('project_docs/'+i):
        if j[-4:] == '.txt':  # Verifying if the input file is text or not
            # Reading data from text files and appending the tuple containing file data and its name
            docs_data.append((open(j).read(), j[j.rfind('/')+1:-4]))
```

#### Iv. redactPhone(data, args)

This method takes data from the file and command line input parameters and redacts the dates identified using the below regex pattern.

```python
pattern = '\\b[+]?[0-9]{0,3}[ -]?[(]?[0-9]{3}[)]?[- ]?[0-9]{3}[- ]?[0-9]{4}\\b'
```

All the identified dates are replaced with block charcters and the method returns redacted data if **--phone** flag is passed from the command line or else it returns the unredacted data.

#### v. redactGender(data, args)

This method takes data returned by the above and command line input parameters and redacts the gender related words using the below list of gender's list.

```python
gender_list = ['HE', 'SHE',	'HIM', 'HER', 'HIS', 'HERS', 'HIMSELF', 'HERSELF', 'BOYFRIEND',
                   'GIRLFRIEND', 'HUSBAND', 'WIFE', 'SISTER', 'BROTHER', 'SON', 'DAUGHTER', 'GIRL',
                   'BOY', 'MALE', 'FEMALE', 'MAN', 'MEN', 'WOMAN', 'WOMEN', 'MOTHER', 'FATHER']
```

All the identified gender words are replaced with block charcters and the method returns redacted data if **--genders** flag is passed from the command line or else it returns the unredacted data.

#### vi. redactNames(data, args)

This method takes data returned by the above and command line input parameters and redacts the names which are identified using the nltk package.

```python
tokenized_data = nltk.word_tokenize(data)       # Splitting data into words
# Generationg the parts of speech of each word
pos_tokenized_data = nltk.pos_tag(tokenized_data)
# Chunking the tagged words using named entity chunker
chk_tagged_tokens = nltk.chunk.ne_chunk(pos_tokenized_data)
for chk in chk_tagged_tokens.subtrees():
    if chk.label().upper() == 'PERSON':  # Extracting the words with tag PERSON
    # Extracting first and last name
    name = ' '.join([i[0] for i in chk])
```

All the identified names are replaced with block charcters and the method returns redacted data if **--names** flag is passed from the command line or else it returns the unredacted data.

#### vii. redactDates(data, args)

This method takes data returned by the above and command line input parameters and redacts the dates which are identiffied using **commonregex** package.

```python
parsed_data = CommonRegex(data)  # Parsing the data using common regex
matched_dates = parsed_data.dates  # Finding all the dates available in data
```

All the identified dates are replaced with block charcters and the method returns redacted data if **--dates** flag is passed from the command line or else it returns the unredacted data.

#### viii. redactConcept(data, args)

This method takes data returned by the above and command line input parameters and redacts the entire sentence where the words which have similar meaning to that of the given concept word is identified.

```python
# Identifies the synonyms of words which has same meaning
syns = wordnet.synsets(concept)
# Extracting the lemmatized names of the words similar to synonyms of the concept
concept_syns.append([i.lemma_names() for i in syns])
```

All the identified sentences are replaced with block charcters and the method returns redacted data if **--concept** flag is passed from the command line or else it returns the unredacted data.

#### ix. redactedDoc(message, out_path)

This method takes data returned by the above and name of the redaction file as a tuple and also the output directory name or it's path to place the redacted files with an extension **.redacted**

```python
redactDoc = open(
    os.getcwd()+"/project_docs/{}/{}.redacted".format(out_path, message[1]), 'w')  # Opening a file
redactDoc.write(message[0])  # Writing a line to file
redactDoc.close()  # Closing the file
```

### 3. test_redactor.py

The package **test_redactor.py** has test cases defined as methods, that can be used for unit testing of methods defined in the package **redactor.py**. In order to test each method in **redactor.py**, first we need to import **redactor.py**. I am using **assert** in python to verify if the test condition is true or not. If the condition returns FALSE then assert statement will fail, which inturns fails the test case.

#### i. testStatusFile()

This method is used to test method **statsFile(args)** in **redactor.py**. In this, I am verifying if the log file created by **redactor.statusFile(args)** when it is called.

```python
redactor.statsFile('../test_project/testLog')	# Calling the method to create testlog file
assert os.path.isfile('project_docs/test_project/testlog')	# Verifying if the testlog file is created or not
```

#### ii. testUpdateStatusLog()

This method is used to test method **updateStatusLog()** in **redactor.py**. In this, I am verifying if the message that we have passed is updated in the log file or not.

```python
message = 'Testing status updating method'	# Message to be writted to status log
redactor.updateStatusLog(message, '../test_project/testLog')	# Updating the status log
assert open('project_docs/test_project/testlog').read().splitlines()[-1] == message  # Verifying the updated message
```

#### iii. testRedactedDoc()

This method is used to test method **redactedDoc()** in **redactor.py**. In this, I am verifying if the contents and the name of the redacted document.

```python
assert os.path.isfile('project_docs/test_project/test.redacted')	# Verifying if the file with .redacted extension id created or not
assert open(
	'project_docs/test_project/test.redacted').read().splitlines()[-1] == message[0]  # Verifying the contents of the redacted file
```
