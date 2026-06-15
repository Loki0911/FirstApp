import nlpcloud

class API:

    def __init__(self):
        self.__api = "your nlpcloud api key here"

    def language_detection(self,text):
            client = nlpcloud.Client("python-langdetect", self.__api, gpu=False)
            response = client.langdetection(text)
            return response

    def ner_analysis(self,text,search):
         client = nlpcloud.Client("gpt-oss-120b", self.__api, gpu=True)
         response = client.entities(text, searched_entity = search)
         return response

    def sentiment_analysis(self,text):
         client = nlpcloud.Client("gpt-oss-120b", self.__api, gpu=True)
         response = client.sentiment(text,target="NLP Cloud") 
         return response