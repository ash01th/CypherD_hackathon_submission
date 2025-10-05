from state_mgmt import update_state,get_state
from user_mgmt import register_user,import_wallet
logged_in=get_state('is_logged_in')
if not logged_in:
    choice=input("enter 1 to register\nenter 2 to import wallet\n")
    if choice=='1':
        username=input("Enter username:")
        email_id=input("Enter email id:")
        register_user(username,email_id)
        update_state('is_logged_in',True)
    elif choice=='2':
        seed_phrase=input("Enter your 12 word seed phrase:")
        seed_phrase=seed_phrase.strip().lower()
        import_wallet(seed_phrase)
        update_state('is_logged_in',True)