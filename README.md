# Namnsdagskalkylator

## Översikt
Detta Python-skript tillhandahåller en unik metod för att beräkna en "namnsdag" för ett givet namn. Skriptet söker först efter namnet i en fördefinierad lista med namnsdagar. Om namnet inte finns i listan, används en avancerad kalkylator för att generera ett namnsdagsdatum.

## Användning
Kör skriptet och ange ett namn när du uppmanas. Skriptet kommer antingen att returnera den officiella namnsdagen för namnet, om det finns, eller generera en namnsdag baserat på en unik algoritm.

```
$ python namnsdagskalkylator.py
```

Exempel på körning i terminalen:
```
$ python namnsdagskalkylator.py 
Ange ett namn för att beräkna dess namnsdag: Anders 
Namnsdagen för Anders är den 30 november.
```
## Funktionalitet
- Söker efter officiella namnsdagar i en fördefinierad JSON-fil.
- Genererar ett namnsdagsdatum för namn som inte finns i listan, med hjälp av en unik algoritm baserad på bokstavsvärden och matematiska beräkningar.

## Beräkningsmetod för Namnsdagar

För namn som inte finns med i den officiella listan över namnsdagar använder skriptet en unik algoritm för att generera ett namnsdagsdatum. Processen är följande:

### Steg 1: Konvertera Bokstäver till Numeriska Värden
Varje bokstav i namnet konverteras till ett numeriskt värde. Detta görs enligt den engelska alfabetets ordning där 'A' = 1, 'B' = 2, och så vidare upp till 'Z' = 26. De svenska bokstäverna 'Å', 'Ä' och 'Ö' tilldelas värdena 27, 28 respektive 29.

### Steg 2: Beräkna Summan och Produkten av Värdena
Algoritmen beräknar två nyckeltal från namnet:
   - **Summa:** Totalen av alla numeriska värden som motsvarar bokstäverna i namnet.
   - **Produkt:** Produkten av alla numeriska värden (dvs. resultatet av att multiplicera alla värden).

### Steg 3: Kombinera och Normalisera Värdet
Summan och produkten kombineras genom addition. Det kombinerade värdet normaliseras sedan för att fördela namnsdagarna jämnare över året. Detta görs genom att applicera en sinuskurva, vilket resulterar i ett värde mellan 0 och 365.

### Steg 4: Konvertera Värdet till ett Datum
Det slutliga värdet representerar en dag på året. För att omvandla detta till ett faktiskt datum, räknas antalet dagar från årets början (1 januari) med hjälp av Python's `datetime`-bibliotek.

Denna metod garanterar att varje unikt namn tilldelas en konsekvent och unik namnsdag. Det är dock viktigt att notera att dessa datum inte följer traditionella namnsdagar och är helt genererade av algoritmen.

Detta ger en mer jämn fördelning av namnsdagar genom året.

## JSON-Datafil
Officiella namnsdagar lagras i en JSON-fil (`namnsdagar.json`). Denna fil innehåller en mappning av datum till namn för varje månad.

## Bidrag
Alla bidrag till detta projekt är välkomna. Om du har förslag på förbättringar eller vill rapportera buggar, vänligen skapa ett ärende eller pull-förfrågan.

## Licens
Detta projekt är licensierat under MIT-licensen.

