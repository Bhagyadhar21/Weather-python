import requests
 
print("Welcome to the Weather Forecaster! ")
print("Enter the city name to watch the weather condition ")
 
city_name = input("Enter the name of the City : ")
print("\n\n")
 

def Gen_report(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    print(T)
     
Gen_report(city_name)
