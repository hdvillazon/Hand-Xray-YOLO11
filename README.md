# Hand-Xray-YOLO11

Sistema de visión artificial especializado en la detección de estructuras óseas y articulaciones en radiografías de mano y muñeca, utilizando la arquitectura **YOLO11**.

El sistema está diseñado para procesar en tiempo real imágenes de placas radiográficas capturadas a través de una cámara web (ya sean placas físicas, o imágenes mostradas en monitores y dispositivos móviles).

## Clases detectadas
El modelo identifica 6 categorías anatómicas:
- **Articulaciones:** DIP, PIP, MCP.
- **Huesos/Regiones:** Radius, Ulna, Wrist.

## Requisitos
- **Python:** 3.10.
- **Hardware:** Cámara web (Para la detección de las radiografías).

## Instalación

### Opción 1: Con Conda
```bash
conda env create -f environment.yml
conda activate hand-xray-env
```

### Opción 2: Con Pip
Se recomienda el uso de un entorno virtual para mantener las dependencias aisladas.

1. Crear el entorno virtual:
```bash
python -m venv venv
```
2. Activar el entorno:
* En Windows: `venv\Scripts\activate`
* En Mac/Linux: `source venv/bin/activate`
3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso
1. Ejecuta el script principal:
```bash
python main.py
```
2. Coloca la radiografía (física o en pantalla) frente a la cámara para iniciar la detección.
3. Presiona 'q' para salir de la ventana de video.

## Detalles técnicos
* Modelo: YOLO11 Nano (yolo11n).
* Hardware: Soporte automático para CUDA (NVIDIA), MPS (Apple Silicon) y CPU.