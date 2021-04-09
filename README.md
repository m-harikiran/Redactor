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
   **`python3 project1/main.py --input '*.txt' '*.pdf' --input 'others/*.txt' --names --phones --genders --dates --concept 'shot' 'shackles' --stats 'redaction_status'`**

## Assumptions

In this project I am using NLTK package to identify the names present in the documents, and custom regex patter to identify the phone numbers and using a library to identify the different dates present in the documents. Using these methods most of the data related to them is identifiend and redacted, but there might be edge cases where regex pattern might not be able to identify the dates, names, genders and phone numbers. The default folder where all the files related to project must be placed is **project_docs** including the documents which are supposed to be redacted and the redaction status logs will be placed in **project_docs/redaction_logs**. In case if you want to go up a directory **"../"** must be passed along with the input files path.

Example **"../redact.txt"** if the file you want redact is placed in default project directory (**cs5293sp21-project1**)
