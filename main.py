import cv2
import torch
from ultralytics import YOLO
from pathlib import Path

def get_device():
    # Detecta automáticamente el mejor hardware disponible.
    if torch.cuda.is_available():
        return "cuda"       # NVIDIA GPU
    elif torch.backends.mps.is_available():
        return "mps"        # Apple Silicon (M1, M2, M3, M4)
    else:
        return "cpu"        # Por defecto

def main():
    # Configuración de rutas
    DIRECTORIO_BASE = Path(__file__).resolve().parent
    RUTA_MODELO = DIRECTORIO_BASE / "best.pt"

    if not RUTA_MODELO.exists():
        print(f"Error: No se encuentra el modelo en {RUTA_MODELO}")
        return

    # Selección de hardware y carga de modelo
    device = get_device()
    print(f"Ejecutando en: {device.upper()}")

    model = YOLO(str(RUTA_MODELO)).to(device)

    # Inicializar captura
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: No se pudo acceder a la cámara")
        return
    
    print("Detección iniciada. Presiona 'q' para salir.")
    
    while True:
        # Read frame from the video capture
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame")
            break

        # Inferencia optimizada
        # stream=True ayuda con la memoria, device asegura el hardware correcto    
        results = model(frame, device=device, stream=True, verbose=False, conf=0.5)
        
        # Process the results
        for result in results:
            boxes = result.boxes
            for box in boxes:
                # Print the raw box.xyxy[0] value
                # print("Raw box.xyxy[0]:", box.xyxy[0])
                # print("Type of box.xyxy[0]:", type(box.xyxy[0]))
                
                # Get box coordinates
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                
                # Print the coordinates
                # print(f"Coordendas de Bounding Box:")
                # print(f"Arriba-Izquierda: ({x1}, {y1})")
                # print(f"Debajo-Derecha: ({x2}, {y2})")
                # print(f"Ancho: {x2-x1}, Alto: {y2-y1}")
                # print("-" * 30)
                
                # Get confidence and class
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                class_name = model.names[cls]
                
                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) #frame, arriba izquierda, debajo derecha, color, grosor
                label = f"{class_name}: {conf:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Mostrar frame
        cv2.imshow('YOLO Object Detection', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
