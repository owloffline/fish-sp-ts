from phoenixapi import phoenix
import json
from sleep_utils import sleep_rand
from actions import enter_ts
import os

with open('config.json', 'r') as config_file:
  config = json.load(config_file)

main_char_port = config['main_char_port']
first_alt_port = config['first_alt_port']
second_alt_port = config['second_alt_port']
ts_to_do = config['ts_to_do']


ts_done = 0
all_chars = []
all_alts = []
main_char_id = None
currentRoom = 0

running = True
ts = True

base_profile = os.path.join(os.path.dirname(__file__), 'base.ini')
boss_profile = os.path.join(os.path.dirname(__file__), 'last_room.ini')

if __name__ == "__main__":
  
    main_char = phoenix.Api(main_char_port)
    
    if first_alt_port != "":
      first_alt = phoenix.Api(first_alt_port)
      all_alts.append(first_alt)
      all_chars.append(first_alt)
      
    if second_alt_port != "":
      second_alt = phoenix.Api(second_alt_port)
      all_alts.append(second_alt)
      all_chars.append(second_alt)
          
    main_char.query_player_information()
    print('Starting...')
    
    
    while running and main_char.working():
      try:
        if not main_char.empty():
          msg = main_char.get_message()
          json_msg = json.loads(msg)
          
          
          if json_msg["type"] == phoenix.Type.query_player_info.value:
            main_char_id = json_msg["player_info"]["id"]
            
          if json_msg["type"] == phoenix.Type.packet_recv.value:
            packet_split = json_msg["packet"].split(" ")
            if ts:
              print('Starting TS in 3 seconds...')
              sleep_rand(2.8, 3.5)
              enter_ts(main_char, all_alts, main_char_id)
              ts = False
              sleep_rand(0.5, 1)
              main_char.player_walk(22, 3)
              currentRoom = 1
            
            if json_msg["packet"] == "dlgi #rstart^1 rstart 92 0 0":
              sleep_rand(0.5, 0.8)
              main_char.send_packet('#rstart^1')
              ts_done += 1
              print('Starting TS No.', ts_done)
              
            if json_msg["packet"] == "mapout":
              sleep_rand(0.5, 0.8)
              if currentRoom == 0:
                pass
              elif currentRoom == 1:
                main_char.load_settings(base_profile)
                main_char.start_bot()
              elif currentRoom == 2:
                main_char.player_walk(22, 4)
                currentRoom = 3
              elif currentRoom == 3:
                main_char.start_bot()
              elif currentRoom == 4:
                main_char.start_bot()
              elif currentRoom == 5:
                main_char.start_bot()
              elif currentRoom == 6:
                main_char.player_walk(39, 21)
                currentRoom = 7;
              elif currentRoom == 7:
                main_char.start_bot()
              elif currentRoom == 8:
                main_char.start_bot()
              elif currentRoom == 9:
                main_char.start_bot()
                currentRoom = 10
              elif currentRoom == 10:
                main_char.player_walk(22, 38)
                currentRoom = 11
              elif currentRoom == 11:
                main_char.start_bot()
                currentRoom = 12
              elif currentRoom == 12:
                main_char.player_walk(22, 39)
                currentRoom = 13
              elif currentRoom == 13:
                main_char.player_walk(4, 21)
                currentRoom = 14
              elif currentRoom == 14:
                main_char.player_walk(22, 38)
                currentRoom = 15
              elif currentRoom == 15:
                main_char.load_settings(boss_profile)
                main_char.start_bot()
                currentRoom == 16

            if json_msg["packet"] == "mapclear":
              sleep_rand(0.5, 0.8)
              if currentRoom == 0:
                pass
              elif currentRoom == 1:
                main_char.stop_bot()
                main_char.player_walk(4, 21)
                currentRoom = 2
              elif currentRoom == 3:
                main_char.stop_bot()
                main_char.player_walk(22, 4)
                currentRoom = 4
              elif currentRoom == 4:
                main_char.stop_bot()
                main_char.player_walk(3, 21)
                currentRoom = 5
              elif currentRoom == 5:
                main_char.stop_bot()
                main_char.player_walk(60, 33)
                currentRoom = 6
              elif currentRoom == 7:
                main_char.stop_bot()
                main_char.player_walk(39, 21)
                currentRoom = 8
              elif currentRoom == 8:
                main_char.stop_bot()
                main_char.player_walk(39, 21)
                currentRoom = 9
              elif currentRoom == 10:
                main_char.stop_bot()
                main_char.player_walk(39, 21)
                currentRoom = 11
              elif currentRoom == 12:
                main_char.stop_bot()
                main_char.player_walk(8, 33)
                currentRoom = 13
                
            if "score" in json_msg["packet"]:
              main_char.stop_bot()
              currentRoom = 0
              sleep_rand(4, 6)
              print('Finished TS No.', ts_done)
              main_char.send_packet('escape')
              
              for alt in all_alts:
                alt.send_packet('escape')
            
            if json_msg["packet"] == "c_map 0 2 1":
              if ts_done < ts_to_do:
                sleep_rand(12, 15)
                ts = True
              else:
                print('All ' + str(ts_done) + ' out of ' + str(ts_to_do) + ' are done ! You can close this program :)')
                ts = False
                running = False
            
            
              


              
              
            
              
      except KeyboardInterrupt:
          main_char.__del__()
          exit()
      except Exception as e:
          print(e)
          main_char.__del__()
          exit()
          
    input("Press Enter to exit...")