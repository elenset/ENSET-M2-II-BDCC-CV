import numpy as np
from arcface import ArcFace

class ArcFaceRecognition:
    def __init__(self, model_path):
        self.arcface_model = ArcFace(model_path)

    def get_embedding(self, face_image):
        return self.arcface_model.get_embedding(face_image)

# Exemple d'utilisation
if __name__ == "__main__":
    model_path = 'path/to/arcface_model.h5'
    arcface_recognition = ArcFaceRecognition(model_path)
    # Charger une image de visage ici et l'utiliser pour obtenir l'embedding
