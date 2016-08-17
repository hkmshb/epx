"""
Defines the forms that represents the GUI for ePinXtractr.
"""
import os
import epx
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import Directory

from fysom import Fysom
from epx.core import EPXEngine


TARGET_EXT = '.xml'


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
        self._define_fsm()
    
    def display(self):
        self.root.mainloop()
    
    def _init_widgets(self):
        # variables
        self.var_dirpath = StringVar()
        self.var_dirstats = StringVar()
        self.var_opsstats = StringVar()

        # row: 0
        Label(self.body, text="Directory to Process")\
            .grid(row=0, column=0, sticky=W)

        # row: 1
        txt_dirpath = Entry(self.body, textvariable=self.var_dirpath)
        btn_browse = Button(self.body, text="Browse...")

        txt_dirpath.grid(row=1, column=0, ipadx=2, ipady=2, padx=(0, 3))
        txt_dirpath.config(width=70, state=DISABLED)
        
        btn_browse.config(command=self._select_directory)
        btn_browse.grid(row=1, column=1)

        # row: 2
        iframe2 = Frame(self.body)
        self.var_dirstats.set("...")
        self.var_opsstats.set("...")

        iframe2.grid(row=3, column=0, columnspan=2, sticky='WE')
        Label(iframe2, text="Info: ").grid(row=0, column=0, sticky=W)
        Label(iframe2, textvariable=self.var_dirstats).grid(row=0, column=1)
        Label(iframe2, textvariable=self.var_opsstats, justify=CENTER)\
            .grid(row=0, column=2)
        
        btn_about = Button(iframe2, text='i', width=1)
        btn_about.config(command=self._show_about)
        btn_about.grid(row=0, column=3, padx=(0,1))

        btn_help = Button(iframe2, text='?', width=1)
        btn_help.config(command=self._show_help)
        btn_help.grid(row=0, column=4)
        iframe2.grid_columnconfigure(2, weight=1)

        # row: 3
        iframe3 = Frame(self.body)
        self.pbar = Progressbar(iframe3)
        #self.pbar.grid(row=0, column=0, ipady=1, padx=(0, 3), sticky='WE')

        btn_process = Button(iframe3, text='Process', command=self._manage_state)
        btn_process.grid(row=0, column=1)
        iframe3.grid_columnconfigure(0, weight=1)

        # widget refs added to self
        self.btn_process = btn_process
        self.btn_browse = btn_browse
        self.processbox = iframe3
    

    def _define_fsm(self):
        self._fsm = Fysom({
            'initial': {'state': 'start', 'event':'init', 'defer':True},
            'events': [
                ('process', 'start', 'processing'),
                ('cancel', 'processing', 'aborted'),
                ('done', 'processing', 'finished'),
                ('init', ['aborted', 'finished'], 'start'),
            ],
            'callbacks': {
                'onprocess': self._on_process,
                'oncancel': self._on_cancel,
                'ondone': self._on_done,
            }
        })

    def _toggle_processbox(self, show=True):
        if show:
            self.processbox.grid(row=2, column=0, pady=(3, 2), columnspan=2, sticky='WE')
        else:
            self.processbox.grid_forget()
    
    def _select_directory(self):
        self._cleanup_widgets()
        if self._fsm.can('init'):
            self._fsm.init()
        
        dirpath = Directory(self.root).show()
        self.var_dirpath.set(dirpath)
        if not dirpath:
            return
        
        # get directory content details
        detail_fmt = "sub-dirs: %s / files: %s / sms-files: %s"
        dirpath, dirnames, filenames = next(os.walk(dirpath))
        xmlfiles = [f for f in filenames if f.endswith(TARGET_EXT)]

        self.var_dirstats.set(detail_fmt % (
            len(dirnames), len(filenames), len(xmlfiles)))

        if not self.processbox.grid_info():
            self._toggle_processbox(True)
        
        # set process button state
        self.btn_process.config(state=DISABLED if len(xmlfiles) == 0 else NORMAL)

    def _cancel(self):
        pass
    
    def _manage_state(self):
        if self._fsm.isstate('start'):
            self._fsm.process()
        elif self._fsm.isstate('processing'):
            self._fsm.cancel()
        
    def _show_about(self):
        window = AboutDialog(self.root)
        window.transient(self.root)
    
    def _show_help(self):
        pass
    
    def _cleanup_widgets(self):
        self.var_dirstats.set('...')
        self.var_opsstats.set('...')
        self.btn_process.config(state=DISABLED)
        self.pbar.grid_forget()
    
    def _config_widget_for_result(self):
        self.btn_browse.config(state=NORMAL)
        self.btn_process.config(state=DISABLED, text="Process")
    
    def _on_process(self, e):
        self.btn_browse.config(state=DISABLED)
        self.btn_process.config(text='Cancel', state=NORMAL)
        self.var_opsstats.set('processing...')
        
        engine = EPXEngine(TARGET_EXT)
        result = engine.process(self.var_dirpath.get())
        engine.write_report(result)

        self.var_opsstats.set('done')
        self._fsm.done(result=result)
    
    def _on_cancel(self, e):
        self._config_widget_for_result()
        self.var_opsstats.set('aborted!')
    
    def _on_done(self, e):
        self._config_widget_for_result()
        self.var_opsstats.set(
            "[ p:%s / f:%s ]" % (len(e.result.passed), len(e.result.failed)))


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
        self.geometry("+%d+%d" % (self.parent.winfo_rootx()+85,
                                  self.parent.winfo_rooty()+10))
        self.wait_visibility()
        self.grab_set()
