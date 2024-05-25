# actions.py

from phoenixapi import phoenix
from sleep_utils import sleep_rand

def enter_ts(main_char, all_alts, main_char_id):
    main_char.send_packet('ncif 2 4294967196')
    sleep_rand(1, 1.2)
    main_char.send_packet('treq 73 134')
    sleep_rand(0.5, 0.8)
    main_char.send_packet('treq 73 134 1')
    
    for alt in all_alts:
        sleep_rand(1, 1.5)
        alt.send_packet('treq 73 134')
        sleep_rand(0.5, 1)
        alt.send_packet('#wreq^3^' + str(main_char_id))
        sleep_rand(1, 1.2)
