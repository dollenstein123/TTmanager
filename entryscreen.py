from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import datetime
import dbaccess
import myfunctions

ath = {}
entry_num = 0


def entry(parent, competition):
    def new_athlete(firstname, surname, pick, tournament):
        if dbaccess.add_to_ranklist(firstname, surname, pick, entry_num, tournament):
            ath["entry"].append((surname + " " + firstname + " " + pick, entry_num))
            myfunctions.fill_treeview(ranklist, ath["entry"])
        else:
            messagebox.showinfo(
                "Nem megfelelő adatok", "Nem sikerült felvenni a versenyzőt."
            )

    def entry_add(group):
        remove = []
        for item in ranklist.selection():
            ath[group].append(ath["entry"][int(item)])
            remove.append(ath["entry"][int(item)])
        ath["entry"] = [item for item in ath["entry"] if item not in remove]
        myfunctions.fill_treeview(ranklist, ath["entry"])
        myfunctions.fill_treeview(tv[group], ath[group])

    def entry_remove(group):
        remove = []
        for item in tv[group].selection():
            remove.append(ath[group][int(item)])
        ath[group] = [item for item in ath[group] if item not in remove]
        for item in remove:
            ath["entry"].append(item)
        ath["entry"].sort(key=lambda x: x[1])
        myfunctions.fill_treeview(ranklist, ath["entry"])
        myfunctions.fill_treeview(tv[group], ath[group])

    def save_config(competition, ath):
        dbaccess.delete_old_datas(competition.id)
        if competition.status == "created":
            competition.ath = ath
            for group in competition.firstround:
                for number, item in enumerate(ath[group], start=1):
                    dbaccess.store_players(competition.id, item[1], group, number)

    def exit():
        save_config(competition, ath)
        entryscreen.destroy()
        entryscreen.update()

    entryscreen = Toplevel(parent)
    parent.withdraw()

    fr_main = Frame(entryscreen, style="main.TFrame")
    fr_title = Frame(fr_main, style="main.TFrame")
    fr_ranklist = Frame(fr_main, style="main.TFrame")
    fr_groups = Frame(fr_main, style="main.TFrame")

    b_back = Button(fr_title, text="Vissza", style="blue.TButton", command=exit)
    b_start = Button(fr_title, text="Verseny indítása", style="blue.TButton")
    l_tournament = Label(
        fr_title, text=competition.tournament + " nevezés", style="title.TLabel"
    )
    l_compname = Label(fr_title, text=competition.name, width=30, style="title.TLabel")
    l_compdate = Label(
        fr_title,
        text=datetime.datetime.strptime(competition.date, "%Y.%m.%d").strftime(
            "%Y. %B %d."
        ),
        width=30,
        style="title.TLabel",
    )
    l_ranglista = ttk.Label(fr_ranklist, text="Nevezettek", style="tree.TLabel")

    ranklist = Treeview(fr_ranklist, style="my.Treeview", height=30)
    ath = dbaccess.read_players(competition.id)
    ath.update({"entry": dbaccess.athletes(competition.tournament)})
    entry_num = len(ath["entry"]) + 1
    for group in competition.firstround:
        ath["entry"] = [item for item in ath["entry"] if item not in ath[group]]
    myfunctions.fill_treeview(ranklist, ath["entry"])
    ranklist["columns"] = ["Név", "Hely"]
    ranklist["displaycolumns"] = ["Hely", "Név"]
    ranklist["show"] = "headings"
    ranklist.column("Hely", width=40)
    ranklist.heading("Hely", text="Hely")
    ranklist.column("Név", width=160)
    ranklist.heading("Név", text="Név")
    scrollbar_ranklist = Scrollbar(
        fr_ranklist, orient="vertical", command=ranklist.yview
    )
    scrollbar_ranklist.config(command=ranklist.yview)
    ranklist.configure(yscrollcommand=scrollbar_ranklist.set)
    sn = StringVar()
    sn.set("Vezetéknév")
    surname = Entry(fr_ranklist, width=30, textvariable=sn)
    surname.bind("<FocusIn>", lambda e: surname.selection_range(0, END))
    surname.bind(
        "<Return>",
        lambda e: surname.focus_set()
        if (sn.get() == "" or sn.get() == "Vezetéknév")
        else firstname.focus_set(),
    )
    fn = StringVar()
    fn.set("Keresztnév")
    firstname = Entry(fr_ranklist, width=20, textvariable=fn)
    firstname.bind("<FocusIn>", lambda e: firstname.selection_range(0, END))
    firstname.bind(
        "<Return>",
        lambda e: firstname.focus_set()
        if (fn.get() == "" or fn.get() == "Keresztnév")
        else pickname.focus_set(),
    )
    pn = StringVar()
    pn.set("Egyéni")
    pickname = Entry(fr_ranklist, width=10, textvariable=pn)
    pickname.bind("<FocusIn>", lambda e: pickname.delete(0, END))
    pickname.bind("<Return>", lambda e: b_addname.focus_set())
    b_addname = Button(fr_ranklist, text="Új versenyző", style="group.TButton")
    b_addname.bind(
        "<Button-1>",
        lambda e: new_athlete(fn.get(), sn.get(), pn.get(), competition.tournament),
    )
    b_addname.bind(
        "<Return>",
        lambda e: new_athlete(fn.get(), sn.get(), pn.get(), competition.tournament),
    )

    fr_main.grid(column=0, row=0, sticky="NWES")
    fr_title.grid(column=0, row=0, columnspan=2, pady=(5, 10))
    fr_ranklist.grid(column=0, row=1, sticky="NS")
    fr_groups.grid(column=1, row=1, sticky="NEW")
    b_back.grid(column=0, row=0, sticky="W", padx=10)
    b_start.grid(column=2, row=0, sticky="E", padx=10)
    l_tournament.grid(column=1, row=0)
    l_compname.grid(column=0, row=1, sticky="E")
    l_compdate.grid(column=2, row=1, sticky="W")
    l_ranglista.grid(column=0, row=0)
    ranklist.grid(column=0, row=1, pady=(5, 20), padx=(10, 0))
    scrollbar_ranklist.grid(column=1, row=1, sticky=NS, pady=(5, 20), padx=(0, 10))
    surname.grid(column=0, row=2, columnspan=2, sticky="W", padx=10, pady=2)
    firstname.grid(column=0, row=3, columnspan=2, sticky="W", padx=10, pady=2)
    pickname.grid(column=0, row=4, columnspan=2, sticky="W", padx=10, pady=2)
    b_addname.grid(column=0, row=5, columnspan=2, pady=(5, 20))

    for item in competition.firstround:
        if item not in ath:
            ath.update({item: []})  # sportolók azonosítója és neve csoportonként
    tv = {}  # a csoportok widgetjei
    bu_add = {}  # a csoportok hozzáadó gombjai
    bu_del = {}  # a csoportok törlő gombjai
    lb = {}  # a csoportok címkéi
    sb = {}  # a csoportok görhető mezői
    gr_count = 0
    for group in competition.firstround:
        lb[group] = Label(fr_groups, text=group + " csoport", style="tree.TLabel")
        tv[group] = Treeview(fr_groups, style="my.Treeview", height=13)
        tv[group]["columns"] = ["Név", "Hely"]
        tv[group]["displaycolumns"] = ["Név"]
        tv[group]["show"] = "headings"
        tv[group].column("Név", width=200)
        tv[group].heading("Név", text="Név")
        sb[group] = Scrollbar(fr_groups, orient="vertical", command=tv[group].yview)
        sb[group].config(command=tv[group].yview)
        tv[group].configure(yscrollcommand=sb[group].set)
        myfunctions.fill_treeview(tv[group], ath[group])
        bu_add[group] = Button(
            fr_groups,
            text="Hozzáad",
            style="group.TButton",
            command=lambda group=group: entry_add(group),
        )
        bu_del[group] = Button(
            fr_groups,
            text="Kivesz",
            style="group.TButton",
            command=lambda group=group: entry_remove(group),
        )
        lb[group].grid(
            column=(gr_count % 4) * 3,
            row=(gr_count // 4) * 3,
            columnspan=3,
            sticky="N",
            pady=5,
        )
        tv[group].grid(
            column=(gr_count % 4) * 3,
            row=(gr_count // 4) * 3 + 1,
            columnspan=2,
            sticky="NE",
            padx=(3, 0),
            pady=(3, 5),
        )
        sb[group].grid(
            column=(gr_count % 4) * 3 + 2,
            row=(gr_count // 4) * 3 + 1,
            sticky="SNW",
            padx=(0, 3),
            pady=(3, 5),
        )
        bu_add[group].grid(
            column=(gr_count % 4) * 3,
            row=(gr_count // 4) * 3 + 2,
            sticky="N",
            pady=5,
            padx=2,
        )
        bu_del[group].grid(
            column=(gr_count % 4) * 3 + 1,
            row=(gr_count // 4) * 3 + 2,
            sticky="N",
            pady=5,
            padx=2,
        )
        gr_count += 1

    parent.wait_window(entryscreen)
    parent.update()
    parent.deiconify()
