from deepface import DeepFace

class DeepFaceRecognition:
    def verify(self, img1_path, img2_path):
        result = DeepFace.verify(img1_path, img2_path)
        return result

# Exemple d'utilisation
if __name__ == "__main__":
    verifier = DeepFaceRecognition()
    result = verifier.verify("img1.jpg", "img2.jpg")
    print(result)
