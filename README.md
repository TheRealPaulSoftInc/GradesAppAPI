# GradesApp 
## Install dependencies
```bash
pip install -r ./requirements.txt
```
## Configure .env file
In order to run locally, you must create a .env file on the root folder and set these configurations:
```bash
SECRET_KEY=A$$S0M3-$3CR3T-K3Y
DEBUG=1
ALLOWED_HOSTS=localhost 127.0.0.1 
CORS_ALLOWED_ORIGINS=http://localhost http://127.0.0.1 

DB_LOCAL_NAME=gradesappdb
DB_LOCAL_USER=sa
DB_LOCAL_PASSWORD=password
DB_LOCAL_HOST=localhost
```
## Docker
```bash
docker build . -t gradesapp
docker run -p 8000:8000 gradesapp
```
