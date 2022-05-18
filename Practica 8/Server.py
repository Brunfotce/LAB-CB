#!/usr/bin/env python3
import os
from ftplib import FTP, FTP_PORT, FTP_TLS, ftpcp
import ftplib
from typing import List


def save_file(con: FTP, remote_file_path: str, local_file_path: str):
    with open(local_file_path, "wb") as local_file:
        con.retrbinary(f"RETR {remote_file_path}", local_file.write)


def get_txt_file(con: FTP, file_path: str) -> List[str]:
    listado: List[str] = []
    con.retrlines(f"RETR {file_path}", listado.append)
    return listado


def list_folder(con: FTP, directory: str):
    print(directory)
    listado: List[str] = []
    con.retrlines(f"LIST {directory}", listado.append)
    return listado


def get_file_dir(con: FTP, directory: str):
    listado = list_folder(con, directory)
    return [file_info for file_info in listado if file_info.startswith("-")], [
        file_info for file_info in listado if not file_info.startswith("-")
    ]


def get_file_name(file_info: str) -> str:
    return "".join(file_info.split()[8:])





def connect_ftp(
    host: str, port: int = FTP_PORT, usr: str = "", pwd: str = "", save_path: str = ""
):  
    
    try:
        connection = FTP()
        connection.connect(host=host, port=port, timeout=3)
        connection.login(usr, pwd)
        print("Status: Conexion succed")
        connection.cwd("pub")
        nombreca="vault.centos.org"
        f=open("vault.centos.org","w")

        connection.cwd(f)
        print("\nWe are in :  " + connection.pwd() + "\n")
        connection.dir();
        archivos = connection.nlst('*.txt')
        for archivo in archivos [0:len(archivos)]:
            abrir = open(archivo, 'wb')
            connection.retrbinary(archivo, abrir.write)
            print("\nDLing files...")
            connection.close()
    except Exception as e:
        print ("An unexpected error ocurred, try again")
        connection.close()
        
if __name__ == "__main__":
    # http://www.ftp-sites.org/
    # connect_ftp('192.168.11.3', 8022)
    # connect_ftp(host="ftp.mirror.nl", save_path="/home/jhernandez/txt")
    connect_ftp(host="ftp.heanet.ie", save_path="/home/jhernandez/txt")