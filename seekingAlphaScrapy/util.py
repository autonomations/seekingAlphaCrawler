from textblob import TextBlob

class Util(object):

    def __init__(self):
        pass

    def sentimentAnalysis(self, text):
        blob = TextBlob("ITP is a two-year graduate program good located in the Tisch School of the Arts. "
                "Perhaps the best way to describe great us is as a Center for the Recently Possible.")
        print(blob.sentiment)

