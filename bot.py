import requests,asyncio,os
from telegram import Bot
from datetime import datetime
import pytz

TELEGRAM_TOKEN=os.getenv("TELEGRAM_TOKEN")
CHAT_ID=os.getenv("CHAT_ID")
SAST=pytz.timezone('Africa/Johannesburg')
bot=Bot(token=TELEGRAM_TOKEN)

async def main():
    msg=f"**DAILY MACRO BIAS | {datetime.now(SAST).strftime('%d %b %Y')}**\n\nTest message - bot is live.\n\nNext: Add full data logic once deployed."
    await bot.send_message(chat_id=CHAT_ID,text=msg,parse_mode='Markdown')

async def scheduler():
    while True:
        now=datetime.now(SAST).time()
        if now.hour==9 and now.minute==0:
            await main()
            await asyncio.sleep(60)
        await asyncio.sleep(30)

if __name__=="__main__":
    asyncio.run(scheduler())
