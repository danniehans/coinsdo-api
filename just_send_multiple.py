import random
from datetime import datetime
import hmac
import hashlib
from tkinter import W
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import base64
import json
import requests
now = datetime.now()
from random import randint
import time


#unchanged variables
apiKey = "c96bc07dceb84437"
apiSecret = "306a50f556ca4d7f82c084a3e260da34"
apiKey2 = "6807d0b1614f4f3b"
apiSecret2 = "3f3a79e6330840288f083f1a3b04d227"
submitAccount = "api"
reviewUuid = "58E51634-3269-44AF-8351-F9506E2A4A6F"
targetDeviceUuid = "4A76D3E2-43C4-4E91-AFA0-F4D7A7842CDC"
approveUuid = "58E51634-3269-44AF-8351-F9506E2A4A6F"
collect_wallet = "B65EB9AC-75DB-4B08-A84A-1C70349E61E8"
#changing variables

ada = {"amount":"10", "address":"addr_test1qptys73efk7utcnlpendudw0wp8hchhq447zcufxx8kc8gjxsp6cm5ng23985u0qhugpexetesa6y8w3nnr7pkheg2csgxr7w7", "flag":"ADA"}
bch = {"amount":"0.012", "address":"bchtest:qzc0k3j8a8gq3egaw4n7xxd6eanp9vehnuwcu4teup", "flag":"BCH"}
bnb = {"amount":"0.021", "address":"0x917455f2f5ed2ef7edfeced6e9ad88221379037c", "flag":"BNB"}
btc = {"amount":"0.00051", "address":"mwCyvUYvnUXvnJs5P1AS5vYhpzuVMV6aPt", "flag":"BTC"}
dash = {"amount":"0.011", "address":"yhMVascjpNpQD5pqBvHxnmAAjh1mtGzAxy", "flag":"DASH"}
doge = {"amount":"10", "address":"nrH6vTNodKEU8hti3wT3rx59md3rNbDcMp", "flag":"DOGE"}
eos = {"amount":"2", "address":"dandanmian23","flag":"EOS"}
etc = {"amount":"0.051","address":"0x6181bb8a514695253183f93bdd4e3e1ff82fe088", "flag":"ETC"}
eth = {"amount":"0.001", "address":"0x40ea01ce6b380153ca330cd500dcc4480d6b9bd6", "flag":"ETH"}
ftm = {"amount":"1.1", "address":"0xde081271459976375eaa5db5f2ff7928121ae51c", "flag":"FTM"}
ht = {"amount":"0.1", "address":"0x533cfccc58ceb64f9eb5fcb49be0d716adbfd7f3", "flag":"HT"}
etc = {"amount":"0.05", "address":"0xa18d879d3c93e94480515e33f407a5a9917bc9f6", "flag":"ETC"}
ltc = {"amount":"0.0016", "address":"muWCY6fGsPP6byYJ5W5PAf6ZnCRS59hX78", "flag":"LTC"}
matic = {"amount":"0.02", "address":"0x893e2ff9ef46133bbf4fbd4be8392223842b8038", "flag":"MATIC"}
okt = {"amount":"0.16", "address":"0xd68295fb8875254227669496bab56f438ebbbcb8", "flag":"OKT"}
sol = {"amount":"0.0012", "address":"9AtARPDdL4MvzmrLY3T6EaxeJjXRzrBs9QCH9kkoonGd", "flag":"SOL"}
trx = {"amount":"100", "address":"TAe5SfcPvjF6fN7NeAjMEzMQTSuQn8QG1D", "flag":"TRX"}
xdai = {"amount":"0.0001", "address":"0x380a051a751c609778a53233e08c4f0b712cd3e8", "flag":"XDAI"}
xrp = {"amount":"100", "address":"r4iWMTvmN9rAMAvWdWWV2MpqCJXVbsZfqg", "flag":"XRP"}
zec = {"amount": "0.00102", "address":"tmVPjay6ZeRYw52J5fv9KvAvM6Pt5qsJJfk", "flag":"ZEC"}
list_to_send = [sol]
def signature(key, msg):
    key=bytes(key,'utf-8')
    msg = msg.encode()
    return hmac.new(key, msg, hashlib.sha256).hexdigest()

def import_private_key(filename):
    with open(filename, "rb") as file:
        private_key = RSA.importKey(file.read())
    return private_key

