# A program által használt Widgetek stílusának definíciói
def beallit(s):
    s.configure(".", font="Helvetica 10", background="whitesmoke", foreground="black")
    s.configure("main.TFrame", padding=(3, 3, 12, 12), background="whitesmoke")
    s.configure(
        "title.TLabel",
        foreground="blue",
        font=("Helvetica", 16, "bold"),
        padding=(5, 10),
        anchor="center",
    )
    s.configure("entry.TLabel", font="Helvetica 12 bold", padding=(1, 5))
    s.configure("tree.TLabel", font="Helvetica 12 bold", padding=(1, 5))
    s.configure("group.TButton", font="Helvetica 10 bold", padding=(1, 1))
    s.configure(
        "blue.TButton",
        foreground="black",
        background="blue",
        font="Helvetica 12 bold",
        padding=(5, 5),
    )
    s.configure(
        "tree.TButton", background="orange", font="Helvetica 12 bold", padding=(5, 5)
    )

    s.configure("big.TSpinbox", font="Helvetica 12 bold")

    s.element_create("plain.field", "from", "clam")
    s.layout(
        "big.TEntry",
        [
            (
                "Entry.plain.field",
                {
                    "children": [
                        (
                            "Entry.background",
                            {
                                "children": [
                                    (
                                        "Entry.padding",
                                        {
                                            "children": [
                                                ("Entry.textarea", {"sticky": "nswe"})
                                            ],
                                            "sticky": "nswe",
                                        },
                                    )
                                ],
                                "sticky": "nswe",
                            },
                        )
                    ],
                    "border": "2",
                    "sticky": "nswe",
                },
            )
        ],
    )
    s.configure("big.TEntry", fieldbackground="lightyellow")

    s.layout(
        "date.TEntry",
        [
            (
                "Entry.plain.field",
                {
                    "children": [
                        (
                            "Entry.background",
                            {
                                "children": [
                                    (
                                        "Entry.padding",
                                        {
                                            "children": [
                                                ("Entry.textarea", {"sticky": "nswe"})
                                            ],
                                            "sticky": "nswe",
                                        },
                                    )
                                ],
                                "sticky": "nswe",
                            },
                        )
                    ],
                    "border": "2",
                    "sticky": "nswe",
                },
            )
        ],
    )
    s.configure("date.TEntry", fieldbackground="lightyellow")
    s.element_create("my.Treeheading.border", "from", "default")
    s.layout(
        "my.Treeview.Heading",
        [
            ("my.Treeheading.cell", {"sticky": "nswe"}),
            (
                "my.Treeheading.border",
                {
                    "sticky": "nswe",
                    "children": [
                        (
                            "my.Treeheading.padding",
                            {
                                "sticky": "nswe",
                                "children": [
                                    (
                                        "my.Treeheading.image",
                                        {"side": "right", "sticky": ""},
                                    ),
                                    ("my.Treeheading.text", {"sticky": "we"}),
                                ],
                            },
                        )
                    ],
                },
            ),
        ],
    )
    s.map("my.Treeview.Heading", relief=[("active", "groove"), ("pressed", "sunken")])
    s.configure(
        "my.Treeview.Heading", font="Helvetica 10 bold", background="whitesmoke"
    )
    s.configure("my.Treeview.Heading", relief="groove")
