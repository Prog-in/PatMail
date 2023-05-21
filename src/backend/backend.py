import smtplib
import os
import pandas as pd
import typing  # Use annotations
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from pathlib import Path
from screeninfo import get_monitors  # Get the active monitor
from tkinter import Tk, Toplevel  
from string import Template


# TODO
# Implementar sistema de variáveis de $-substituição dinâmicas com base nas colunas
#    (possibilidade) usuário adiciona as variaveis e as chama pelo nome

# (para o futuro): arquivo de configuração para as variáveis e caminhos


class ContactsTableError(Exception):
    """
    Base class for errors on contacts table
    """
    def __init__(self, error_explanation: str, error_cause: str, extension: str | list | tuple) -> None:
        filtered_error_explanation = error_explanation.removeprefix('\n')
        self.message = f'{filtered_error_explanation}\n  {error_cause} {extension}'
        super().__init__(self.message)


class InvalidNumberOfColumnsError(ContactsTableError):
    """
    Raised when the DataFrame (file table of contents) have a number of columns different of two. 
    """
    def __init__(self, number_of_columns: list | tuple):
        super().__init__(
            self.__doc__, 
            'Number of columns:', 
            number_of_columns
        )


class InvalidHeader(ContactsTableError):
    """
    Raised when the header does not behave as expected.
    
    Expected headers: ['Name', 'Email'] or one of this variations: ['Nome', 'E-mail'] (case insensitive)
    """
    def __init__(self, name_of_header_columns: list | tuple):
        super().__init__(
            self.__doc__, 
            'File Header Columns:', 
            '[' + ', '.join(name_of_header_columns) + ']'
        )   


ENCODING = 'utf-8'
ALT_ENCODING = 'latin-1'
USER_HOME = os.path.expanduser('~')
sending_emails_errors = []


def file_exists(file: str | tuple) -> bool:
    """
    Returns True if the file exists. Otherwise, False
    
    Parameters:
        - file: file to be checked
    """
    # file will be a tuple if filedialog.askopenfilename is closed before the user chooses a file
    if isinstance(file, tuple):
        return False
    else:
        return os.path.isfile(file)


def get_contacts(file_path: str, sep: str) -> typing.Generator[tuple[str, str], None, None]:
    """
    Returns a generator containing, respectively, name and email of the contacts.

    Parameters:
        - file_path: file path from which information will be imported

    Expected pattern in CSV:
        * name,email
        * example1,example1@email.com
        * example2,example2@email.com
        * ...
    """
    def iter_contacts(filtered_contacts_df: pd.DataFrame) -> typing.Generator[tuple[str, str], None, None]:
        """
        Returns a generator with the elements (name, email), already treated
        """
        col_name, col_email = filtered_contacts_df.keys()

        qtd_rows = filtered_contacts_df.shape[0]

        for row in range(qtd_rows):
            name: str = filtered_contacts_df.at[row, col_name]
            name = name.capitalize()
            email: str = filtered_contacts_df.at[row, col_email]
            yield name, email


    try:
        contacts_df = pd.read_csv(file_path, sep=sep, encoding=ENCODING)
    except UnicodeDecodeError:  # error with \xe9 char
        contacts_df = pd.read_csv(file_path, sep=sep, encoding=ALT_ENCODING)
        
    #if file_path.endswith(('.csv', '.CSV')):
    #    contacts_df = pd.read_csv(file_path)
    #elif file_path.endswith(('xls', 'xlsx')):
    #    contacts_df = pd.read_excel(file_path)
    
    columns = contacts_df.columns
    
    if len(columns) != 2:
        raise InvalidNumberOfColumnsError(len(columns))

    elif columns[0].lower().strip() not in ('name', 'nome') \
        or columns[1].lower().strip() not in ('email', 'e-mail'):
        raise InvalidHeader(columns)

    else:
        filtered_contacts_df = contacts_df[columns]
        #filtered_df.dropna(inplace=True)
        return iter_contacts(filtered_contacts_df)


def get_attachments(attachments: list[str]) -> MIMEBase:
    """
    
    """
    for path in attachments:
        part = MIMEBase('application', 'octet-stream')

        with open(path, 'rb') as file:
            part.set_payload(file.read())

        encoders.encode_base64(part)

        part.add_header(
            'Content-Disposition',
            'attachment; filename={}'.format(Path(path).name))
        
        yield part


def read_template(file_path) -> Template:
    """
    Reads a template file and returns a Template of it
    Template file: file containing a template message, with $-overriders inside it

    Parameters:
        - file_path: path of the file in which the message is
    """
    with open(file_path, 'r', encoding=ENCODING) as template_file:
        template_file_content = template_file.read()

    return Template(template_file_content)


def gen_user_message(template: Template, name='', email='') -> str:
    """
    Returns a message consisting of the template with the $-overrides made
    
    Parameters:
        - template: Template where $-overrides will take place
        - name: recipient's name
        - email: recipient's email

    $-overrides allowed:
        - ${NAME} : name
        - ${EMAIL} : email
    """
    message = template.safe_substitute(NAME=name, EMAIL=email)
    return message


def send_mails(user_email: str, 
               user_passwd: str,
               #*others,
               contacts: typing.Generator[tuple[str, str], None, None],
               template: Template,
               attachments: list[str],
               subject: str
               # client: str   # gmail, outlook, ...
               ) -> None:
    """
    Send emails with final messages to contacts.

    Parameters:
        - user_email: sender account email
        - user_passwd: sender account password
        - contacts: generator containing recipient information
        - template: the message to be sent, with possible $-overrides
        - subject: the subject of the email
    """
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
        server.starttls()
        server.login(user_email, user_passwd)
        server.send
        
        for name, email in contacts:
            msg = MIMEMultipart()

            msg['From'] = user_email
            msg['To'] = email
            msg['Subject'] = subject
            msg['Date'] = formatdate(localtime=True)

            message = gen_user_message(template, name, email)

            msg.attach(MIMEText(message, _charset=ENCODING))

            for attachment in get_attachments(attachments):
                msg.attach(attachment)

            try:
                server.send_message(msg, msg['From'], msg['To'])
            except Exception as error:
                sending_emails_errors.append((name, email, error))


def get_send_emails_errors() -> list[tuple[Exception, str, str]]:
    """
    returns a list containing (name, email, error) of all recipients whose email sending 
    caused exceptions in the last email send
    """
    global sending_emails_errors

    tmp = sending_emails_errors.copy()
    sending_emails_errors = []

    return tmp
    

def set_geometry_popup(
    popup: Tk | Toplevel, 
    root: Tk, 
    width: int, 
    height: int
    ) -> None:
    """
    Sets the geometry of the new window in the middle of the selected screen
    
    Parameters:
        - popup: the popup to be created
        - root: popup root
        - width: popup width
        - height: popup height
    """

    def get_monitor_from_coord(x, y):
        """
        Find the active monitor from tkinter geometry coordinates
        
        Parameters:
            - x: x coordinates
            - y: y coordinates
        """
        monitors = get_monitors()

        for m in reversed(monitors):
            if m.x <= x <= m.width + m.x and m.y <= y <= m.height + m.y:
                return m
        return monitors[0]

    monitor = get_monitor_from_coord(root.winfo_x(), root.winfo_y())
    monitor_pos_width = (monitor.width - width) // 2 + monitor.x
    monitor_pos_height = (monitor.height - height) // 2 + monitor.y
    popup.geometry(f"{width}x{height}+{monitor_pos_width}+{monitor_pos_height}")
