## Cara menginstall
- Clone Project

- Buat virtual environment untuk python
- Masuk direktori project
```
cd fis-diagnosa-diabetes-melitus-
python -m venv env
```
- Mengaktifkan vrtual environment python.
```
# linux
source env/bin/activate

# Windows
env\Scripts\Activate.ps1
```
- Download library python yang dibutuhkan
```
cd server
pip install -r requirement.txt
```
- Jalankan server
```
# Linux
python3 server.py

# Windows
python server.py
```
