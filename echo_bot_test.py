# -*- coding: utf-8 -*-
from pycq import *

# CHANGE THIS!
_test_uin = 111111 
_test_password = "password"

TEST_RESULTS_FILE = 'test_results.txt'

c = pycq()
c.connect()
c.login(_test_uin, _test_password, 0, 1)
c.change_status(32)  # Free for Chat

print(f"Started, UIN: {_test_uin}.")

while True:
    p = c.main(10)

    if p and isinstance(p, list) and len(p) > 0 and isinstance(p[0], dict):
        if 'uin' in p[0] and 'message_text' in p[0]:
            message_text = p[0]['message_text']
            sender_uin = p[0]['uin']

            print(f"Received message from {sender_uin}: {repr(message_text)}")

            # Record the received message for main bot to check
            try:
                with open(TEST_RESULTS_FILE, 'a', encoding='utf-8') as f:
                    f.write(f"RECEIVED:{sender_uin}:{message_text}\n")
                print(f"[+] Message recorded to {TEST_RESULTS_FILE}")
            except Exception as e:
                print(f"[-] Error writing to file: {e}")