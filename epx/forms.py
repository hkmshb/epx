"""
Defines the forms that represents the GUI for ePinXtractr.
"""
import epx
from tkinter import *
from tkinter.ttk import *



class ePinXtractr(object):
    TITLE = epx.__name__
    
    def __init__(self, root=None):
        super(ePinXtractr, self).__init__()
        root.title(self.TITLE)
        root.resizable(0, 0)
        self.root = root

        self.body = Frame(root)
        self.body.grid(row=0, column=0, padx=10, pady=10)
        self._init_widgets()
    
    def display(self):
        self.root.mainloop()

    def _init_widgets(self):
        # variables
        self.var_dirpath = StringVar()
        self.dir_stats = StringVar()
        self.ops_stats = StringVar()

        # row: 0
        Label(self.body, text="Directory to Process")\
            .grid(row=0, column=0, sticky=W)

        # row: 1
        txt_dirpath = Entry(self.body, textvariable=self.var_dirpath)
        btn_browse = Button(self.body, text="Browse...")

        txt_dirpath.grid(row=1, column=0, ipadx=2, ipady=2, padx=(0, 5))
        txt_dirpath.config(width=55, state=DISABLED)
        
        btn_browse.grid(row=1, column=1)
        btn_browse.config(command=self._select_directory)

        # row: 2
        iframe2 = Frame(self.body)
        self.dir_stats.set("...")
        self.ops_stats.set("...")
        iframe2.grid_columnconfigure(2, weight=1)

        iframe2.grid(row=3, column=0, columnspan=2, sticky='WE')
        Label(iframe2, text="Info: ").grid(row=0, column=0, sticky=W)
        Label(iframe2, textvariable=self.dir_stats).grid(row=0, column=1)
        Label(iframe2, textvariable=self.ops_stats, justify=RIGHT)\
            .grid(row=0, column=2, padx=5, sticky=E)
        
        btn_about = Button(iframe2, text="?", command=self._show_about)
        btn_about.config(width=1)
        btn_about.grid(row=0, column=3, sticky=E)

        # non-displayed widgets
        self.pbar = Progressbar(self.body)
    
    def _toggle_progressbar(self, show=True):
        if show:
            self.pbar.grid(row=2, column=0, pady=(5,2), columnspan=2, sticky='WE')
        else:
            self.pbar.grid_forget()

    def _select_directory(self):
        if not self.pbar.grid_info():
            self._toggle_progressbar()
        else:
            self._toggle_progressbar(False)
    
    def _show_about(self):
        window = AboutDialog(self.root)
        window.transient(self.root)


class AboutDialog(Toplevel):
    
    def __init__(self, parent):
        super(AboutDialog, self).__init__(parent)
        self.parent = parent
        self._init_widgets()
        self._re_position()

    def _init_widgets(self):
        self.body = Frame(self)
        self.body.grid(row=0, column=0, padx=10, pady=10)

        font_family = 'Trebuchet MS'
        font_title = (font_family, 14, 'bold')
        font_ver = (font_family, 9, 'bold')

        Label(self.body, text=ePinXtractr.TITLE, font=font_title)\
            .grid(row=0, column=1, sticky=W)
        Label(self.body, text="1.0", font=font_ver)\
            .grid(row=1, column=1, sticky=W, pady=(0, 10))
        
        Label(self.body, text="%s is developed with <3 by" % epx.__name__)\
            .grid(row=2, column=1, sticky=W)
        Label(self.body, text=epx.__author__, foreground="blue")\
            .grid(row=2, column=2, sticky=W)
        Label(self.body, text=self._get_contact_info())\
            .grid(row=3, column=1, columnspan=2, sticky=W)
    
    def _get_contact_info(self):
        return "%(author_url)s | %(author_email)s | %(author_mobile)s" % { 
            'author_url': epx.__author_url__, 
            'author_email': epx.__author_email__,
            'author_mobile': epx.__author_mobile__
        }

    def _re_position(self):
        self.geometry("+%d+%d" % (self.parent.winfo_rootx()+50,
                                  self.parent.winfo_rooty()+10))
        self.wait_visibility()
        self.grab_set()
