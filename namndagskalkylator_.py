def namnsdagskalkylator(namn):
    # Omvandla bokstäverna i namnet till siffror
    bokstav_till_siffra = {chr(i): i - 64 for i in range(65, 91)}
    bokstav_till_siffra['Å'] = 27
    bokstav_till_siffra['Ä'] = 28
    bokstav_till_siffra['Ö'] = 29

    # Beräkna summan av siffrorna
    siffra_summa = sum(bokstav_till_siffra[bokstav.upper()] for bokstav in namn if bokstav.upper() in bokstav_till_siffra)

    # Använd summan för att bestämma en dag på året
    dag_på_året = siffra_summa % 365  # 365 dagar på ett normalt år

    # Justera för skottår (efter den 28 februari)
    if dag_på_året > 59:  # 59 är den 28 februari (59:e dagen på året)
        dag_på_året += 1  # Justera för den extra dagen i skottår

    return dag_på_året

# Exempelanvändning
namn = input("Ange ett namn för att beräkna dess namnsdag: ")
namnsdag_nummer = namnsdagskalkylator(namn)

# Konvertera dagnummer till datum (kan behöva ytterligare justering för olika år)
from datetime import datetime, timedelta
namnsdag_datum = datetime(2024, 1, 1) + timedelta(days=namnsdag_nummer - 1)  # Justering för år 2024
print(f"Namnsdagen för {namn} är den {namnsdag_datum.strftime('%d %B')}.")
