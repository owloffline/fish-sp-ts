## Prerequisites:

-   Install Python3 to run the script:
    [Python Download](https://www.python.org/downloads/)
    (click on the yellow button "Download Python 3.12.3")
-   PhoenixBot premium
-   1 character who can complete the TS alone

/!\ You can proceed with 0, 1, or 2 alts accompanying you /!\

### How to use:

-   You can load the files "base.ini" and "last_room.ini"
    to manage your security & the SP skills you'll use.
    The only difference between the two files is that "last_room.ini"
    has "monster priority" activated to focus the boss first.
    (so, perform your skills on base.ini, then copy-paste, rename to last_room.ini, and activate monster priority)

-   Inject PhoenixBot on the characters who will do the TS.
-   Go to the map, next to the TS (within range to enter the TS).
-   Group the characters if there are multiple.

-   Configure the config.json file:
    /!\ BE CAREFUL NOT TO ADD EXTRA SPACES OR REMOVE COMMAS /!\
     - Open the config.json file (with Notepad or similar tool). - Replace the existing port with the corresponding character's Phoenix port
    (this is the port from the Phoenix window title, not Nostale). - "main_char_port" will be the attacker - "first_alt_port" will be the first mule - "second_alt_port" will be the second mule - "ts_to_do" will be the number of TS the bot will do before stopping automatically - if you don't have a first and second mule, leave/put empty quotes as in the example - Save the edited config.json file.

-   Open a terminal in the py_fish-ts folder.
-   Enter the following command (then press enter): `python main.py`
    (if the command doesn't work, try just the command: `main.py`)

-   Once the bot finishes doing the amount TS, it will stop automatically and display a message in the terminal.
    You just need to close it or press enter to close it.
