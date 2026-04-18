# Hand-Xray-YOLO11

Sistema de visión artificial especializado en la detección de estructuras óseas y articulaciones en radiografías de mano y muñeca, utilizando la arquitectura **YOLO11**.

## Clases detectadas
El modelo identifica 6 categorías anatómicas:
- **Articulaciones:** DIP, PIP, MCP.
- **Huesos/Regiones:** Radius, Ulna, Wrist.

## Requisitos
- **Python:** 3.10
- **Hardware:** Cámara web para detección en tiempo real

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
Para iniciar la detección en tiempo real, ejecuta:

```bash
python main.py
```
Presiona 'q' para salir de la ventana de video.

## Detalles técnicos
* Modelo: YOLO11 Nano (yolo11n).
* Hardware: Soporte automático para CUDA (NVIDIA), MPS (Apple Silicon) y CPU.