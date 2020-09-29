# smart-userbot
![python](https://img.shields.io/badge/python-3.x-red.svg)

This user bot learns all messages from a telegram user in a group chose by you

# How to install and run it
- before you do anything you want to run `setup.sh` by doing `sudo bash setup.sh`
- after you set everything up, you want to change the `config.ini` variables. 
**do not touch `api_id` and `api_hash`**
1. run `create_session.py` with `python3 create_session.py`
2. after you have your session is created, grab the name and put it into `session_name` in the `config.ini` file.
3. you have to put your telegram ID in the `my_id` field.
4. and finally you will put the person's telegram ID you want the userbot to learn from in the `person_id_to_learn_from`.
5. finally run the `userbot.py` file by executing `python3 userbot.py`

# These are the following commands already in the userbot
```
/ping - userbot responds with "pong"
/enablechat - enables chat mode so it can chat. i recommend calling this command when the database is at least at 100kb
/leave - by calling this command the userbot leaves from the current group the command was called on
/status - returns if chat mode is enabled or disabled
/learn (group link or group username) - after the userbot joins the group it will start start learning by getting all messages from the person defined in the config.ini person_id_to_learn_from field
/disablechat - disables chat mode
/stoplearning - the userbot will stop all its learning processes
```

# Need Help? Join our telegram group by clicking the picture below
[![telegram](http://www.freepnglogos.com/uploads/telegram-logo-15.png)](https://t.me/tfchat)

# Or join our discord
[![discord](http://i.imgur.com/cbfIsqM.png)](https://discord.com/invite/PcXbQA3)

# Donations
BTC (Bitcoin) wallet address: 3D1FXKMMH46iDNYwn8u7bScrPfbu4ekfDc
