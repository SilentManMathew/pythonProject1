import json
import threading
import time
import requests

# Funkcja odpowiedzialna za pobieranie aktualnej ceny Bitcoina w dolarach
def get_bitcoin_price():
    while True:
        # Wysyłanie zapytania do API
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        # Parsowanie odpowiedzi i wyciąganie ceny z odpowiedzi
        data = json.loads(response.text)
        price = data['bpi']['USD']['rate_float']

        # Wypisanie ceny na ekran
        print(f"Aktualna cena Bitcoina: {price} USD")

        # Pause for 1 second
        time.sleep(1)

# Funkcja odpowiedzialna za wypisanie aktualnej daty i godziny
def print_current_time():
    while True:
        # Pobranie aktualnej daty i godziny
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

        # Wypisanie daty i godziny na ekran
        print(f"Aktualna data i godzina: {current_time}")

        # Pause for 10 seconds
        time.sleep(10)

# Utworzenie wątków
thread1 = threading.Thread(target=get_bitcoin_price)
thread2 = threading.Thread(target=print_current_time)

# Uruchomienie wątków
thread1.start()
thread2.start()
