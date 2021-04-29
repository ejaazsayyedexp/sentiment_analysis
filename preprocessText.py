import re
from nltk.corpus import stopwords


def preprocess_text(text):
    stop_words = list(set(stopwords.words('english')))
    text = text.lower()
    text = re.sub('\<br \/\>','',text)
    text = re.sub('[^a-zA-Z]',' ',text)
    text = re.sub('\'','',text)
    text = re.sub('\"','',text)
    text = re.sub('\\\\','',text)
    text = text.split(" ")
    newtext = []
    for x in text:
        if(x not in stop_words):
            if(x!=' '):
                if(len(x)>2):
                    newtext.append(x)
    text = ' '.join(newtext)
    return text



