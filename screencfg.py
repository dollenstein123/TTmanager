#A program által használt Widgetek stílusának definíciói
def beallit(s):
    s.configure('.', font='Helvetica 10', background='whitesmoke', foreground="black")
    s.configure('main.TFrame', padding=(3, 3, 12, 12))
    s.configure('title.TLabel', foreground="blue", font=('Helvetica', 16, 'bold'), padding=(5,30), anchor='center')
    s.configure('entry.TLabel', font='Helvetica 12 bold', padding=(1,5))
    s.configure('tree.TLabel', font='Helvetica 12 bold', padding=(1,5))
    s.configure('blue.TButton', foreground="black", background='blue', font='Helvetica 12 bold', padding=(5, 5))
    s.configure('tree.TButton', background='orange', font='Helvetica 12 bold', padding=(5, 5))

    s.element_create("plain.field", "from", "clam")
    s.layout("big.TEntry",
             [('Entry.plain.field', {'children': [(
                 'Entry.background', {'children': [(
                     'Entry.padding', {'children': [(
                         'Entry.textarea', {'sticky': 'nswe'})],
                         'sticky': 'nswe'})], 'sticky': 'nswe'})],
                 'border': '2', 'sticky': 'nswe'})])
    s.configure("big.TEntry", fieldbackground="lightyellow")

    s.layout("date.TEntry",
             [('Entry.plain.field', {'children': [(
                 'Entry.background', {'children': [(
                     'Entry.padding', {'children': [(
                         'Entry.textarea', {'sticky': 'nswe'})],
                         'sticky': 'nswe'})], 'sticky': 'nswe'})],
                 'border': '2', 'sticky': 'nswe'})])
    s.configure("date.TEntry", fieldbackground="lightyellow")