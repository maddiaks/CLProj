# {
#     "client": {
#         "clientId": "yourcompanyname",
#         "clientVersion": "1.5.2"
#     },
#     "threatInfo": {
#         "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
#         "platformTypes": ["WINDOWS"],
#         "threatEntryTypes": ["URL"],
#         "threatEntries": [
#             {"url": "http://www.urltocheck1.org/"},
#             {"url": "http://www.urltocheck2.org/"},
#             {"url": "http://www.urltocheck3.com/"}
#         ]
#     }
# }
import json
class CLResponse:
    def __init__(self):
        self.clientVersion = "1.0"
        self.threatInfo = {
            'threatTypes': [],
            'threatEntries': [],
            'active': True
        }

    def to_JSON(self):
        return json.dumps(self.__dict__, indent=4)


if __name__ == "__main__":
    result = CLResponse()
    print(result.to_JSON())