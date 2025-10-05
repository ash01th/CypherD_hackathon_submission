from crypto import generate_mnemonic_phrase,get_wordlist,key_gen,verify_sign,sign
from db import insert_record,fetch_user_from_pub_key,update_balance
from state_mgmt import update_state,get_state
from usd_conv import get_eth_for_usd
import random
import binascii
from ecdsa import SigningKey, SECP256k1


def register_user(username,email_id):
    word_list = get_wordlist()
    seed_phrase = generate_mnemonic_phrase(word_list, num_words=12)
    private_key, public_key, public_key_hex = key_gen(seed_phrase)
    private_key_hex= binascii.hexlify(private_key.to_string()).decode('utf-8')
    init_bal=round(random.uniform(1.0,10.0),2)
    insert_record((username,email_id,public_key_hex,init_bal))
    update_state('username',username)
    update_state('public_key',public_key_hex)
    update_state('email_id',email_id)
    update_state('private_key',private_key_hex)
    
def import_wallet(seed_phrase):
    private_key, public_key, public_key_hex = key_gen(seed_phrase)
    user_data=fetch_user_from_pub_key(public_key_hex)
    if user_data:
        update_state('username',user_data[0])
        update_state('public_key',public_key_hex)
        update_state('email_id',user_data[1])
        private_key_hex= binascii.hexlify(private_key.to_string()).decode('utf-8')
        update_state('private_key',private_key_hex)
    else:
        print("User not found. Please register first.")
    
def check_bal(sender_public_key,amount):
    user_data=fetch_user_from_pub_key(sender_public_key)
    if user_data:
        if user_data[3]>=amount:
            new_balance=user_data[3]-amount
            insert_record((user_data[0],user_data[1],user_data[2],new_balance))
            return True
        else:
            return False
    else:
        return False
def sign_transaction(transaction_data,private_key_hex,amount,type="ETH"):
    private_key_bytes = binascii.unhexlify(private_key_hex)
    sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    signature = sign(sk, transaction_data)
    if type!="ETH":
        conv_amount=get_eth_for_usd(amount)
        return signature,type,conv_amount
    else:
        return signature,type,amount

def perform_transaction(sender_public_key,receiver_public_key,amount,type="ETH"):
    sender_data=fetch_user_from_pub_key(sender_public_key)
    recv_data=fetch_user_from_pub_key(receiver_public_key)
    if not sender_data or not recv_data:
        print("Sender or receiver not found.")
        return
    if type!="ETH":
        if check_bal(sender_public_key,amount):
            sig,type,amt=sign_transaction("tx_data",get_state("private_key"),amount,type)
            try:
                verify_sign("transaction",sig,recv_data[2]) 
                print("Signature verified.comitting transaction...")
                update_balance(sender_data[0],sender_data[3]-amt)
                update_balance(receiver_public_key,sender_data[3]+amt)

            except Exception as e:
                print(f"Signature verification failed: {e}")
                return
    else:
        conv_amount=get_eth_for_usd(amount)
        if check_bal(sender_public_key,conv_amount):
            sig,type,init_amt=sign_transaction("tx_data",get_state("private_key"),amount,type)
            try:
                verify_sign("transaction",sig,recv_data[2])
                print("Signature verified.comitting transaction...")
                update_balance(sender_data[0],sender_data[3]-init_amt)
                update_balance(receiver_public_key,sender_data[3]+init_amt)
            except Exception as e:
                print(f"Signature verification failed: {e}")
                return
