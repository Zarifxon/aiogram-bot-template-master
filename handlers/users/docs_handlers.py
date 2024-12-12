from loader import dp, bot
from aiogram.types import ContentType, Message
from pathlib import Path

#kelgan hujjatlar rasm. video, audio, download/categories papkasiga tushadi
download_path = Path().joinpath("Downloads", "categories")
download_path.mkdir(parents=True, exist_ok=True)
@dp.message_handler()
async def text_handler(message: Message):
    await message.reply("Siz matn yubordingiz!")


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download(destination_dir=download_path)
    doc_id = message.document.file_id
    await message.reply("Siz hujjat yubordingiz!\n"
                        f"file_id = {doc_id}")

@dp.message_handler(content_types=ContentType.VIDEO)
async def video_handler(message: Message):
    await message.video.download(destination_dir=download_path)
    # video_id = message.video.video_id
    await message.reply("Video qabul qilindi\n"
                        f"file_id = {message.video.file_id}")


@dp.message_handler(content_types='photo')
async def photo_handler(message: Message):
    await message.photo[-1].download(destination_dir=download_path)
    await message.reply("Rasm qabul qilindi\n"
                        f"file_id = {message.photo[-1].file_id}")

@dp.message_handler(content_types='audio')
async def audio_handler(message: Message):
    await message.audio.download(destination_dir=download_path)
    # video_id = message.video.video_id
    await message.reply("Audio qabul qilindi\n"
                        f"file_id = {message.audio.file_id}")

@dp.message_handler(content_types=ContentType.ANY)
async def any_handler(message: Message):
    await message.reply(f"{message.content_type} qabul qilindi")

