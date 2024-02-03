import math
from datetime import datetime, timedelta
import json

def read_namnsdagar_file(file_path):
    """Reads and returns the contents of the namnsdagar JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: The file was not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: File is not a valid JSON.")
        return {}

def map_characters_to_numbers():
    """Maps Swedish alphabet characters to their respective numbers, including Å, Ä, and Ö."""
    return {chr(i): i - 64 for i in range(65, 91)} | {'Å': 27, 'Ä': 28, 'Ö': 29}

def advanced_namnsdagskalkylator(namn, bokstav_till_siffra):
    """Calculates a pseudo-random day for a given name based on character values."""
    siffra_summa = sum(bokstav_till_siffra.get(bokstav.upper(), 0) for bokstav in namn)
    siffra_produkt = math.prod(bokstav_till_siffra.get(bokstav.upper(), 1) for bokstav in namn)
    kombinerat_värde = (siffra_summa + siffra_produkt) % 365
    normalized_value = int((math.sin(kombinerat_värde / 365 * 2 * math.pi) + 1) / 2 * 365)
    return normalized_value

def hitta_officiell_namnsdag(namn, namnsdagar_dict):
    """Finds the official name day for a given name from the namnsdagar dictionary."""
    namn_lower = namn.lower()
    for month, days in namnsdagar_dict.items():
        for day, names in days.items():
            if namn_lower in [name.lower() for name in names]:
                return f"{day} {month}"
    return None

def månadsnamn_till_svenska():
    """Provides a dictionary mapping English month names to Swedish."""
    return {
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

def hitta_namnsdag(namn, namnsdagar_dict):
    """Determines and returns the name day for a given name, either official or calculated."""
    officiell_namnsdag = hitta_officiell_namnsdag(namn, namnsdagar_dict)
    månadsnamn = månadsnamn_till_svenska()
    if officiell_namnsdag:
        dag, månad = officiell_namnsdag.split()
        return f"Den officiella namnsdagen för {namn} är den {dag} {månadsnamn[månad]}."
    else:
        bokstav_till_siffra = map_characters_to_numbers()
        namnsdag_nummer = advanced_namnsdagskalkylator(namn, bokstav_till_siffra)
        namnsdag_datum = datetime(2024, 1, 1) + timedelta(days=namnsdag_nummer - 1)
        return f"Den inofficiella namnsdagen för {namn} är den {namnsdag_datum.day} {månadsnamn[namnsdag_datum.strftime('%B')]}."

def main():
    namnsdagar_dict = read_namnsdagar_file('namnsdagar.json')
    while True:
        namn_input = input("Ange ett namn för att beräkna dess namnsdag (eller skriv 'Quit' för att avsluta): ")
        if namn_input.lower() == 'quit':
            print("Programmet avslutas.")
            break
        namnsdag_meddelande = hitta_namnsdag(namn_input, namnsdagar_dict)
        print(namnsdag_meddelande)
