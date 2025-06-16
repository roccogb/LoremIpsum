#!/usr/bin/env python3
import subprocess
import sys
import os

def run_command(command, description):
    """Ejecuta un comando y maneja errores"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completado")
        if result.stdout:
            print(f"   Salida: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {description}")
        print(f"   Código de error: {e.returncode}")
        if e.stderr:
            print(f"   Error: {e.stderr.strip()}")
        return False

def main():
    print("🚀 Iniciando proyecto Flask...")
    print("=" * 50)
    
    # Verificar que estamos en el directorio correcto
    if not os.path.exists("backend"):
        print("❌ No se encontró la carpeta 'backend'. Asegúrate de ejecutar este script desde la raíz del proyecto.")
        sys.exit(1)
    
    # Comando 1: Inicializar base de datos
    if not run_command("python3 backend/database/init_db.py", "Inicializando base de datos"):
        print("❌ Falló la inicialización de la base de datos. Abortando...")
        sys.exit(1)
    
    # Comando 2: Inicializar datos de prueba
    if not run_command("python3 -m tests.init_test_data", "Inicializando datos de prueba"):
        print("❌ Falló la inicialización de datos de prueba. Abortando...")
        sys.exit(1)
    
    # Comando 3: Ejecutar la aplicación Flask
    print("🌟 Iniciando servidor Flask...")
    print("=" * 50)
    try:
        # Cambiar al directorio backend y ejecutar app.py
        os.chdir("backend")
        subprocess.run("python3 app.py", shell=True, check=True)
    except subprocess.CalledProcessError:
        print("❌ Error al iniciar el servidor Flask")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido por el usuario")
        sys.exit(0)

if __name__ == "__main__":
    main()
