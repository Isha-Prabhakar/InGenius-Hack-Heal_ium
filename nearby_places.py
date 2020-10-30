import requests


class GetNearbyHospitals(object):

    def __init__(self, lat, long):
        self.URL = "https://discover.search.hereapi.com/v1/discover"
        self.lat = lat 
        self.long = long
        self.api_key = '<YOUR_API_KEY_HERE>'
        self.query = 'hospitals'
        self.limit = 5
        self.PARAMS = {
                    'apikey':self.api_key,
                    'q':self.query,
                    'limit': self.limit,
                    'at':'{},{}'.format(self.lat,self.long)
                } 


    def retrieve_places(self):
        get_r = requests.get(url = self.URL, params = self.PARAMS) 
        data = get_r.json()
        return data

    def get_hospital_one(self):
        data = self.retrieve_places()
        hospital = data['items'][0]['title']
        hospital_address =  data['items'][0]['address']['label']
        print("Hospital 1 Details -")
        print("")
        print("Name:", hospital)
        print("Address:", hospital_address)
        print("")

    def get_hospital_two(self):
        data = self.retrieve_places()
        hospital = data['items'][1]['title']
        hospital_address =  data['items'][1]['address']['label']
        print("Hospital 2 Details -")
        print("")
        print("Name:", hospital)
        print("Address:", hospital_address)
        print("")

    def get_hospital_three(self):
        data = self.retrieve_places()
        hospital = data['items'][2]['title']
        hospital_address =  data['items'][2]['address']['label']
        print("Hospital 3 Details -")
        print("")
        print("Name:", hospital)
        print("Address:", hospital_address)
    

    def get_hospital_four(self):
        data = self.retrieve_places()
        hospital = data['items'][3]['title']
        hospital_address =  data['items'][3]['address']['label']
        print("Hospital 4 Details -")
        print("")
        print("Name:", hospital)
        print("Address:", hospital_address)

    
    def get_hospital_five(self):
        data = self.retrieve_places()
        hospital = data['items'][4]['title']
        hospital_address =  data['items'][4]['address']['label']
        print("Hospital 5 Details -")
        print("")
        print("Name:", hospital)
        print("Address:", hospital_address)




