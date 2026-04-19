# Hand-Xray-YOLO11

Sistema de visión artificial especializado en la detección de estructuras óseas y articulaciones en radiografías de mano y muñeca, utilizando **YOLO11**.

El sistema está diseñado para procesar en tiempo real radiografías físicas o digitales mediante captura directa de cámara.

## Clases detectadas
El modelo está entrenado para identificar las siguientes estructuras:

| ID |Clase | Descripción |
| :--- | :--- | :--- |
| 0 | DIP | Articulación Interfalángica Distal |
| 1 | MCP | Articulación Metacarpofalángica |
| 2 | PIP | Articulación Interfalángica Proximal |
| 3 | Radius | Radio |
| 4 | Ulna | Cúbito |
| 5 | Wrist | Muñeca |

## Requisitos del sistema
* **Python:** 3.10.x.
* **Hardware:** Cámara web.

## Instalación

### 1. Configuración del entorno
#### **Opción A: Virtualenv (venv)**

**1. Crear el entorno:**

```bash
python3.10 -m venv venv
```

**2. Activar el entorno:**

| Sistema operativo | Comando de activación |
| :--- | :-- |
| Windows (PowerShell) | `.\venv\Scripts\Activate.ps1` |
| Windows (CMD) | `venv\Scripts\activate.bat` |
| Mac / Linux | `source venv/bin/activate`|

#### **Opción B: Conda (Recomendado)**

**1. Crear el entorno:**
```bash
conda create -n hand-xray python=3.10 -y
```

**2. Activar el entorno:**
```bash
conda activate hand-xray
```

### 2. Instalación de dependencias
#### **Apple Silicon (Chips M1, M2, M3, M4)**

Requiere Pytorch Nightly para soporte total de la GPU (MPS):
```bash
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
pip install ultralytics opencv-python
```

#### **NVIDIA GPU (CUDA)**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install ultralytics opencv-python
```

#### **Solo CPU**
```bash
pip install torch torchvision torchaudio
pip install ultralytics opencv-python
```

## Ejecución
1. Ejecuta el script principal:
```bash
python main.py
```
2. Coloca la radiografía (física o en pantalla) frente a la cámara para iniciar la detección.
3. Presiona 'q' para salir de la ventana de video.

## Detalles técnicos
* Modelo: YOLO11 Nano (yolo11n).
* Hardware: Soporte automático para CUDA (NVIDIA), MPS (Apple Silicon) y CPU.