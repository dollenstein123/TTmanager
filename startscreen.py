from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import locale
import datetime
import entryscreen
import dbaccess
import myfunctions

complist = object


# a megkapott Comp egyedet feltölti az új verseny adataival
def newcomp(parent, competition):
    fr_newcomp = ttk.Frame(parent, relief="groove", padding="0.3i")
    fr_newcomp.grid(column=0, row=1, padx=10, pady=(10, 5), sticky="EW")

    # kezeli a tournament Combobox adatait
    def tournament_validate(name_tournament) -> str:
        if name_tournament not in dbaccess.tournaments():
            new_tournament = messagebox.askyesno(
                "Nem létező versenysorozat",
                "Felveszi új versenysorozatként: " + name_tournament,
            )
            if new_tournament:
                dbaccess.insert_new_tournament(name_tournament)
                tournament["values"] = dbaccess.tournaments()
                c_tournament_var.set(name_tournament)
            else:
                c_tournament_var.set("Egyedi verseny")
        compname.focus_set()

    # leellenőrzi, hogy írtak-e be versenynevet és az nem szerepel a mentett listában
    def compname_validate(cname: str):
        if len(cname) == 0:
            compname.focus_set()
            return False
        else:
            try:
                if dbaccess.isexists_comp(cname):
                    messagebox.showinfo("Létező versenynév", "Adj meg egy más nevet.")
                    compname.selection_range(0, END)
                    return False
                else:
                    compdate.focus_set()
                    return True
            except OSError:
                compdate.focus_set()
                return True

    # ellenőrzi a beírt dátum érvényességét
    def compdate_validate(cdate):
        try:
            datetime.datetime.strptime(cdate, "%Y.%m.%d")
            compdate.configure({"foreground": "black"})
            createcomp.focus_set()
            return True
        except ValueError:
            compdate.configure({"foreground": "red"})
            return False

    def compgroups_validate(cgroups):
        pass

    # ha érvényesek az adatok, feltölti a verseny példányát a megadott adatokkal
    def compcreation(cname, ctournament, cdate, cgroups, cplaces):
        global complist
        places_def = {
            "Nincs": "",
            "Főtábla": "M",
            "Főtábla-Vígaszág": "MR",
            "Főtábla-Vígaszcsoport": "MZ",
        }
        if compname_validate(cname) and compdate_validate(cdate):
            groups = ""
            for g in range(cgroups):
                groups += chr(g + 65)
            competition.startnewcomp(
                cname, ctournament, cdate, groups, places_def[cplaces]
            )
            myfunctions.fill_treeview(complist, dbaccess.compscontent())
            entryscreen.entry(parent.master, competition)
        else:
            messagebox.showwarning(
                "Nem megfelelő adatok",
                "Nem lehetett létrehozni a versenyt,\n"
                "mert nem jó valamelyik adat.\n"
                "Ellenőrizze a verseny nevét és dátumát!",
            )

    l_tournament = ttk.Label(
        fr_newcomp, text="A versenysorozat neve:", style="entry.TLabel"
    )
    c_tournament_var = StringVar()
    c_tournament_var.set("Vinolingua Kupa")
    tournament = ttk.Combobox(fr_newcomp, width=30, textvariable=c_tournament_var)
    tournament["values"] = dbaccess.tournaments()
    tournament.bind("<Return>", lambda e: tournament_validate(c_tournament_var.get()))
    tournament.bind("<<ComboboxSelected>>", lambda e: compname.focus_set())

    l_compname = ttk.Label(fr_newcomp, text="A verseny neve:", style="entry.TLabel")
    cname_var = StringVar()
    compname = ttk.Entry(
        fr_newcomp, width=50, style="big.TEntry", textvariable=cname_var
    )
    compname.bind("<Return>", lambda e: compname_validate(cname_var.get()))
    compname.focus_set()
    l_compdate = Label(fr_newcomp, text="A verseny időpontja:", style="entry.TLabel")
    cdate_var = StringVar()
    cdate_var.set(datetime.datetime.today().strftime("%Y.%m.%d"))
    compdate = Entry(fr_newcomp, width=12, style="date.TEntry", textvariable=cdate_var)
    compdate.bind("<Return>", lambda e: compdate_validate(compdate.get()))
    l_compgroups = ttk.Label(fr_newcomp, text="Csoportok száma:", style="entry.TLabel")
    cgroups_var = IntVar()
    cgroups_var.set(1)
    compgroups = ttk.Spinbox(
        fr_newcomp,
        from_=1,
        to=8,
        wrap=True,
        width=3,
        style="big.TSpinbox",
        textvariable=cgroups_var,
    )
    compgroups.bind("<Return>", lambda e: compgroups_validate(cgroups_var.get()))
    l_compplaces = ttk.Label(fr_newcomp, text="Helyosztó:", style="entry.TLabel")
    cplaces_var = StringVar()
    cplaces_var.set("Nincs")
    compplaces = ttk.Spinbox(
        fr_newcomp,
        values=("Nincs", "Főtábla", "Főtábla-Vígaszág", "Főtábla-Vígaszcsoport"),
        wrap=True,
        width=20,
        style="big.TSpinbox",
        textvariable=cplaces_var,
    )
    compgroups.bind("<Return>", lambda e: compgroups_validate(cplaces_var.get()))
    createcomp = Button(fr_newcomp, text="Új verseny létrehozása", style="blue.TButton")
    createcomp.bind(
        "<Return>",
        lambda e: compcreation(
            cname_var.get(),
            c_tournament_var.get(),
            cdate_var.get(),
            cgroups_var.get(),
            cplaces_var.get(),
        ),
    )
    createcomp.bind(
        "<Button-1>",
        lambda e: compcreation(
            cname_var.get(),
            c_tournament_var.get(),
            cdate_var.get(),
            cgroups_var.get(),
            cplaces_var.get(),
        ),
    )
    l_tournament.grid(column=0, row=0, sticky="E", padx=(20, 0), pady=(10, 10))
    l_compname.grid(column=0, row=1, sticky="E", padx=(20, 0), pady=(10, 10))
    l_compdate.grid(column=0, row=2, sticky="E", padx=(20, 0), pady=(10, 10))
    l_compgroups.grid(column=0, row=3, sticky="E", padx=(20, 0), pady=(10, 10))
    l_compplaces.grid(column=2, row=3, sticky="E", padx=(20, 0), pady=(10, 10))
    tournament.grid(column=1, row=0, columnspan=3, sticky="W")
    compname.grid(column=1, row=1, columnspan=3, sticky="W")
    compdate.grid(column=1, row=2, sticky="W")
    compgroups.grid(column=1, row=3, sticky="W")
    compplaces.grid(column=3, row=3, sticky="W")
    createcomp.grid(column=4, row=0, rowspan=3, padx=(30, 10))


