import dbaccess


class Competition:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.tournament = ""
        self.date = ""
        self.status = ""  # crerated, started, closed
        self.firstround = "A"
        self.secondround = ""
        self.athletes = {}
        self.matches = {}  # [number, group, player1_id, player2_id, result, sets]

    def startnewcomp(
        self, cname: str, ctournament: str, cdate: str, cmain: str, crest: str
    ):
        self.name = cname
        self.tournament = ctournament
        self.date = cdate
        self.status = "created"
        self.firstround = cmain
        self.secondround = crest
        dbaccess.insert_newcomp(self)

    def loadcomp(
        self,
        id: int,
        cname: str,
        tournament: str,
        cdate: str,
        cstatus: str,
        cfirstround: str,
        csecondround: str,
    ):
        self.id = id
        self.name = cname
        self.tournament = tournament
        self.date = cdate
        self.status = cstatus
        self.firstround = cfirstround
        self.secondround = csecondround


if __name__ == "__main__":
    import datetime

    c = Competition()
    cdate = datetime.date.today()
    c.startnewcomp("1. verseny", cdate.strftime("%Y.%m.%d"))
