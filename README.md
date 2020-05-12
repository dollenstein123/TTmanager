# TTmanager
Asztalitenisz verseny lebonyolítását támogató alkalmazás

Legfeljebb két fázisú versenyt támogat. Mindenképpen csoportküzdelmekkel kezdődik. Ha a résztvevők száma alapján szükséges, a második fázisban egy lefeljebb 16 fős főtábla és vígaszágra van lehetőség. A második szakaszban a vígaszág helyett lehetőség van újabb csoportmérkőzéseket lebonyolítani. Ilyenkor az egymás ellen korábban lejátszott mérkőzéseket már nem rendezi meg újra, hanem átemeli az első körből.

A rendszer fájlok:
ttmanager.db 		- az adatbázist tartalmazza
dbaccess.py			- az adatbázihoz hozzáférést igénylő függvények
screencfg.py		- a program által használt stílusokat definiálja
myfunctions.py	-	a rendszer függvényei által több helyen is használt általános rutinok
start.py				- ezzel indul az alkalmazás
competition.py	- az osztály definíciója
startscreen.py	- a kezdőképernyőt kezelő függvények
entryscreen.py	- a nevezéseket kezelő és a versenyt elindító függvények

A jelenlegi állapotban versenyek létrehozása, és azok konfigurálása oldható meg.
A következő lépés a verseny elindítása lesz.
Sorsolás
Első körös csoportmérkőzések lejátszása
Második körös helyosztók és csoportmérkőzések levezénylése.
Ranglista kezelés és verseny lezárás.