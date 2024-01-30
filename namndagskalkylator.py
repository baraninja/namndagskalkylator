import math
from datetime import datetime, timedelta

def advanced_namnsdagskalkylator(namn):
    # Omvandla bokstäverna i namnet till siffror
    bokstav_till_siffra = {chr(i): i - 64 for i in range(65, 91)}
    bokstav_till_siffra['Å'] = 27
    bokstav_till_siffra['Ä'] = 28
    bokstav_till_siffra['Ö'] = 29

    # Beräkna summan och produkten av siffrorna
    siffra_summa = sum(bokstav_till_siffra[bokstav.upper()] for bokstav in namn if bokstav.upper() in bokstav_till_siffra)
    siffra_produkt = math.prod(bokstav_till_siffra[bokstav.upper()] for bokstav in namn if bokstav.upper() in bokstav_till_siffra)

    # Kombinera dessa värden
    kombinerat_värde = (siffra_summa + siffra_produkt) % 365

    # Normalisera resultatet med en sinuskurva för jämnare fördelning över året
    normalized_value = int((math.sin(kombinerat_värde / 365 * 2 * math.pi) + 1) / 2 * 365)

    return normalized_value

# Fråga användaren efter ett namn
namn_input = input("Ange ett namn för att beräkna dess namnsdag: ")

# Beräkna namnsdagens nummer
namnsdag_nummer = advanced_namnsdagskalkylator(namn_input)

# Konvertera numret till ett datum
namnsdag_datum = datetime(2024, 1, 1) + timedelta(days=namnsdag_nummer - 1)  # Justera för år 2024
print(f"Namnsdagen för {namn_input} är den {namnsdag_datum.strftime('%d %B')}.")
