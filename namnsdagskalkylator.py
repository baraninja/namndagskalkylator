import math
from datetime import datetime, timedelta
import json

# Läs in namnsdagar från en fil
with open('namnsdagar.json', 'r') as file:
    namnsdagar_dict = json.load(file)

# Uppslagslista för månadsöversättningar
månadsnamn = {
    "January": "Januari",
    "February": "Februari",
    "March": "Mars",
    "April": "April",
    "May": "Maj",
    "June": "Juni",
    "July": "Juli",
    "August": "Augusti",
    "September": "September",
    "October": "Oktober",
    "November": "November",
    "December": "December"
}


def advanced_namnsdagskalkylator(namn):
    bokstav_till_siffra = {chr(i): i - 64 for i in range(65, 91)}
    bokstav_till_siffra['Å'] = 27
    bokstav_till_siffra['Ä'] = 28
    bokstav_till_siffra['Ö'] = 29

    siffra_summa = sum(
        bokstav_till_siffra[bokstav.upper()] for bokstav in namn if bokstav.upper() in bokstav_till_siffra)
    siffra_produkt = math.prod(
        bokstav_till_siffra[bokstav.upper()] for bokstav in namn if bokstav.upper() in bokstav_till_siffra)

    kombinerat_värde = (siffra_summa + siffra_produkt) % 365
    normalized_value = int((math.sin(kombinerat_värde / 365 * 2 * math.pi) + 1) / 2 * 365)

    return normalized_value


def hitta_officiell_namnsdag(namn, namnsdagar_dict):
    namn_lower = namn.lower()  # Konvertera det inmatade namnet till små bokstäver
    for month, days in namnsdagar_dict.items():
        for day, names in days.items():
            if names and namn_lower in [name.lower() for name in names]:  # Jämför med namn i små bokstäver
                return f"{day} {month}"
    return None


def hitta_namnsdag(namn, namnsdagar_dict):
    officiell_namnsdag = hitta_officiell_namnsdag(namn, namnsdagar_dict)
    if officiell_namnsdag:
        dag, månad = officiell_namnsdag.split()
        månad_svenska = månadsnamn[månad.capitalize()]
        return f"Den officiella namnsdagen för {namn} är den {dag} {månad_svenska}."
    else:
        namnsdag_nummer = advanced_namnsdagskalkylator(namn)
        namnsdag_datum = datetime(2024, 1, 1) + timedelta(days=namnsdag_nummer - 1)
        månad_svenska = månadsnamn[namnsdag_datum.strftime('%B')]
        return f"Den inofficiella namnsdagen för {namn} är den {namnsdag_datum.strftime(f'%d {månad_svenska}')}."


while True:
    namn_input = input("Ange ett namn för att beräkna dess namnsdag (eller skriv 'Quit' för att avsluta): ")
    if namn_input.lower() == 'quit':
        print("Programmet avslutas.")
        break
    namnsdag_meddelande = hitta_namnsdag(namn_input, namnsdagar_dict)
    print(namnsdag_meddelande)
