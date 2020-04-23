from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import locale
import datetime
import screencfg


def compscontent():#beolvassa a tárolt versenyek adatait
    try:
        with open('versenyek.comp') as f:
            cc = [line.strip().split(',') for line in f]
    except OSError:
        cc = []
    return cc


def newcomp(parent, competition):#a megkapott Comp egyedet feltölti az új verseny adataival
    def compname_validate(cname):#leellenőrzi, hogy írtak-e be versenynevet és az nem szerepel a mentett listában
        if len(cname) == 0:
            compname.focus_set()
            return False
        else:
            try:
                savedcomps = [i[0] for i in compscontent()]
                if cname in savedcomps:
                    messagebox.showinfo('Létező versenynév', 'Adj meg egy más nevet.')
                    compname.selection_range(0, END)
                    return False
                else:
                    compdate.focus_set()
                    return True
            except OSError:
                compdate.focus_set()
                return True


    def compdate_validate(cdate):#ellenőrzi a beírt dátum érvényességét
        try:
            datetime.datetime.strptime(cdate, '%Y.%m.%d')
            compdate.configure({'foreground': 'black'})
            createcomp.focus_set()
            return True
        except ValueError:
            compdate.configure({'foreground': 'red'})
            return False

    def compcreation(cname, cdate):#ha érvényesek az adatok, feltölti a verseny példányát a megadott adatokkal
        if compname_validate(cname) and compdate_validate(cdate):
            competition.startnewcomp(cname, cdate)
        else:
            messagebox.showwarning('Nem megfelelő adatok', 'Nem lehetett létrehozni a versenyt,\nmert nem jó valamelyik adat.\nEllenőrizze a verseny nevét és dátumát!')


    l_compname = ttk.Label(parent, text='A verseny neve:', style='entry.TLabel')
    cname_var = StringVar()
    compname = ttk.Entry(parent, width=50, style='big.TEntry', textvariable=cname_var)
    compname.bind('<Return>', lambda e: compname_validate(cname_var.get()))
    compname.focus_set()
    l_compdate = Label(parent, text='A verseny időpontja:', style='entry.TLabel')
    cdate_var = StringVar()
    cdate_var.set(datetime.datetime.today().strftime('%Y.%m.%d'))
    compdate = Entry(parent, width=12, style='date.TEntry', textvariable=cdate_var)
    compdate.bind('<Return>', lambda e: compdate_validate(compdate.get()))
    createcomp = Button(parent, text='Új verseny létrehozása', style='blue.TButton')
    createcomp.bind('<Return>', lambda e: compcreation(cname_var.get(), cdate_var.get()))
    createcomp.bind('<Button-1>', lambda e: compcreation(cname_var.get(), cdate_var.get()))
    l_compname.grid(column=0, row=0, sticky='E', padx=(20, 0), pady=(10,10))
    l_compdate.grid(column=0, row=1, sticky='E', padx=(20, 0), pady=(10,10))
    compname.grid(column=1, row=0, sticky='W')
    compdate.grid(column=1, row=1, sticky='W')
    createcomp.grid(column=2, row=0, rowspan=2, padx=(30, 10))


def loadcomp(parent, competition):#már elmentett versenyek adatait tölti be
    def fill_complist():#feltölti friss adatokkal a TreeView-t
        index = iid = 0
        for item in compscontent():
            complist.insert('', index, iid, values=item)
            index = iid = index + 1

    def sortby(tree, col, desc):#rendezi a lista elemeit az adott oszlop alapján
        data = [(tree.set(child, col), child) for child in tree.get_children('')]
        data.sort(reverse=desc)
        for indx, item in enumerate(data):
            tree.move(item[1], '', indx)
        tree.heading(col, command=lambda col=col: sortby(tree, col, int(not desc)))

    def loadexists():#betölti a kiválasztott, korábban elmentett verseny adatait
        if complist.selection():
            curitem = complist.focus()
            param = complist.item(curitem)['values']
            competition.loadcomp(param[0], param[1], param[2], param[3], param[4], param[5])

    l_complist = Label(parent, text='VERSENYEK', style='tree.TLabel')
    complist = ttk.Treeview(parent)
    scrollbar_complist = Scrollbar(parent, orient='vertical', command=complist.yview)
    scrollbar_complist.config(command=complist.yview)
    fill_complist()
    complist['columns'] = ['Név', 'Dátum', 'Fájlnév', 'Állapot']
    complist['displaycolumns'] = ['Név', 'Dátum', 'Állapot']
    complist['show'] = 'headings'
    complist.column("Dátum", anchor=CENTER, width=120)
    complist.column("Állapot", anchor=CENTER, width=120)
    complist.heading('Név', text='Név', command=lambda c='Név': sortby(complist, c, 0))
    complist.heading('Dátum', text='Dátum', command=lambda c='Dátum': sortby(complist, c, 0))
    complist.heading('Állapot', text='Állapot')
    complist.configure(yscrollcommand=scrollbar_complist.set)
    loadcomp = Button(parent, text='Verseny betöltése', style='tree.TButton', command=loadexists)

    l_complist.grid(column=0, row=0, columnspan=2)
    complist.grid(column=0, row=1)
    scrollbar_complist.grid(column=1, row=1, sticky='NS')
    loadcomp.grid(column=2, row=1, columnspan=2, padx=(30, 10))


if __name__ == '__main__':
    import competition

    locale.setlocale(locale.LC_ALL, 'hu-HU.utf8')
    root = Tk()
    root.title('Table Tennis Competiton Manager')
#feltölti a stílus elemeit a screencfg modulból
    s = ttk.Style()
    screencfg.beallit(s)
#létrehozza az induló képernyő két frame-jét
    fr_newcomp = ttk.Frame(root, relief='groove', padding='0.3i')
    fr_loadcomp = ttk.Frame(root, relief='groove', padding='0.3i')

    fr_newcomp.grid(column=0, row=0)
    fr_loadcomp.grid(column=0, row=1)

    c = competition.Comp()
    newcomp(fr_newcomp, c)
    loadcomp(fr_loadcomp, c)


    root.mainloop()
    print(c.cname, c.cdate, c.cfilename, c.cfirstround, c.csecondround, c.athletes)