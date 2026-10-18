import platform
import socket
import os
import shutil
import subprocess
import psutil

print("=" * 50)
print("           WINDOWS PC INFORMATION")
print("=" * 50)

# Device Name
print(f"\nDevice Name: {socket.gethostname()}")

# Operating System
print(f"Operating System: {platform.system()}")
print(f"Windows Version: {platform.version()}")

# CPU
cpu = subprocess.check_output(
    'powershell "(Get-CimInstance Win32_Processor).Name"',
    shell=True,
    text=True
).strip()

print(f"Processor: {cpu}")

# CPU Cores
print(f"CPU Cores: {os.cpu_count()}")

# RAM
ram = round(psutil.virtual_memory().total / (1024**3), 2)
print(f"Installed RAM: {ram} GB")

# Python Version
print(f"Python Version: {platform.python_version()}")

# System Type
print(f"System Type: {platform.machine()}")

# Manufacturer
try:
    manufacturer = subprocess.check_output(
        'powershell "(Get-CimInstance Win32_ComputerSystem).Manufacturer"',
        shell=True,
        text=True
    ).strip()

    print(f"Manufacturer: {manufacturer}")
except:
    print("Manufacturer: Unable to detect")

# Model
try:
    model = subprocess.check_output(
        'powershell "(Get-CimInstance Win32_ComputerSystem).Model"',
        shell=True,
        text=True
    ).strip()

    print(f"Model: {model}")
except:
    print("Model: Unable to detect")

# GPU
try:
    gpu = subprocess.check_output(
        'powershell "(Get-CimInstance Win32_VideoController).Name"',
        shell=True,
        text=True
    ).strip()

    print(f"Graphics Card: {gpu}")
except:
    print("Graphics Card: Unable to detect")

# Storage
try:
    total, used, free = shutil.disk_usage("C:\\")

    print(f"\nDrive C:")
    print(f"  Total Storage: {round(total / (1024**3), 2)} GB")
    print(f"  Used Storage: {round(used / (1024**3), 2)} GB")
    print(f"  Free Storage: {round(free / (1024**3), 2)} GB")
except:
    print("Storage: Unable to detect")
try:
    edition = subprocess.check_output(
        'powershell "(Get-ComputerInfo).OsName"',
        shell=True,
        text=True
    ).strip()

    print(f"Windows Edition: {edition}")
except:
    print("Windows Edition: Unable to detect")
print("\n" + "=" * 50)
print("System check complete!")
print("=" * 50)