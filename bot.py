import random
import pyrogram
import JDB
from inline import mark, spon
import os
try:
    os.mkdir("dbs")
except:
    pass
pr = None
inp = 0
if inp != "0":
    pr = {
        "scheme": "socks5",
        "hostname": inp.split(":")[0],
        "port": int(inp.split(":")[1])
    }

app = pyrogram.Client(
    "dbs/bot",
    api_id=10972622,
    api_hash="46a68ad7647433f42b4e4b2e51e679af",
    bot_token="dadadaad",
    proxy=pr
)
DB = JDB.DB("dbs/bot")
if not DB.Get("Videos"):
    DB.Define("Videos", {})
if not DB.Get("Bot"):
    DB.Define("Bot", input("UN Bot:"))
if not DB.Get("Channel"):
    DB.Define("Channel", input("Channel bot: "))
if not DB.Get("Spons"):
    DB.Define("Spons", {})
if not DB.Get("Users"):
    DB.Define("Users", [])
al = ("a b c d e f g h i j k l m n o q r s t u v w x y z " +
      "A B C D E F G H I J K L M N O P Q R S Y U V W X Y Z").split(" ")


@app.on_inline_query()
async def kos(client, query):
    __sponss = DB.Get("Spons")
    print(__sponss)
    for i in __sponss.keys():
        try:
            await app.get_chat_member(chat_id=__sponss[i], user_id=query.from_user.id)
        except:
            await app.send_message(chat_id=query.from_user.id, text="برای حمایت از من جوین کانال/گروه زیر بده :) ", reply_markup=spon(pyrogram.types, DB.Get("Spons"),f"{DB.Get('Bot')}?start={query.query}"))
            return
    else:
        print('not')
        pass
    await app.answer_inline_query(
        query.id,
        results=[
            pyrogram.types.InlineQueryResultCachedVideo(DB.Get(
                "Videos")[query.query], title="Click!", description="برای دیدن ویدیو کلیک کنید")

        ]
    )


@app.on_message(pyrogram.filters.video)
async def video(client, message: pyrogram.types.Message):
    if message.via_bot:
        return
    print("video")
    __name = "".join([random.choice(al) for i in range(32)])
    DB.AddToDict("Videos", __name, message.video.file_id)
    await message.reply(text=f"Video Saved SuccessFully \n Link : {DB.Get('Bot')}?start={__name}", reply_to_message_id=message.id)


@app.on_message(pyrogram.filters.text)
async def user(client, message: pyrogram.types.Message):
    if not message.from_user.id in DB.Get("Users"):
        DB.AddToList("Users", message.from_user.id)
    print("text")
    txt = message.text
    if txt.startswith("/start "):
        # ______________________#
        __sponss = DB.Get("Spons")
        print(__sponss)
        for i in __sponss.keys():
            try:
                await app.get_chat_member(chat_id=__sponss[i], user_id=message.from_user.id)
            except:
                await message.reply("برای حمایت از من جوین کانال/گروه زیر بده :) ", reply_to_message_id=message.id, reply_markup=spon(pyrogram.types, DB.Get("Spons"),f"{DB.Get('Bot')}?start={txt.split(' ')[-1]}"))
                return
        else:
            print('not')
            pass
        # ______________________#
            __vids = DB.Get("Videos")
            if txt.split(" ")[-1] in __vids:
                await message.reply("برای مشاهده فیلم روی دکمه زیر کلیک کنید:", reply_markup=mark(pyrogram.types, txt.split(" ")[-1]), reply_to_message_id=message.id)
            else:
                await message.reply("این ویدیو وجود ندارد", reply_to_message_id=message.id)
    elif txt == "/start":
        await message.reply("خوش اومدی چنل اصلی: "+"\n"+DB.Get("Channel"), reply_to_message_id=message.id)
    elif txt.startswith("/spon "):
        __d = txt.split(" ")[-1]
        if not "+" in __d and not "joinchat" in __d:
            __a = await app.get_messages(__d.split("/")[-1], message_ids=1)

        else:
            __a = await app.get_messages(__d, message_ids=1)
        if __a:
            DB.AddToDict("Spons", "https://t.me/"+__d[1:], __a.chat.id)
            await message.reply(text="OK shod :D", reply_to_message_id=message.id)
        else:
            await message.reply(text=("Error")+__d, reply_to_message_id=message.id)
    elif txt.startswith("/dspon "):
        DB.DelFromDict("Spons", txt.split(" ")[-1])
        await message.reply(text="Delete Shod :D", reply_to_message_id=message.id)
    elif txt == "/spons":
        __spons = DB.Get("Spons")
        __o = ""
        if not len(__spons.keys()) == 0:
            for i in __spons.keys():
                __o += f"`{i}`\n"
        else:
            __o = "There is no sponser!"
        await message.reply(text=__o, reply_to_message_id=message.id)
    elif txt == "/boff":
        await message.reply("Ok!", reply_to_message_id=message.id)
        exit()
    elif txt == "/hamg":
        __i = await message.reply("Sending...", reply_to_message_id=message.id)
        m = message.reply_to_message
        for i in DB.Get("Users"):
            try:
                await app.copy_message(i, m.chat.id, m.id)
            except Exception as e:
                print(e)
        await __i.edit_text("Sent")

app.run()
# await message.reply("dddd", reply_markup=mark(pyrogram.types))
