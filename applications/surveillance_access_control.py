import cv2

class SurveillanceSystem:
    def start_camera(self):
        cap = cv2.VideoCapture(0)
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Logique de détection de visage ici (par exemple, utiliser un détecteur de visage)
            cv2.imshow('Surveillance', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

# Exemple d'utilisation
if __name__ == "__main__":
    surveillance_system = SurveillanceSystem()
    surveillance_system.start_camera()
