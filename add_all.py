import random
from datetime import datetime
import hmac
import hashlib
from tkinter import W
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64
import json
import requests
now = datetime.now()
from random import randint
from dotenv import load_dotenv
import os 

load_dotenv()
#unchanged variables
apiKey = os.environ.get('apiKey')
apiSecret = os.environ.get('apiSecret')
submitAccount = "server1"
reviewUuid = os.environ.get('reviewUuid')
targetDeviceUuid = os.environ.get('dispatchWallet')
approveUuid = os.environ.get('approveUuid')
collect_wallet = os.environ.get('collectWallet')
#changing variables
dispatch_wallet = {'MATIC':"0.01", "SOL":"0.0012", "DASH":"0.01", "LTC":"0.001", "ZEC":"0.00102", "BCH":"0.02", "BNB":"0.02", "BTC":"0.0005", "DOGE":"30", "ETH":"0.001", "FTM":"1", "HT":"0.1", "OKT":"0.1", "TRX":"100", "XDAI":"0.0001", "ETC":"0.05", "ADA":"10"}

def signature(key, msg):
    key=bytes(key,'utf-8')
    msg = msg.encode()
    return hmac.new(key, msg, hashlib.sha256).hexdigest()

def import_private_key(filename):
    with open(filename, "rb") as file:
        private_key = RSA.importKey(file.read())
    return private_key

def get_sign(message):
    keypair = import_private_key('s_key.pem') #Private RSA key
    message = bytes(message, 'utf-8') # convert to bytes from string
    h = SHA256.new(message) # encrypt with sha256
    sign = pkcs1_15.new(keypair).sign(h) # sign with RSA
    return base64.b64encode(sign).decode("utf-8") # get the final output in base 64

def transaction(data, apiSecret):
    final_sign = signature(apiSecret, json.dumps(data).replace(" ", ""))
    ver1 = json.dumps(data).replace(" ", "").replace('"', '\"')
    content = {}
    content['data']= ver1
    content['sign'] = final_sign
    r = json.dumps(content)
    return json.loads(r)

def add_and_send(chain_selected, amount_to_send):
    list_of_add = []
    rand = randint(1,10)
    print("Random number generated is",rand,', chain is: ', chain_selected)
    timestamp_str = str(round(datetime.timestamp(now)))
    data_to_sign_collect = {"apiKey":apiKey,"chain":chain_selected,"timestamp":timestamp_str,"targetDeviceUuid":collect_wallet}
    for x in range (0,rand):
        url = 'https://open.coinsdo.com/coinsdo/open/v1/addressGet'
        x = requests.post(url, json = transaction(data_to_sign_collect, apiSecret))
        print(json.loads(x.text)["data"]["address"])
        list_of_add.append(json.loads(x.text)["data"]["address"])
    for i in list_of_add: ## executing the dispatch 
        businessId = i.encode('utf-8').hex()[:4]+'_'+i[-5:]
        approver2 = str('businessId='+businessId+'&'+'deviceUuid='+targetDeviceUuid)
        approver1 = str('businessId='+businessId+'&'+'address='+i+'&'+'amount='+amount_to_send+'&'+'currency='+chain_selected+'&'+'flag='+chain_selected)
        approve1_sign = get_sign(approver1)
        approve2_sign = get_sign(approver2)
        data_to_sign = {"apiKey":apiKey,"submitAccount":"server1","address":i,"amount":float(amount_to_send),"currency":chain_selected,"flag":chain_selected,"businessId":businessId,"timestamp":timestamp_str,"reviewUuid":reviewUuid,"reviewSign":approve1_sign,"targetDeviceUuid":targetDeviceUuid,"approveUuid":approveUuid,"approveSign":approve2_sign}
        url = 'https://open.coinsdo.com/coinsdo/open/v1/withdraw'
        k = requests.post(url, json = transaction(data_to_sign, apiSecret))
        print(k.text)

for x in list(dispatch_wallet.keys()):
    add_and_send(x, dispatch_wallet[x])
