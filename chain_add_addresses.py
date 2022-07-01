import pandas as pd
import secrets
# from pycardano import Address, Network, PaymentSigningKey, PaymentVerificationKey
import json
from xrpl.wallet import Wallet
from web3 import Web3, HTTPProvider
from tronpy import Tron
from tronpy.keys import PrivateKey
from bitcoinaddress import Wallet as wallet_btc
from cryptos import *
from cashaddress import convert


chain = []
secret_chain = []
add_chain = []
dict = {"Name of Mainnet": chain, "Private key": secret_chain, "Address": add_chain}

def create_eth(amount): #rinkeby
    for x in range(amount):
        w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/8e4cd4b220fa42d3ac2acca966fd07fa"))
        chain2 = 'ETH'
        acct = w3.eth.account.create()
        private_key = acct._private_key.hex()
        chain.append(chain2)
        secret_chain.append(private_key[2:])
        add_chain.append(acct.address)
    

def create_xrp(amount): #testnet
    for x in range(amount):
        chain3 = 'XRP'
        test_wallet = Wallet.create()
        xrp_address = test_wallet.classic_address
        xrp_secret =  test_wallet.private_key
        chain.append(chain3)
        secret_chain.append(xrp_secret)
        add_chain.append(xrp_address)


def create_trx(amount): #nile
    for x in range(amount):
        client = Tron(network='nile')
        chain4 = 'TRX'
        wallet = client.generate_address()
        trx_address = wallet['base58check_address']
        trx_secret =  wallet['private_key']
        chain.append(chain4)
        secret_chain.append(trx_secret)
        add_chain.append(trx_address)

def create_btc(amount): #BTC testnet
    for x in range(amount):
        wallet = wallet_btc(testnet=True)
        chain5 = 'BTC'
        btc_address = wallet.address.__dict__['testnet'].__dict__['pubaddr1c']
        btc_secret =  wallet.key.__dict__['testnet'].__dict__['wifc']
        chain.append(chain5)
        secret_chain.append(btc_secret)
        add_chain.append(btc_address)


# def create_ada(amount):   
#     for x in range(amount):
#         network = Network.TESTNET
#         payment_signing_key = PaymentSigningKey.generate()
#         skey_json = json.loads(payment_signing_key)
#         skey = skey_json['cborHex']
#         payment_verification_key = PaymentVerificationKey.from_signing_key(payment_signing_key)
#         address = Address(payment_part=payment_verification_key.hash(), network=network)
#     return address, skey

def create_dash(amount):
    for x in range(amount):
        chain6 = 'DASH'
        priv = random_key()
        coin = Dash(testnet=True)
        pub2 = coin.privtopub(priv)
        dash_address = coin.pubtoaddr(pub2)
        dash_wallet = wallet_btc(priv, testnet=True)
        dash_secret = dash_wallet.key.__dict__['testnet'].__dict__['wifc']
        chain.append(chain6)
        secret_chain.append(dash_secret)
        add_chain.append(dash_address)

def create_bch(amount):
    for x in range(amount):
        chain7 = 'BCH'
        priv = random_key()
        coin = BitcoinCash(testnet=True)
        pub2 = coin.privtopub(priv)
        legacy_bch_address = coin.pubtoaddr(pub2)
        cash_bch_address = convert.to_cash_address(legacy_bch_address)
        bch_wallet = wallet_btc(priv, testnet=True)
        bch_secret = bch_wallet.key.__dict__['testnet'].__dict__['wifc']
        chain.append(chain7)
        secret_chain.append(bch_secret)
        add_chain.append(cash_bch_address)

def create_ltc(amount):
    for x in range(amount):
        chain7 = 'LTC'
        priv = random_key()
        coin = Litecoin(testnet=True)
        pub2 = coin.privtopub(priv)
        ltc_address = coin.pubtoaddr(pub2)
        ltc_wallet = wallet_btc(priv, testnet=True)
        ltc_secret = ltc_wallet.key.__dict__['testnet'].__dict__['wifc']
        chain.append(chain7)
        secret_chain.append(ltc_secret)
        add_chain.append(ltc_address)

def create_doge(amount):
    for x in range(amount):
        chain8 = 'DOGE'
        priv = random_key()
        coin = Doge(testnet=True)
        pub2 = coin.privtopub(priv)
        doge_address = coin.pubtoaddr(pub2)
        doge_wallet = wallet_btc(priv, testnet=True)
        doge_secret = doge_wallet.key.__dict__['testnet'].__dict__['wifc']
        chain.append(chain8)
        secret_chain.append(doge_secret)
        add_chain.append(doge_address)

def create_bnb(amount): #same as rinkeby
    for x in range(amount):
        w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/8e4cd4b220fa42d3ac2acca966fd07fa"))
        chain9 = 'BNB'
        acct = w3.eth.account.create()
        private_key = acct._private_key.hex()
        chain.append(chain9)
        secret_chain.append(private_key[2:])
        add_chain.append(acct.address)

def create_ftm(amount): #same as rinkeby
    for x in range(amount):
        w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/8e4cd4b220fa42d3ac2acca966fd07fa"))
        chain10 = 'FTM'
        acct = w3.eth.account.create()
        private_key = acct._private_key.hex()
        chain.append(chain10)
        secret_chain.append(private_key[2:])
        add_chain.append(acct.address)

def create_okt(amount): #same as rinkeby
    for x in range(amount):
        w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/8e4cd4b220fa42d3ac2acca966fd07fa"))
        chain11 = 'OKT'
        acct = w3.eth.account.create()
        private_key = acct._private_key.hex()
        chain.append(chain11)
        secret_chain.append(private_key[2:])
        add_chain.append(acct.address)

def create_xdai(amount): #same as rinkeby
    for x in range(amount):
        w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/8e4cd4b220fa42d3ac2acca966fd07fa"))
        chain12 = 'XDAI'
        acct = w3.eth.account.create()
        private_key = acct._private_key.hex()
        chain.append(chain12)
        secret_chain.append(private_key[2:])
        add_chain.append(acct.address)

def create_matic(amount): #same as rinkeby
    for x in range(amount):
        w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/8e4cd4b220fa42d3ac2acca966fd07fa"))
        chain13 = 'MATIC'
        acct = w3.eth.account.create()
        private_key = acct._private_key.hex()
        chain.append(chain13)
        secret_chain.append(private_key[2:])
        add_chain.append(acct.address)

def create_ht(amount): #same as rinkeby
    for x in range(amount):
        w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/8e4cd4b220fa42d3ac2acca966fd07fa"))
        chain14 = 'HT'
        acct = w3.eth.account.create()
        private_key = acct._private_key.hex()
        chain.append(chain14)
        secret_chain.append(private_key[2:])
        add_chain.append(acct.address)

def create_etc(amount): #same as rinkeby
    for x in range(amount):
        w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/8e4cd4b220fa42d3ac2acca966fd07fa"))
        chain15 = 'ETC'
        acct = w3.eth.account.create()
        private_key = acct._private_key.hex()
        chain.append(chain15)
        secret_chain.append(private_key[2:])
        add_chain.append(acct.address)

amount = 50
create_eth(amount)
create_xrp(amount)
create_trx(amount)
create_btc(amount)
create_dash(amount)
create_bch(amount)
create_ltc(amount)
create_doge(amount)
create_bnb(amount)
create_ftm(amount)
create_okt(amount)
create_xdai(amount)
create_matic(amount)
create_ht(amount)
create_etc(amount)
# print(chain, secret_chain, add_chain,)

df = pd.DataFrame(dict)
df.to_excel('addresses_to_upload.xlsx')
