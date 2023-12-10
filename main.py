from flask import Flask, request, jsonify
from pyrogram import Client
import asyncio

api_id = "111111"
api_hash = "111111"
bot_token = "111111"

app = Flask(__name__)

async def getinfo(yhm):
    async with Client("IcyDCBot", api_id, api_hash, bot_token) as bot:
        user = await bot.get_users(yhm)
        return user

@app.route('/', methods=['POST'])
def kaihuji():
    yhm = request.json['id']
    user = asyncio.run(getinfo(yhm))
    dc = user.dc_id
    uid = user.id
    username = user.first_name + " " + user.last_name
    bot = user.is_bot
    restricted = user.is_restricted
    premium = user.is_premium
    lang = user.language_code
    return jsonify({
        "code": 200,
        "data": {
            "dc": dc,
            "uid": uid,
            "username": username,
            "bot": bot,
            "restricted": restricted,
            "premium": premium,
            "lang": lang
        }
    })

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=3002)
