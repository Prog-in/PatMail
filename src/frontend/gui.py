from src.metadata import __project__
import tkinter as tk
from tkinter import scrolledtext 
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import src.backend.backend as backend
import typing

# TODO 
# implementar Style (dark e white)
# colocar o path de contacts file e template file nas abas
# implementar forma de ver se a informação já foi preenchida

class App():
    def start(self):
        backend.set_geometry_popup(self.root, self.root, self.WIDTH, self.HEIGHT)

        self.root.minsize(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.root.maxsize(self.MAX_WIDTH, self.MAX_HEIGHT)
        self.root.title(__project__)

        self.root.mainloop()


    def __init__(self):
        self.root = tk.Tk()

        self.WIDTH = 630
        self.HEIGHT = 380

        self.MIN_WIDTH = 550
        self.MIN_HEIGHT = 380

        self.MAX_WIDTH = 700
        self.MAX_HEIGHT = 400

        # create notebook
        self.notebook = ttk.Notebook(self.root)

        # Initialize the *path vars, needed for some functions
        self.contacts_path = '' 
        self.template_path = ''

        # Initialize the user account vars
        self.email = ''
        self.password = ''

        self.subject = ''

        frame_home = self.create_frame_home()
        frame_home.pack(fill='both', expand=True)

        frame_contacts_file = self.create_frame_contacts_file()
        frame_contacts_file.pack(fill='both', expand=True)

        frame_template_file = self.create_frame_template_file()
        frame_template_file.pack(fill='both', expand=True)

        frame_attachments = self.create_frame_attachments()
        frame_attachments.pack(fill='both', expand=True)

        frame_about = self.create_frame_about()
        frame_about.pack(fill='both', expand=True)

        # add frames to notebook
        self.notebook.add(frame_home, text='Home')
        self.notebook.add(frame_contacts_file, text='Contacts File')
        self.notebook.add(frame_template_file, text='Template File')
        self.notebook.add(frame_attachments, text='Attachments')
        self.notebook.add(frame_about, text='About')

        self.notebook.pack(fill='both', expand=True)

        self.contacts_filetypes = (
            ('csv files', ('.csv', '.CSV')), 
            #('Excel files', ('.xlsx', '.XLSX', '.xls', '.XLS')), 
        )

        self.template_filetypes = (
            ('Txt files', ('.txt', '.TXT')), 
            ('Doc files', ('.docx', '.DOCX', '.doc', '.DOC')),
        )

        self.contacts_filetypes_supported = self.get_supported(self.contacts_filetypes)
        self.template_filetypes_supported = self.get_supported(self.template_filetypes)


    def create_frame_home(self) -> ttk.Frame:

        def create_home_frame1() -> ttk.Labelframe:

            home_frame1 = ttk.Labelframe(
                frame_home, 
                text='Account Options',
            )

            self.user_email = tk.StringVar(home_frame1)
            self.user_password = tk.StringVar(home_frame1)

            label_user_email = ttk.Label(
                home_frame1, 
                text='Enter your email:',
            )
            entry_user_email = ttk.Entry(
                home_frame1, 
                textvariable=self.user_email,
            )
            label_user_password = ttk.Label(
                home_frame1, 
                text='Enter your password:',
            )
            entry_user_password = ttk.Entry(
                home_frame1, 
                show='*', 
                textvariable=self.user_password,
            )
            button_submit_account = ttk.Button(
                home_frame1, 
                text='Submit', 
                command=self.get_user_account
            )

            for i in range(5):
                home_frame1.columnconfigure(i, weight=1)

            label_user_email.grid(row=0, column=1, padx=6, pady=5, sticky='e')
            entry_user_email.grid(row=0, column=2, padx=6, pady=5, sticky='ew')

            label_user_password.grid(row=1, column=1, padx=6, pady=5, sticky='e')
            entry_user_password.grid(row=1, column=2, padx=6, pady=5, sticky='ew')
            
            button_submit_account.grid(row=2, column=2, padx=6, pady=5, sticky='e')

            return home_frame1


        def create_home_frame2() -> ttk.Labelframe:

            home_frame2 = ttk.Labelframe(
                frame_home, 
                text='Import Options',
            )

            self.contacts_file_stringvar = tk.StringVar(home_frame2)
            self.template_file_stringvar = tk.StringVar(home_frame2)

            label_import_contacts = ttk.Label(
                home_frame2, 
                text='Import contacts file:',
            )
            entry_import_contacts = ttk.Entry(
                home_frame2, 
                textvariable=self.contacts_file_stringvar,
            )
            button_browse_import_contacts = ttk.Button(
                home_frame2, 
                text='Browse', 
                command=lambda: self.browse(
                    self.contacts_file_stringvar, 
                    'Select Contacts File', 
                    self.contacts_filetypes
                ),
            )
            button_submit_import_contacts = ttk.Button(
                home_frame2, 
                text='Submit', 
                command=self.import_contacts,
            )

            label_import_template = ttk.Label(
                home_frame2, 
                text='Import template file:',
            )
            entry_import_template = ttk.Entry(
                home_frame2, 
                textvariable=self.template_file_stringvar,
            )
            button_browse_import_template = ttk.Button(
                home_frame2, 
                text='Browse', 
                command=lambda: self.browse(
                    self.template_file_stringvar, 
                    'Select Template File', 
                    self.template_filetypes
                ),
            )
            button_submit_import_template = ttk.Button(
                home_frame2, 
                text='Submit', 
                command=self.import_template,
            )

            for i in range(5):
                home_frame2.columnconfigure(i, weight=1)

            label_import_contacts.grid(row=0, column=1, padx=6, pady=5, sticky='e')
            entry_import_contacts.grid(row=0, column=2, padx=6, pady=5, sticky='ew')
            button_browse_import_contacts.grid(row=0, column=3, padx=6, pady=5, sticky='w')
            button_submit_import_contacts.grid(row=0, column=4, padx=6, pady=5, sticky='w')

            label_import_template.grid(row=1, column=1, padx=6, pady=5, sticky='e')
            entry_import_template.grid(row=1, column=2, padx=6, pady=5, sticky='ew')
            button_browse_import_template.grid(row=1, column=3, padx=6, pady=5, sticky='w')
            button_submit_import_template.grid(row=1, column=4, padx=6, pady=5, sticky='w')

            return home_frame2
        

        def create_home_frame3() -> ttk.Labelframe:
            
            home_frame3 = ttk.Labelframe(
                frame_home, 
                text='Email Options',
            )

            self._subject = tk.StringVar(home_frame3)

            label_subject = ttk.Label(
                home_frame3, 
                text='Enter the subject of the email:',
            )
            entry_subject = ttk.Entry( 
                home_frame3, 
                textvariable=self._subject,
            )
            button_subject = ttk.Button(
                home_frame3, 
                text='Submit', 
                command=self.get_subject,
            )

            for i in range(5):
                home_frame3.columnconfigure(i, weight=1)

            label_subject.grid(row=0, column=0, padx=6, pady=5, sticky='e')
            entry_subject.grid(row=0, column=1, padx=6, pady=5, sticky='ew', columnspan=3)
            button_subject.grid(row=0, column=4, padx=6, pady=5)

            return home_frame3


        def create_home_frame4() -> ttk.Labelframe:

            home_frame4 = ttk.Labelframe(
                frame_home, 
                text='Send Emails',
            )
            button_send_emails = ttk.Button(
                home_frame4, 
                text='Send Emails', 
                command=self.send_mails,
            )

            button_send_emails.pack(pady=6)

            return home_frame4


        frame_home = ttk.Frame(self.notebook)

        home_frame1 = create_home_frame1()
        home_frame2 = create_home_frame2()
        home_frame3 = create_home_frame3()
        home_frame4 = create_home_frame4()
        
        home_frame1.pack(fill='both', expand=True)
        home_frame2.pack(fill='both', expand=True)
        home_frame3.pack(fill='both', expand=True)
        home_frame4.pack(fill='both', expand=True)

        return frame_home


    def create_frame_contacts_file(self) -> ttk.Frame:
        frame_contacts_file = ttk.Frame(self.notebook)
        
        columns = ('Name', 'Email')
        self.treeview_contacts = ttk.Treeview(
            frame_contacts_file, 
            columns=columns, 
            show='headings'
        )
        button_list_contacts = ttk.Button(
            frame_contacts_file, 
            text='Refresh Contact List', 
            command=self.populate_treeview_contacts
        ) 
        treeview_scroolbar = ttk.Scrollbar(
            frame_contacts_file, 
            orient='vertical', 
            command=self.treeview_contacts.yview
        )
        self.treeview_contacts.configure(yscrollcommand=treeview_scroolbar.set)

        self.treeview_contacts.heading('Name', text='Name')
        self.treeview_contacts.heading('Email', text='Email')

        self.treeview_contacts.bind('<Double-1>', self.gen_preview_toplevel)

        button_list_contacts.pack(side='top', anchor='nw', pady=6)
        treeview_scroolbar.pack(side='right', fill='y')
        self.treeview_contacts.pack(side='bottom', fill='both', expand=True)

        return frame_contacts_file

    
    def create_frame_template_file(self) -> ttk.Frame:
        frame_template_file = ttk.Frame(self.notebook)

        button_visualize_template = ttk.Button(
            frame_template_file, 
            text='Refresh Template',
            command=self.visualize_template,
        )
        self.scrolledtext_template = scrolledtext.ScrolledText(
            frame_template_file, 
            state='disabled',
        )

        button_visualize_template.pack(side='top', anchor='nw', pady=6)
        self.scrolledtext_template.pack(side='bottom', fill='both', expand=True)
        
        return frame_template_file


    def create_frame_attachments(self) -> ttk.Frame:
        frame_attachments = ttk.Frame(self.notebook)

        frame_above = ttk.Frame(frame_attachments)

        self.attachments_str = tk.StringVar()
        self.attachments_list = []

        label_attachments = ttk.Label(
            frame_above, 
            text='Enter the attachment path:',
        )
        entry_attachments = ttk.Entry(
            frame_above, 
            textvariable=self.attachments_str,
        )
        button_browse_attachments = ttk.Button(
            frame_above, 
            text='Browse', 
            command=lambda: self.browse(
                self.attachments_str, 
                'Select Attachment File', 
                None
            ),
        )
        button_submit_attachments = ttk.Button(
            frame_above, 
            text='Submit', 
            command=self.import_attachments,
        )
        button_refresh_attachments = ttk.Button(
            frame_above, 
            text='Refresh attachments', 
            command=self.populate_treeview_attachments,
        )
        button_remove_attachment = ttk.Button(
            frame_above,
            text='Remove file',
            command=self.remove_attachment,
        )
        columns = ('Filename',)
        self.treeview_attachments = ttk.Treeview(
            frame_attachments, 
            columns=columns, 
            show='headings'
        )
        treeview_scroolbar = ttk.Scrollbar(
            frame_attachments, 
            orient='vertical', 
            command=self.treeview_attachments.yview
        )

        self.treeview_attachments.heading('Filename', text='Filename')
        
        for i in range(5):
            frame_above.columnconfigure(i, weight=1)

        label_attachments.grid(row=0, column=0, padx=6, pady=5, sticky='e')
        entry_attachments.grid(row=0, column=1, padx=6, pady=5, sticky='ew')
        button_browse_attachments.grid(row=0, column=2, padx=6, pady=5, sticky='w')
        button_submit_attachments.grid(row=0, column=3, padx=6, pady=5, sticky='w')
        button_refresh_attachments.grid(row=1, column=0, padx=6, pady=5, sticky='w')
        button_remove_attachment.grid(row=1, column=3, padx=6, pady=5, sticky='w')

        frame_above.pack(fill='both')
        treeview_scroolbar.pack(side='right', fill='y')
        self.treeview_attachments.pack(side='right', fill='both', expand=True)

        return frame_attachments
        

    def create_frame_about(self) -> ttk.Frame:
        frame_about = ttk.Frame(self.notebook, )

        message = '''
            To start using the application, fill in all the fields on the "Home" tab.

            In the "Contacts File" tab, you can see the list of imported contacts by clicking the "Refresh Contact List" button. Another feature is that when you double click on a contact you will see a preview of the email that will be sent to that contact if you have already imported the template file.

            In the "Template File" tab, you can preview the imported model by clicking the "Refresh Template" button.

            If, when sending emails, you receive an authentication error with your Google account, you will need to generate an app password in Google settings and use it as your password in the app.
        '''
        
        message_widget = tk.Message(frame_about, text=message, font='11')
        message_widget.pack(fill='both', expand=True)
        
        return frame_about


    def get_user_account(self) -> None:
        email = self.user_email.get()
        password = self.user_password.get()
        if email == '' or password == '':
            messagebox.showwarning(
                'WARNING',
                'Enter email and password, please.'
            )
        else:
            self.email = email
            self.password = password
            # returns to empty only if it works: gives a chance to put the missing information in case the user forgets
            self.user_email.set('')
            self.user_password.set('')
            messagebox.showinfo(
                'INFO',
                'Account information inserted successfully'
            )


    def get_subject(self) -> None:
        subject = self._subject.get()
        if subject == '':
            messagebox.showwarning(
                'WARNING',
                'Enter a subject, please.'
            )
        else:
            self.subject = subject
            messagebox.showinfo(
                'INFO',
                'Subject inserted successfully.'
            )
        self._subject.set('')

    
    def get_supported(self, filetypes: tuple[str, str | tuple[str]]) -> list[str]:
        supported = []
        for name, extension in filetypes:
            if isinstance(extension, tuple):
                for ext in extension:
                    supported.append(ext)
            else:
                supported.append(extension)
        
        return supported


    def import_file(
        self, 
        string_var: tk.StringVar, 
        extensions_supported: list | None, 
        show_success_notice: bool = True
        ) -> str:
        path = string_var.get()
        string_var.set('')  # teste

        if backend.file_exists(path):
            if extensions_supported is None:
                if show_success_notice:
                    messagebox.showinfo(
                        'INFO', 
                        'File imported\n\n' + path
                    )
                return path
            else:         
                supported = False
                for extension in extensions_supported:
                    if path.endswith(extension):
                        supported = True       
                        break

                if supported:
                    if show_success_notice:
                        messagebox.showinfo(
                            'INFO', 
                            'File imported\n\n' + path
                        )
                    return path
                else:
                    messagebox.showerror(
                        'ERROR', 
                        'Invalid extension\n\nAre supported: {}'.format(', '.join(extensions_supported))
                    )
        else:
            messagebox.showerror(
                'ERROR',  
                'Invalid path'
            )    

        return ''


    def import_contacts(self) -> None:
        path = self.import_file(self.contacts_file_stringvar, self.contacts_filetypes_supported, False)
        if path != '':
            try:
                backend.get_contacts(path)
            except Exception as error:
                messagebox.showerror(
                    'ERROR', 
                    error
                )
            else:
                messagebox.showinfo(
                    'INFO', 
                    'File imported\n\n' + path
                )
                self.contacts_path = path


    def import_template(self) -> None:
        path = self.import_file(self.template_file_stringvar, self.template_filetypes_supported)
        if path != '':
            self.template_path = path


    def import_attachments(self) -> None:
        path = self.import_file(self.attachments_str, None, False)
        if path != '':
            if path in self.attachments_list:
                messagebox.showwarning(
                    'WARNING',
                    'This file is already imported.'
                )
            messagebox.showinfo(
                'INFO', 
                'File imported\n\n' + path
            )
            self.attachments_list.append(path)
    

    def browse(self, stringvar: str, title: str, filetypes: str | None):
        if filetypes is None:
            path = filedialog.askopenfilename(
                initialdir=backend.USER_HOME, 
                title=title,
            )        
        else:
            path = filedialog.askopenfilename(
                initialdir=backend.USER_HOME, 
                title=title, 
                filetypes=filetypes
            )
        if backend.file_exists(path):
            stringvar.set(path)        


    def contacts_isimported(self) -> bool:
        return self.contacts_path != ''


    def template_isimported(self) -> bool:
        return self.template_path != ''


    def populate_treeview_contacts(self) -> None:
        if not self.contacts_isimported():
            messagebox.showwarning(
                'WARNING', 
                'Please, enter contacts file path in "Home" tab'
            )
            
        else:
            # Cleans the treeview from previous populate
            self.treeview_contacts.delete(*self.treeview_contacts.get_children())
            contacts_generator = backend.get_contacts(self.contacts_path)
            for contact in contacts_generator:
                self.treeview_contacts.insert('', 'end', values=contact)
    

    def populate_treeview_attachments(self) -> None:
        if len(self.attachments_list) == 0:
            messagebox.showwarning(
                'WARNING', 
                'Please insert the attached files'
            )
            
        else:
            # Cleans the treeview from previous populate
            self.treeview_attachments.delete(*self.treeview_attachments.get_children())
            for attachment in self.attachments_list:
                self.treeview_attachments.insert('', 'end', values=(attachment,))        


    def visualize_template(self) -> None:
        if not self.template_isimported():
            messagebox.showwarning(
                'WARNING', 
                'Please, enter template file path in "Home" tab'
            )        
        else:
            # Change state to 'normal' temporarily to make changes on the text
            self.scrolledtext_template.configure(state='normal')

            # clear the scrolledtext before the insertion of the content
            self.scrolledtext_template.delete('1.0', 'end')
            
            template = backend.read_template(self.template_path)
            self.scrolledtext_template.insert('end', template.template)

            self.scrolledtext_template.configure(state='disabled')


    def gen_preview_toplevel(self, event: tk.Event) -> None:
        if not self.template_isimported():
            messagebox.showwarning(
                'WARNING',
                'Import template file before.'
            )
        else:
            row_id = self.treeview_contacts.identify_row(event.y)

            if row_id != '':
                row_values = self.treeview_contacts.item(row_id)['values']
                name, email = row_values
                
                email_preview = tk.Toplevel(
                    self.root, 
                )
                email_preview.title('Email Preview')
                backend.set_geometry_popup(email_preview, self.root, 600, 400)

                scrolledtext_email_preview = scrolledtext.ScrolledText(
                    master=email_preview, 
                ) 

                template = backend.read_template(self.template_path)
                message = backend.gen_user_message(template, name, email)

                scrolledtext_email_preview.delete('1.0', 'end')
                scrolledtext_email_preview.insert('end', message)
                scrolledtext_email_preview.configure(state='disabled')

                scrolledtext_email_preview.pack(fill='both', expand=True)


    def remove_attachment(self) -> None:
        focus = self.treeview_attachments.focus()
        if focus == '':
            messagebox.showwarning(
                'WARNING', 
                'Please, select a attachment file'
            )   
        else:
            info = self.treeview_attachments.item(focus)
            value = info['values'][0]
            self.attachments_list.remove(value)
            self.treeview_attachments.delete(focus)
            messagebox.showinfo(
                'INFO', 
                'File removed\n\n'
            )


    def send_mails(self) -> None:
        if self.email == '' or self.password == '':
            messagebox.showwarning(
                'WARNING',
                'Please, enter your email and password before.'
            )
        elif self.subject == '':
            messagebox.showwarning(
                'WARNING',
                'Please, enter the subject of the email before.'
            )
        elif not self.contacts_isimported() or not self.template_isimported():
            messagebox.showwarning(
                'WARNING',
                'Import contacts file and template file before.'
            )
        else:
            contacts = backend.get_contacts(self.contacts_path)
            template = backend.read_template(self.template_path)

            try:  # error in connection phase
                backend.send_mails(
                    self.email, 
                    self.password, 
                    contacts, 
                    template, 
                    self.attachments_list,
                    self.subject
                )
                
            except Exception as error:
                messagebox.showerror(
                    'ERROR',
                    'An error occurred while sending the emails:\n\n' + str(error)
                )
            
            else:
                send_emails_errors = backend.get_send_emails_errors()
                if len(send_emails_errors) == 0:
                    messagebox.showinfo(
                        'INFO',
                        'All emails were sent successfully.'
                    )
                else:
                    header = 'Errors occurred with sending emails. See below.'
                    # message: name, email, error
                    messages = (message for message in send_emails_errors)
                    self.gen_error_toplevel(header, messages)
    

    def gen_error_toplevel(
        self, 
        header: str, 
        messages: typing.Generator[tuple[Exception, str, str], None, None]
        ) -> None:
        error_toplevel = tk.Toplevel(
            self.root,
        )
        error_toplevel.title('Errors with sending emails')
        error_toplevel.resizable(False, False)
        backend.set_geometry_popup(error_toplevel, self.root, 700, 400)

        errors_entry = ttk.Label(
            error_toplevel,
            text=header,
        )
        columns = ('Name', 'Email', 'Error')
        errors_treeview = ttk.Treeview(
            error_toplevel,
            columns=columns,
            show='headings',
            selectmode='none',
        )   
        treeview_scroolbar_y = ttk.Scrollbar(
            error_toplevel,
            orient='vertical', 
            command=errors_treeview.yview,
        )
        treeview_scroolbar_x = ttk.Scrollbar(
            error_toplevel,
            orient='horizontal', 
            command=errors_treeview.xview,
        )
        button_exit = ttk.Button(
            error_toplevel,
            text='Exit',
            command=error_toplevel.destroy,
        )
        errors_treeview.configure(
            yscrollcommand=treeview_scroolbar_y.set,
            xscrollcommand=treeview_scroolbar_x.set,
        )

        errors_treeview.heading('Name', text='Name', anchor='w')
        errors_treeview.heading('Email', text='Email', anchor='w')
        errors_treeview.heading('Error', text='Error', anchor='w')
        errors_treeview.column('Name', minwidth=250, stretch=True)
        errors_treeview.column('Email', minwidth=300, stretch=True)
        errors_treeview.column('Error', minwidth=800, stretch=True)

        for message in messages:
            errors_treeview.insert('', 'end', values=message)

        errors_entry.pack(anchor='w')
        button_exit.pack(side='bottom', pady=6)
        treeview_scroolbar_y.pack(side='right', fill='y')
        treeview_scroolbar_x.pack(side='bottom', fill='x')
        errors_treeview.pack(fill='both', expand=True)
