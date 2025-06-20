import re
import random as r
import string as str

def randomname(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def obfuscatecode(code: str) -> str:
    names = set(re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', code))
    blacklist = {'def', 'class', 'import', 'from', 'return', 'if', 'else', 'elif',
                 'for', 'while', 'in', 'with', 'as', 'try', 'except', 'pass',
                 'True', 'False', 'None', 'print', 'range', 'break', 'continue',
                 'and', 'or', 'not', 'is', 'lambda'}

    replace_map = {}
    for name in names:
        if name not in blacklist and not name.startswith("__"):
            replace_map[name] = randomname()

    for old, new in replace_map.items():
        code = re.sub(rf'\b{old}\b', new, code)

    junk_lines = ['\n' + random.choice([
        "pass", 
        "a = 123456", 
        "x = x", 
        "None == None", 
        '"junk" == "junk"'
    ]) for _ in range(10)]

    code += '\n' + '\n'.join(junk_lines)
    return code

def obfuscatefile(input_path: str, output_path: str):
    with open(input_path, "r", encoding="utf-8") as f:
        original = f.read()
    obfuscated = obfuscatecode(original)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(obfuscated)
    print(f"[+] Obfuscated file saved to {output_path}")

if __name__ == "__main__":
    obfuscatefile("../agent/client.py", "obf_client.py")
