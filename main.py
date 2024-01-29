from telegram.ext import ApplicationBuilder , CommandHandler ,  ContextTypes , MessageHandler , filters
import asyncio 
import os
from rembg import remove
from telegram import Update   
from PIL import Image 
  
TOKEN = "6720392998:AAGFLS-keCk4vEjLaa6NaaVbaaIEyL3R-_Y"

async def help(update : Update , context : ContextTypes.DEFAULT_TYPE):
             await context.bot.send_message(chat_id = update.effective_chat.id , text = 'hey im work man click here to run the bot /start')

async def start(update : Update , context : ContextTypes.DEFAULT_TYPE):
             await context.bot.send_message(chat_id = update.effective_chat.id , text = 'give mme the pic you wont to remove the background')

async def hundler(update : Update , context : ContextTypes.DEFAULT_TYPE):
            if filters.PHOTO.check_update(update):
                    file_id = update.message.photo[-1].file_id
                    unique_file_id = update.message.photo[-1].file_unique_id
                    name_photo = f'{unique_file_id}.jpg'
            elif filters.Document.IMAGE:
                    file_id = update.message.document.file_id
                    unique_file_id = update.message.document.file_unique_id
                    _, ext = os.path.splitext(update.message.document.file_name)
                    name_photo = f'{unique_file_id}.{ext}'
                
            photo_file = await context.bot.get_file(file_id)
            await photo_file.download_to_drive(custom_path=f'./tmp/{name_photo}')
            await context.bot.send_message(chat_id = update.effective_chat.id , text = 'prosseccc')
            prossecc_image = await prosseccImage(name_photo)
            await context.bot.send_document(chat_id = update.effective_chat.id , document= prossecc_image)
            os.remove(prossecc_image)

            
   


async def prosseccImage(image: str):
    nameImage, _ = os.path.splitext(image)
    newNameImage = f'./proccessImage/{nameImage}'
    inputImage = Image.open(f'./tmp/{image}')
    output_image = remove(inputImage)
    output_image.save(newNameImage, format="PNG")
    os.remove(f'./tmp/{image}')
    return newNameImage

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    commend = CommandHandler('help' ,  help)
    cms = CommandHandler('start' ,  start)
    message_hunder =  MessageHandler(filters.PHOTO | filters.Document.IMAGE , hundler )
    app.add_handler(commend)
    app.add_handler(message_hunder)
    app.add_handler(cms)
    app.run_polling()