import requests
import json
import jsonpath

class DevTest():
    def __init__(self,url):
        self.url=url

#Post Request test:
    def postRequest(self):
        # Read iput Json file
        file = open('C:\\Users\\Gajanan\\devtest\\CreateUser.json', 'r')
        json_input = file.read()
        request_json = json.loads(json_input)

        # Post request with json input body
        response = requests.post(self.url, request_json)

        # validating response code for +ve testing
        assert response.status_code == 201

        # Festch header from response
        print(response.headers.get('Content-Length'))

        # Parse response to json format
        response_json = json.loads(response.text)

        # pick id using json Path
        id = jsonpath.jsonpath(response_json, 'id')
        print(id[0])

#Put Request test:
    def putRequest(self):
        # Read iput Json file
        file = open('C:\\Users\\Gajanan\\Desktop\\CreateUser.json', 'r')
        json_input = file.read()
        request_json = json.loads(json_input)

        # Put request with json input body
        response = requests.put(self.url, request_json)

        # validating response code
        assert response.status_code == 200

        # Parse response to json format
        response_json = json.loads(response.text)

        # pick id using json Path
        updated_user = jsonpath.jsonpath(response_json, 'updatedAt')
        print(updated_user[0])

#Delete Request test:
    def deleteRequest(self):
        # Delete user
        response = requests.delete(self.url)

        # Fetch response code
        print(response.status_code)

        # validating response code for testing
        assert response.status_code == 204

#Get request test
    def getRequest(self):
        # Send get request
        response = requests.get(self.url)

        # Parse response to json format
        response_json = json.loads(response.text)
        print(response_json)

        # validating response code
        assert response.status_code == 200

        # fetch the value using json Path
        pages = jsonpath.jsonpath(response_json,'total_pages')
        print(pages[0])

        # validating code for testing
        assert pages[0]== 2


test=DevTest("https://reqres.in/api/users?page=2")
test.postRequest()
test.putRequest()
test.deleteRequest()
test.getRequest()

