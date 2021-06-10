import requests

def main():
    s1 = "https://api.censusreporter.org/1.0/tabulation/01001"
    s2 = "http://embed.censusreporter.org.s3.amazonaws.com/1.0/data/profiles/2015/16000US1714000.json"
    response = requests.get(s2)
    
    if response.status_code != 200:
        print("Status Code: " , response.status_code)
        raise Exception("ERRRORR!")
    
    data = response.json()
    print("JSON data: " ,data )
    
if __name__ == "__main__":
    main()