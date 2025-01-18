import numpy as np
import tensorflow as tf
from keras.models import load_model

class FaceNet:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def get_embedding(self, face_image):
        face_image = np.expand_dims(face_image, axis=0)
        embedding = self.model.predict(face_image)
        return embedding[0]

# Exemple d'utilisation
if __name__ == "__main__":
    model_path = 'path/to/facenet_model.h5'
    facenet = FaceNet(model_path)
    # Charger une image de visage ici et l'utiliser pour obtenir l'embedding
