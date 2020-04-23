# TTmanager
Asztalitenisz verseny lebonyolítását támogató alkalmazás

Legfeljebb két fázisú versenyt támogat. Mindenképpen csoportküzdelmekkel kezdődik. Ha a résztvevők száma alapján szükséges, a második fázisban egy lefeljebb 16 fős főtábla és vígaszágra van lehetőség. A második szakaszban a vígaszág helyett lehetőség van újabb csoportmérkőzéseket lebonyolítani. Ilyenkor az egymás ellen korábban lejátszott mérkőzéseket már nem rendezi meg újra, hanem átemeli az első körből.

Adatfájlok:
versenyek.comp - ez a szöveges fájl tartalmazza az alkalmazással elindított, illetve lebonyolított versenyek adatait: versenynév, dátum, fájlnév, státusz, első kör, második kör szerkezetben. A státusz értékei: created, started, finished. Az első körben a csoportok számát tárolja: ABCDEFGH (legfeljebb 8 csoport). A második körben: M-main, R-rest (ezek helyosztó jellegű táblák), valamint Z (ez a vígaszkör) lehetséges.
versenyfájlnév.athl - az adott versenyen részt vevő versenyzők neveit és sorszámait tartalmazza. A fájl szerkezete: azonosító, vezetéknév, keresztnév, helyezés
versenyfájlnáv.resu - az adott verseny során elért eredményeket tartalmazza. A fájl szerkezete: szakaszazonosító, sorszám, versenyző1 azonosító, versenyző2 azonosító, eremény (3-0, 3-1, 3-2, 0-3, 1-3, 2-3 alakban), szett (11-9,11-13, stb. alakban... ez utóbbi opcionális, csoportmérkőzéseken kötelező, a helyosztó táblákon nem szükséges)
