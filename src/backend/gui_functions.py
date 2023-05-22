import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk
from screeninfo import get_monitors  # Get the active monitor
import typing
import src.backend.backend as backend


def get_supported(filetypes: tuple[str, str | tuple[str]]) -> list[str]:
    supported = []
    for name, extension in filetypes:
        if isinstance(extension, tuple):
            for ext in extension:
                supported.append(ext)
        else:
            supported.append(extension)
    
    return supported


def import_file( 
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


def browse(stringvar: str, title: str, filetypes: str | None) -> None:
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


def set_geometry_popup(
    popup: tk.Tk | tk.Toplevel, 
    root: tk.Tk, 
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
