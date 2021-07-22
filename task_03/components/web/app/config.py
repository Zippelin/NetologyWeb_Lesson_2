import os

adr = os.getenv('hostip')
POSTGRE_URI = f'postgresql://admin:admin@{adr}:5432/web_01'