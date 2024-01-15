# Python API Automation Framework

Hybrid Custom Framework to Test the REST APIs

![Screenshot 2023-12-08 at 8 20 27 AM](https://github.com/PramodDutta/Py1xAPIAutomation/assets/1409610/a09647ad-720b-4afb-8d33-b69e4710cee4)


- Name - Pramod
- Author - Pramod


### Web Automation Framework with POM in Python(Selenium)

- Python, PyTest
- Selenium
- Allure Report
- Gitignore, PyTest Report
- Page Object Model and Page Factory both
- Highlight element while run
- Parallel Run with xdist
- MY SQL data base connect to verify data.

## Folder Structure

<img width="944" alt="Screenshot 2023-08-28 at 5 28 26 PM" src="https://github.com/PramodDutta/PyWebAutomation0x/assets/1409610/629dd569-5a7f-4293-a821-7af6f97786cc">



# CI/CD Run


<img width="1199" alt="Screenshot 2023-08-28 at 5 28 46 PM" src="https://github.com/PramodDutta/PyWebAutomation0x/assets/1409610/b339baf7-ae46-4188-b285-bfb88862f752">



- pip install allure-pytest requests
- pip install pytest selenium pytest-html openpyxl 
- pip install selenium-page-factory 
- pip install pyyaml faker openpyxl
- pip install pytest-xdist 
- pip install mysql-connector-python
- pip install pytest-reportportal

### How to Install Packages
`` pip install requests pytest pytest-html faker allure-pytest jsonschema
``

### To Freeze your Package version
`` pip freeze > requirements.txt ``

## To Install te Freeze Version
``pip install -r requirements.txt``
<<<<<<< HEAD


## How to run your Testcase Parallel 
`` pip install pytest-xdist ``


``pytest -n auto tests/integration_test/test_create_booking.py -s -v
``

### To Work with the Excel- read write
``pip install openpyxl``


### To Install faker for random data
``pip install faker``

    from faker import Faker
    faker=Faker()
    faker.first_name()

### Install .env package for secured environment
``pip install python-dotenv``

    from dotenv import load_dotenv
    import os

## To work wit JSON Schema
``pip install jsonschema``

    from jsonschema import validate
    from jsonschema.exceptions import ValidationError