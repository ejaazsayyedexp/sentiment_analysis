from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
import numpy as np


def load_word_index():
    word_index = imdb.get_word_index()
    return word_index


def encode_text(text):
    MAXLEN = 200
    word_index = load_word_index()
    
    text = [word_index[word] if word in word_index else 0 for word in text.split(" ")]
    text = sequence.pad_sequences([text],MAXLEN)[0]
    return text

def decode_text(integers):
    PAD = 0 
    word_index = load_word_index()
    reverse_word_index = {value:key for (key,value) in word_index.items()}
    text=""
    for nums in integers:
        if(nums!=PAD):
            text+=reverse_word_index[nums]+" "
    return text[:-1]

def predict(model, text):
    MAXLEN = 200
    encoded_text = encode_text(text)
    pred = np.zeros((1,MAXLEN))
    pred[0] = encoded_text
    result = model.predict(pred)
    return result[0][0]










