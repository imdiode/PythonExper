from cryptography.fernet import Fernet
import os
from pathlib import Path

default_path = Path("/home/Diode/Dicot/VisionIOT/main")

if not os.path.exists(default_path):
    os.makedirs(default_path)
    filen = os.path.join(default_path, "app.dat")
    open(filen, 'w').close()
    forread = open(filen)
    content = forread.read()
    forread.close()
    appsetting = open(filen, 'w')
    k_ey = Fernet.generate_key()
    appsetting.write(content + "\nsecretKey: " + str(k_ey))
    appsetting.close()