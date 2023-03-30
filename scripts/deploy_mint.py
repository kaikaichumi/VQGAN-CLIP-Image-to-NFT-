from brownie import PyConNFT, network, config, accounts
from brownie import *
from pinatapy import PinataPy
import json
import subprocess



#contractURI = "ipfs://QmVNpHExvWPkap8k8FLcsswFPMT2iBwjPKzUtDkjmLzWLS"

pinata_api_key = 'f5a0deef109ece878927'
pinata_secret_api_key = '479109799810f4a68fd96245ccd66a431f32d273590d7907c81d823095d474f4'

def json_ipfs():
    pinata = PinataPy(pinata_api_key, pinata_secret_api_key)
    j = pinata.pin_file_to_ipfs('0.json', '/test07')
    json_CID = j["IpfsHash"]
    return json_CID



def main():
    #network.connect('goerli')
    contractURI = "ipfs://"+json_ipfs()+"/0.json"
    print(contractURI)
    account = accounts.add(config["wallets"]["from_key"])
    ERC721 = PyConNFT.deploy(contractURI, {"from": account})
    print(f"New ERC721 has been deployed at {ERC721.address}")
    ERC721.mint(account.address, contractURI)
    
     

    
