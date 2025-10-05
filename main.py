from state_mgmt import update_state,get_state
from user_mgmt import register_user,import_wallet,perform_transaction
from db import fetch_user_from_pub_key,fetch_user_from_name
from mail_notification import send_email
logged_in=get_state('is_logged_in')
if not logged_in:
    choice=input("enter 1 to register\nenter 2 to import wallet\n")
    if choice=='1':
        username=input("Enter username:")
        email_id=input("Enter email id:")
        register_user(username,email_id)
        update_state('is_logged_in',True)
        print("Registration successful. You can now log in.")
    elif choice=='2':
        seed_phrase=input("Enter your 12 word seed phrase:")
        seed_phrase=seed_phrase.strip().lower()
        import_wallet(seed_phrase)
        update_state('is_logged_in',True)
        print("Wallet imported successfully. You can now log in.")
while True:
    print("You are  logged in.")
    print("press 0 to logout and exit any other key to contine")
    choice=input()
    if choice=='0':
        update_state('is_logged_in',False)
        print("Logged out successfully.")
        exit()
    else:
        print("sample eth transaction demo")
        print("sender details")
        sender_details=fetch_user_from_pub_key(get_state('public_key'))
        print("sender username:",sender_details[0])
        print("sender_balance:",sender_details[3])
        print("amount to send:1.0 ETH")
        print("receiver details")
        print("receiver username:ash2")
        receiver_details=fetch_user_from_name("ash2")
        print("receiver_balance before transaction:",receiver_details[3])
        print("proceeding with transaction...")
        perform_transaction(get_state('public_key'),receiver_details[2],1.0)
        receiver_details=fetch_user_from_name("ash2")
        print("receiver_balance after transaction:",receiver_details[3])
        print("sendig mail notification to receiver")
        send_email(receiver_email=receiver_details[1],
                   subject="You have received 1.0 ETH",
                     body=f"Hello {receiver_details[0]},\n\nYou have received 1.0 ETH from {sender_details[0]}.your current balance is {receiver_details[3]} ETH \n\nBest regards,\nCypherD Team",
                     sender_email="boredman665@gmail.com",
                        sender_password="zakp nggx bgxs epsn")
        print("mail sent successfully")
        
            

