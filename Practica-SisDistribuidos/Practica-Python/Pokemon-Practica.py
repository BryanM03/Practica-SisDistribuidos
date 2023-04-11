import requests ## Instalar pip install requests
from random import randint
import threading
import time

def get_pokemon_name():
	response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{randint(1, 151)}")
	if response.status_code == 200:
		result = response.json()
		name = result.get("forms")[0].get("name")
		print(name)

if __name__ == "__main__":
	start_time = time.time()

	# Concurrente
	for _ in range(5):
		thread = threading.Thread(target=get_pokemon_name)
		thread.start()
	
	end_time = time.time()
	total_time = end_time - start_time
	print(f"El tiempo de ejecución fue de {total_time} segundos")



