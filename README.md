# CypherD_hackathon_submission
hackathon_submission
# initial setup:
-run the db.py file to create user database and to populate sample data
-ensure the state.yaml file exists and is_logged_in field is set to false
-run the main.py file
-to check import wallet use the phrase which will be generated in the signup phase
# implementd features:
-conversion from eth to usd (usd_conv.py)
-notifications via mail (mail_notification.py)
both of the above features can be tested individually by simply running them
-cryptographically secure seed phrase generation using BIP-39 English wordlist and fallback if any error occurs
-cryptographically secure signing and sign verification using ecdsa on curve SECP256k1
-basic cli demo of eth transaction between two peers
# future work
-use a keyvalue database to store transactions
-use docker to create image and deploy on cloud platforms
-host a webserver and ui to enable communication