# már elmentett versenyek adatait tölti be
def loadcomp(parent, competition):
    global complist
    fr_loadcomp = ttk.Frame(parent, relief="groove", padding="0.3i")
    fr_loadcomp.grid(column=0, row=2, padx=10, pady=(10, 5), sticky="EW")
    # rendezi a lista elemeit az adott oszlop alapján
    def sortby(tree, col, desc):
        data = [(tree.set(child, col), child) for child in tree.get_children("")]
        data.sort(reverse=desc)
        for indx, item in enumerate(data):
            tree.move(item[1], "", indx)
        tree.heading(col, command=lambda col=col: sortby(tree, col, int(not desc)))

    # betölti a kiválasztott, korábban elmentett verseny adatait
    def loadexists():
        if complist.selection():
            curitem = complist.focus()
            param = complist.item(curitem)["values"]
            competition.loadcomp(
                param[0], param[1], param[2], param[3], param[4], param[5], param[6]
            )
            if competition.status == "created":
                entryscreen.entry(parent.master, competition)

    l_complist = Label(fr_loadcomp, text="VERSENYEK", style="tree.TLabel")
    complist = ttk.Treeview(fr_loadcomp, style="my.Treeview")
    scrollbar_complist = Scrollbar(
        fr_loadcomp, orient="vertical", command=complist.yview
    )
    scrollbar_complist.config(command=complist.yview)
    myfunctions.fill_treeview(complist, dbaccess.compscontent())
    complist["columns"] = ["id", "Név", "Versenysorozat", "Dátum", "Állapot"]
    complist["displaycolumns"] = ["Név", "Versenysorozat", "Dátum", "Állapot"]
    complist["show"] = "headings"
    complist.column("Dátum", anchor=CENTER, width=120)
    complist.column("Állapot", anchor=CENTER, width=120)
    complist.column("Versenysorozat", anchor=CENTER)
    complist.heading("Név", text="Név", command=lambda c="Név": sortby(complist, c, 0))
    complist.heading(
        "Versenysorozat",
        text="Versenysorozat",
        command=lambda c="Versenysorozat": sortby(complist, c, 0),
    )
    complist.heading(
        "Dátum", text="Dátum", command=lambda c="Dátum": sortby(complist, c, 0)
    )
    complist.heading("Állapot", text="Állapot")
    complist.configure(yscrollcommand=scrollbar_complist.set)
    complist.bind("<Double-Button-1>", lambda e: loadexists())
    loadcomp = Button(
        fr_loadcomp, text="Verseny betöltése", style="tree.TButton", command=loadexists
    )

    l_complist.grid(column=0, row=0, columnspan=2)
    complist.grid(column=0, row=1)
    scrollbar_complist.grid(column=1, row=1, sticky="NS")
    loadcomp.grid(column=2, row=1, columnspan=2, padx=(30, 10))


if __name__ == "__main__":
    import screencfg
    import competition

    locale.setlocale(locale.LC_ALL, "hu-HU.utf8")
    root = Tk()
    root.title("Table Tennis Competiton Manager")
    # feltölti a stílus elemeit a screencfg modulból
    s = ttk.Style()
    screencfg.beallit(s)
    # létrehozza az induló képernyőt
    mainframe = ttk.Frame(root, style="main.TFrame")

    mainframe.grid(column=0, row=0)

    c = competition.Comp()
    newcomp(mainframe, c)
    loadcomp(mainframe, c)

    root.mainloop()
    print(c.cname, c.cdate, c.cdirname, c.cfirstround, c.csecondround, c.athletes)
