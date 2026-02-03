# -*- coding: utf-8 -*-
from pycq import *

# CHANGE THIS!
_main_uin = 111111
_main_password = "password"

_test_uin = 111111

c = pycq()
c.connect()
c.login(_main_uin, _main_password, 0, 1)
c.change_status(32)  # Free for Chat

if _test_uin:
    c.set_test_uin(_test_uin)

print(f"Started, UIN: {_main_uin}.")

while True:
    p = c.main(10)

    if p and isinstance(p, list) and len(p) > 0 and isinstance(p[0], dict):
        if 'uin' in p[0] and 'message_text' in p[0]:
            sender_uin = p[0]['uin']
            message_text = p[0]['message_text'].replace('\ufffd', '').strip()

            try:
                if message_text.lower() in ('!выход', '!logout'):
                    c.send_message_server(sender_uin, "До встречи!")
                    c.logout()
                    break

                c.send_message_server(sender_uin, message_text)

                import time
                time.sleep(0.05)

            except Exception as e:
                print(f"[-] Error: {e}")
