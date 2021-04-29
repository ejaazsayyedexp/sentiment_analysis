from tensorflow.keras.models import model_from_json
def load_model():
    path_to_model = './assets/model.json'
    path_to_weights = './assets/weights.h5'
    json_file = open(path_to_model,'r')
    model_data = json_file.read()
    json_file.close()
    model = model_from_json(model_data)
    model.load_weights(path_to_weights)

    print("Model loaded!")

    model.compile(loss="binary_crossentropy",optimizer='rmsprop',metrics=['accuracy'])
    return model