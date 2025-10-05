# CypherD Hackathon Submission

## Initial Setup:

1.  Run the `db.py` file to create the user database and to populate it with sample data.
2.  Ensure the `state.yaml` file exists and the `is_logged_in` field is set to `false`.
3.  Run the `main.py` file.
4.  To check the "import wallet" feature, use the phrase that will be generated during the signup phase.

## Implemented Features:

-   **ETH to USD Conversion:** Conversion from ETH to USD is handled by `usd_conv.py`.
-   **Email Notifications:** Notifications are sent via email using `mail_notification.py`.
    -   *Both of the above features can be tested individually by simply running their respective Python files.*
-   **Secure Seed Phrase Generation:** Cryptographically secure seed phrase generation using the BIP-39 English wordlist, with a fallback mechanism in case of errors.
-   **Digital Signatures:** Cryptographically secure signing and signature verification using ECDSA on the `SECP256k1` curve.
-   **CLI Demo:** A basic command-line interface demo of an ETH transaction between two peers.

## Future Work

-   Use a key-value database to store transactions.
-   Use Docker to create an image and deploy it on cloud platforms.
-   Host a web server and UI to enable communication.
