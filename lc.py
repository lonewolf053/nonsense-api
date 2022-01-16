import requests

base_url = "https://love-calculator.p.rapidapi.com/getPercentage"
headers = {
    'x-rapidapi-host': "love-calculator.p.rapidapi.com",
    'x-rapidapi-key': "5dc36a308cmsh60fdfb30bbd33b7p10535ajsn1428dfa22744"
}

x = input("Enter name: ")
y = input("Enter name: ")
params = {'sname': x, 'fname': y}

response = requests.request("GET", base_url, headers=headers, params=params)
print("Percentage: ", response.json()['percentage'], "%")
print("Verdict: ", response.json()['result'])
