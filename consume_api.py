import requests

data = {
    "nombre": "Javier",
    "email": "javier@gmail.com",
    "ingresos": 100000,
    "egresos": 5000,
}

response = requests.put("http://127.0.0.1:5000/empresa/1", data=data)
# response = requests.get("http://127.0.0.1:5000/empresa/5")
# response = requests.post("http://127.0.0.1:5000/empresa/5")
# response = requests.patch("http://127.0.0.1:5000/empresa/5", data= data)
# response = requests.delete("http://127.0.0.1:5000/empresa/5")

print(response)
messajeJson = response.json()
print(messajeJson)
