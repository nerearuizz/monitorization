#!/usr/bin/env python

import os
import json
import subprocess

# Configurar la red a escanear
network = "172.16.60."  # Cambia esto por la red de tu red local

# Realizar un escaneo de la red para obtener las IPs activas
def scan_network():
    active_hosts = []
    for i in range(20, 25):  # Escanear del 1 al 254
        ip = f"{network}{i}"
        response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")  # Hacer un ping
        if response == 0:
            active_hosts.append(ip)
    return active_hosts

# Generar el inventario en formato JSON para Ansible
def generate_inventory():
    active_hosts = scan_network()
    inventory = {
        "all": {
            "hosts": active_hosts
        }
    }
    print(json.dumps(inventory))  # Imprimir el inventario en formato JSON

if __name__ == "__main__":
    generate_inventory()