def get_sign_dispatch(message):
    keypair = import_private_key('s_key2.pem') #Private RSA key
    message = bytes(message, 'utf-8') # convert to bytes from string
    h = SHA256.new(message) # encrypt with sha256
    sign = pkcs1_15.new(keypair).sign(h) # sign with RSA
    return base64.b64encode(sign).decode("utf-8") # get the final output in base 64


def transaction_dispatch(data, apiSecret2):
    final_sign = signature(apiSecret2, json.dumps(data).replace(" ", ""))
    ver1 = json.dumps(data).replace(" ", "").replace('"', '\"')
    content = {}
    content['data']= ver1
    content['sign'] = final_sign
    r = json.dumps(content)
    return json.loads(r)


for y in range(7):
    
    for x in list_to_send:
        timestamp_str = str(round(datetime.timestamp(now)))
        businessId = hex(int(datetime.timestamp(now)+1))[:10]+'_'+x["address"][-5:]+'_'+str(y)
        approver2 = str('businessId='+businessId+'&'+'deviceUuid='+targetDeviceUuid)
        approver1 = str('businessId='+businessId+'&'+'address='+x["address"]+'&'+'amount='+x["amount"]+'&'+'currency='+x["flag"]+'&'+'flag='+x["flag"])
        approve1_sign = get_sign_dispatch(approver1)
        approve2_sign = get_sign_dispatch(approver2)
        data_to_sign = {"apiKey":apiKey2,"submitAccount":"server1","address":x["address"],"amount":float(x["amount"]),"currency":x["flag"],"flag":x["flag"],"businessId":businessId,"timestamp":timestamp_str,"reviewUuid":"58E51634-3269-44AF-8351-F9506E2A4A6F","reviewSign":approve1_sign,"targetDeviceUuid":"4A76D3E2-43C4-4E91-AFA0-F4D7A7842CDC","approveUuid":"58E51634-3269-44AF-8351-F9506E2A4A6F","approveSign":approve2_sign}
        url = 'https://open.coinsdotest.com/coinsdo/open/v1/withdraw'
        k = requests.post(url, json = transaction_dispatch(data_to_sign, apiSecret2))
        print(k.text, x["flag"])
        

# def add_and_send(chain_selected, amount_to_send):
#     list_of_add = []
#     rand = randint(1,10)
#     print("Random number generated is",rand,', chain is: ', chain_selected)
#     timestamp_str = str(round(datetime.timestamp(now)))
#     data_to_sign_collect = {"apiKey":apiKey,"chain":chain_selected,"timestamp":timestamp_str,"targetDeviceUuid":collect_wallet}
    # for x in range (0,rand):
    #     url = 'https://open.coinsdotest.com/coinsdo/open/v1/addressGet'
    #     x = requests.post(url, json = transaction(data_to_sign_collect, apiSecret))
    #     print(json.loads(x.text)["data"]["address"])
    #     list_of_add.append(json.loads(x.text)["data"]["address"])
    # for i in list_of_add: ## executing the dispatch 
        # businessId = i.encode('utf-8').hex()[:4]+'_'+i[-5:]
        # approver2 = str('businessId='+businessId+'&'+'deviceUuid='+targetDeviceUuid)
        # approver1 = str('businessId='+businessId+'&'+'address='+i+'&'+'amount='+amount_to_send+'&'+'currency='+chain_selected+'&'+'flag='+chain_selected)
        # approve1_sign = get_sign_dispatch(approver1)
        # approve2_sign = get_sign_dispatch(approver2)
        # data_to_sign = {"apiKey":apiKey2,"submitAccount":"server1","address":i,"amount":float(amount_to_send),"currency":chain_selected,"flag":chain_selected,"businessId":businessId,"timestamp":timestamp_str,"reviewUuid":"58E51634-3269-44AF-8351-F9506E2A4A6F","reviewSign":approve1_sign,"targetDeviceUuid":"4A76D3E2-43C4-4E91-AFA0-F4D7A7842CDC","approveUuid":"58E51634-3269-44AF-8351-F9506E2A4A6F","approveSign":approve2_sign}
        # url = 'https://open.coinsdotest.com/coinsdo/open/v1/withdraw'
        # k = requests.post(url, json = transaction_dispatch(data_to_sign, apiSecret2))
        # print(k.text)

# for x in list(dispatch_wallet.keys()):
#     add_and_send(x, dispatch_wallet[x])
