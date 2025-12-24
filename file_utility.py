from pathlib import Path
import datetime
import os
import time

# --- Configuración Inicial ---
VERSION_ACTUAL = "1.0.0" 
DIR_DESTINO = Path(f"Backup_{VERSION_ACTUAL}")

# --- Funciones de Utilidad (Unidad 4) ---

def registrar_log(mensaje: str, ruta_log: Path):
    """
    [Implementación obligatoria - Tarea para Estudiante B / Issue #10]
    Escribe un mensaje con la marca de tiempo en el archivo de log.
    DEBE usar with open() para asegurar el cierre.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea_log = f"[{timestamp}] - {mensaje}\n"
    
    # 1. Implementar escritura en modo "append" ('a')
    # 2. Asegurar el uso de with open()
    pass # Implementación Pendiente


def crear_directorio_seguro():
    """
    [Implementación obligatoria - Tarea para Estudiante A / Issue #9]
    Crea el directorio de destino. DEBE CAPTURAR PermissionError.
    """
    print(f"Intentando crear directorio: {DIR_DESTINO.resolve()}")
    
    try:
        # 1. Intentar crear el directorio con exist_ok=True
        # 2. Si es exitoso, llamar a registrar_log()
        pass # Implementación Pendiente

    # 3. CAPTURAR ERROR ESPECÍFICO DE PERMISOS (Issue #9)
    except PermissionError:
        print(f"\n❌ ERROR CRÍTICO: No se tienen permisos para crear la carpeta en: {DIR_DESTINO.resolve()}")
        print("El programa NO puede continuar.")
        return False
    
    except Exception as e:
        print(f"\n❌ Error inesperado al crear directorio: {e}")
        return False
    
    return True

def transferir_archivos_simulado():
    """
    [Implementación obligatoria - Tarea para Estudiante A / Issue #11]
    Simula la copia de un archivo al directorio de destino.
    """
    if not crear_directorio_seguro():
        return

    # Simulación de un archivo para transferir
    archivo_simulado = Path("archivo_a_copiar.txt")
    if not archivo_simulado.exists():
        archivo_simulado.write_text("Este es el contenido del archivo de prueba.")
    
    ruta_destino_archivo = DIR_DESTINO / archivo_simulado.name
    
    print(f"\nSimulando copia de '{archivo_simulado.name}' a '{ruta_destino_archivo}'...")
    time.sleep(1) # Pausa para simular la operación
    
    # 1. Implementar la copia del archivo
    # 2. Llamar a registrar_log() para registrar la operación

    print("Funcionalidad de transferencia pendiente.") # Implementación Pendiente

# --- Bucle Principal del Programa ---

def main():
    print("==================================================")
    print(f" UTILIDAD DE GESTIÓN DE ARCHIVOS Y RUTA (UGAT) - v{VERSION_ACTUAL}")
    print("==================================================")
    print(f"Ruta de destino definida: {DIR_DESTINO.resolve()}")
    
    # Iniciar la operación
    transferir_archivos_simulado()

if __name__ == "__main__":
    main()