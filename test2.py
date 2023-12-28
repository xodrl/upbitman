import pyupbit
import pandas as pd
import os

# GitHub Secrets에서 시크릿 키를 읽어오기
api_key = os.environ.get('API_KEY')
secret_key = os.environ.get('SECRET_KEY')

print(api_key)
