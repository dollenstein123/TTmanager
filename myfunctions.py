from tkinter import *

# feltölti friss adatokkal a TreeView-t
def fill_treeview(treeview, content):
    items = treeview.get_children()
    if items != {}:
        for item in items:
            treeview.delete(item)
    treeview.delete()
    index = iid = 0
    for item in content:
        treeview.insert("", index, iid, values=item)
        index = iid = index + 1
