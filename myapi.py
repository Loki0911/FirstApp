import nlpcloud

class API:

    def __init__(self):
        self.__api = "your claudecode api key here"

    def language_detection(self,text):
            client = nlpcloud.Client("python-langdetect", self.__api, gpu=False)
            response = client.langdetection(text)
            return response