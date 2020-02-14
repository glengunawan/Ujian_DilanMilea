import requests 
import json

url = "http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json" 
data = requests.get(url) 
daftarProvinsi = data.json() 

url = "http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json" 
data = requests.get(url) 
dataProvinsi = data.json() 

provinsiDilan = "BANTEN"
provinsiMilea = "JAWA BARAT" 

keysProvinsi = list(daftarProvinsi.keys())
valuesProvinsi = list(daftarProvinsi.values()) 

for i in valuesProvinsi: 
    if i == provinsiDilan: 
        kodeProvinsiDilan = keysProvinsi[valuesProvinsi.index(i)] 
        break

for i in valuesProvinsi: 
    if i == provinsiMilea: 
        kodeProvinsiMilea = keysProvinsi[valuesProvinsi.index(i)] 
        break

for i in dataProvinsi[str(kodeProvinsiDilan)]: 
    if i["urban"] == "SAMPORA" : 
        if i["sub_district"] == "CISAUK": 
            if i["city"] == "TANGERANG": 
                kodePosDilan = i["postal_code"]
                break

for i in dataProvinsi[str(kodeProvinsiMilea)]: 
    if i["urban"] == "CITARUM" : 
        if i["sub_district"] == "BANDUNG WETAN": 
            if i["city"] == "BANDUNG": 
                kodePosMilea = i["postal_code"]
                break
apikey = "AkaypVfrop7FofpXt7tATDTwPKmBM3Lx7NaBXlDnUyBAvgLrop78L2s0kkQvu4OJ" 
url = f"https://www.zipcodeapi.com/rest/{apikey}/distance.json/{kodePosDilan}/{kodePosMilea}/km " 

data = requests.get(url)
jarakJson = data.json() 
jarak = jarakJson["distance"] 

print(f"Kode Pos lokasi Dilan adalah {kodePosDilan}")
print(f"Kode Pos lokasi Milea adalah {kodePosMilea}")
print(f"Jarak Dilan & Milea adalah {jarak} km")