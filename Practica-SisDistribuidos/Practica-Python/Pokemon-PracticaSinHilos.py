import requests
from random import randint
import time

def get_pokemon_name():
	response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{randint(1, 151)}")
	if response.status_code == 200:
		result = response.json()
		name = result.get("forms")[0].get("name")
		print(name)

if __name__ == "__main__":
	start_time = time.time()

	# Secuencial
	for _ in range(5):
		get_pokemon_name()
	
	end_time = time.time()
	total_time = end_time - start_time
	print(f"El tiempo de ejecución fue de {total_time} segundos")