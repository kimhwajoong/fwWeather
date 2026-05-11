import requests

API_KEY = "f511c67f19fa06399c188312d2111baf" #<- api_key

url = f"https://api.openweathermap.org/data/2.5/weather?lat=37.5665&lon=126.9780&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

print("temp", data["main"]["temp"])
print("humy", data["main"]["humidity"])
print("winspd",data["wind"]["speed"])

