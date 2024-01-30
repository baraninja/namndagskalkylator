# Namnsdagskalkylator

## Översikt
Detta Python-skript tillhandahåller en unik metod för att beräkna en "namnsdag" för ett givet namn baserat på en avancerad algoritm. Genom att använda en kombination av bokstavsvärdena i ett namn, omvandlar skriptet namnet till ett specifikt datum på året. Denna metod försöker säkerställa att varje namn får en mer eller mindre unik namnsdag.

## Användning
För att använda skriptet, kör det helt enkelt i din Python-miljö. Skriptet kommer att be dig ange ett namn och sedan automatiskt beräkna och visa namnsdagen för det namnet.

```
$ python namnsdagskalkylator.py
```

Exempel på körning i terminalen:
```
$ python namnsdagskalkylator.py 
Ange ett namn för att beräkna dess namnsdag: Anders 
Namnsdagen för Anders är den 15 April.
```

## Metod
Skriptet använder följande steg för att beräkna en namnsdag:
1. Konverterar varje bokstav i namnet till en numerisk motsvarighet (A=1, B=2, ..., Z=26, Å=27, Ä=28, Ö=29).
2. Beräknar både summan och produkten av dessa numeriska värden.
3. Kombinerar dessa värden och använder en sinuskurva för att normalisera resultatet över året.

Detta ger en mer jämn fördelning av namnsdagar genom året.

## Bidrag
Alla bidrag till detta projekt är välkomna. Om du har förslag på förbättringar eller vill rapportera buggar, vänligen skapa ett ärende eller pull-förfrågan.

## Licens
Detta projekt är licensierat under MIT-licensen.

