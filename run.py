from telethon import TelegramClient, events, sync


api_id = 2445378
api_hash = '017d7f3504c401aa10e1c30673f694ea'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

print(client.get_me().stringify())

client.send_message('username', 'Hello! Talking to you from T-rex.Exchange')
client.send_file('username', '/home/myself/Pictures/holidays.jpg')

client.download_profile_photo('me')
messages = client.get_messages('username')
messages[0].download_media()

@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')