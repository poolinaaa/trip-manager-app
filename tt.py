import requests

url = "https://timetable-lookup.p.rapidapi.com/TimeTable/BOS/LAX/20231217/"

headers = {
	"X-RapidAPI-Key": "25d7923676msh76e2082c55923c2p1744a9jsn5eb37ae457be",
	"X-RapidAPI-Host": "timetable-lookup.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())