#### _Read this in [other languages](translations/Translations.md)
<kbd>[<img title="Shqip" alt="Shqip" src="https://cdn.staticaly.com/gh/hjnilsson/country-flags/master/svg/pt.svg" width="22">](translations/README.pt.md)</kbd>

<kbd>[<img title="Shqip" alt="Shqip" src="https://cdn.staticaly.com/gh/hjnilsson/country-flags/master/svg/fr.svg" width="22">](translations/README.fr.md)</kbd>


# PatMail

PatMail is an application for automated sending of emails made entirely in python, using the TKinter module for the graphical interface.

## Documentation
PatMail allows the user to import a .csv file of contacts, containing two columns, in order, "Name" and "Email", and a .txt file, which will contain the message to be sent to the contacts of the contacts file. Furthermore, PatMail allows the user to import attachments to be sent together with the message to be sent to contacts.

### Usage

1- Import the files either by typing the file path or using the search tool;

2- Add attachments to the body of the message, if you want;

3- Enter your email and password;

4- Add the email subject;

5- Click on "Send Emails";

NOTE: Steps 1 through 4 can be done in any order.

## Functionalities

- Automated sending of emails to several contacts;
- Allows you to attach files to send;
- In the message .txt file, 2 variables can be used that will be replaced by recipient information:
    * ${NAME}: is replaced by the recipient's name;
    * ${EMAIL}: is replaced by the recipient's email;
- After importing the contacts file and the message file, in the contacts tab it will be possible to double-click on a recipient's line to open a preview of the message for that specific recipient.


## Installation

Once the requirements are met, there are two main ways to install the package.

### Requirements

- Python 3.6 or higher (application has not been tested on all versions, so it may work on versions prior to this one);
- pip install;

### 1) using as pip package

- Download PatMail source code;
- Navigate to the project root:

```bash
cd Path/To/PathMail
```

- Install the app as a python package:

```bash
pip install .
```

- If pip is not in the system PATH:

```bash
python3 -m pip install .
```

- After installation is complete, PatMail will be installed as a pip package, and can be opened with:

```bash
PatMail
```

### 2) calling the start file directly

If method 1 doesn't work or you don't want to leave PatMail as a pip package, you can simply download the necessary dependencies and call the file that starts the application:

```bash
pip install -r /Path/To/PatMail/requirements.txt
python3 /path/to/PatMail/src/main.py
```

Note: If you choose the second installation method, using an `alias` may facilitate application startup.

#### An example in bash:

add to ~/.bashrc or equivalent the following line:

```bash
alias PatMail='python3 /path/to/PatMail/src/main.py'
```
## Solution of Problems (Troubleshooting)

- PatMail only uses Google's SMTP server to send emails and, therefore, will be limited to possible restrictions of the server in question;
- If you can't log in with your username and password, try generating an application password in your Google user settings and using it as a password.
- If PatMail is not allowing the import of a .csv file, pay attention to the restrictions:
    * In the header (first line), they must contain only two pieces of information: "Name"/"Name" and "Email"/"E-Mail", in that order (the application is case insensitive for this information, to make it easier);
    * ALL rows must contain two columns with characters in them;
- If your problem is not listed here or the solutions presented did not solve your problem, open an issue detailing the situation with as much information as possible, so that it is possible to investigate the causes of the problem and look for solutions;

## License

[MIT](https://choosealicense.com/licenses/mit/)

