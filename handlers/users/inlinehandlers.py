from aiogram import types
from data.courses_python import inline_results_python
from keyboards.inline.courses import aiogram_keys, python_keys
from loader import dp

@dp.inline_handler(text="python")
async def empty_query(query: types.InlineQuery):
    await query.answer(inline_results_python)


@dp.inline_handler(text="rasm")
async def photo_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultPhoto(
                id="ph001",
                photo_url="https://mohirdevbucket.s3.eu-central-1.amazonaws.com/practicum/images/b0fdb946-9b5c-41ed-8381-81a080746807.original.jpeg",
                thumb_url="https://mohirdevbucket.s3.eu-central-1.amazonaws.com/practicum/images/b0fdb946-9b5c-41ed-8381-81a080746807.original.jpeg",
                caption="<b> Mukammal telegram bot</b> Darsi",
                reply_markup=aiogram_keys
            ),
            types.InlineQueryResultPhoto(
                id="ph002",
                photo_url="https://mohirdevbucket.s3.eu-central-1.amazonaws.com/practicum/images/9cca98e9-d11b-44bc-b6c2-f8839485c132.original.jpeg",
                thumb_url="https://mohirdevbucket.s3.eu-central-1.amazonaws.com/practicum/images/9cca98e9-d11b-44bc-b6c2-f8839485c132.original.jpeg",
                caption="<b> Pythonda dasturalsh asoslari</b> Darsi",
                reply_markup=python_keys
            ),
            types.InlineQueryResultVideo(
                id="vd1",
                video_url="https://youtu.be/701E5EIb24I?si=1n4jWQ_4ANzTaJx9",
                title="Bu video internetdan video yuklab olish haqida",
                thumb_url="https://mohirdevbucket.s3.eu-central-1.amazonaws.com/practicum/images/9cca98e9-d11b-44bc-b6c2-f8839485c132.original.jpeg",
                caption="<b> Videolarni yuklab olish</b> Darsi",
                description="Videolarni yuklab olish haqida dars",
                mime_type="video/mp4", #video/mp4 yoki text/html,
            ),

        ]
    )





@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="kurs001",
                title="DAsturlash asoslari. Python",
                input_message_content=types.InputTextMessageContent(
                    message_text="Dars uchun link: https://mohirdev.uz/kurslar/dasturlash-asoslari-python/"

                ),
                url="https://mohirdev.uz/kurslar/dasturlash-asoslari-python/",
                thumb_url= "https://mohirdevbucket.s3.eu-central-1.amazonaws.com/practicum/images/b0fdb946-9b5c-41ed-8381-81a080746807.original.jpeg",
                description="Dasturlash asoslarini eng mahshur dasturlash tili - Python orqali o'rganing",

            ),
            types.InlineQueryResultArticle(
                id="kurs002",
                title="telegram bot",
                input_message_content=types.InputTextMessageContent(
                    message_text="Dars uchun link: https://mohirdev.uz/kurslar/telegram/"

                ),
                url="https://mohirdev.uz/kurslar/telegram/",
                thumb_url="https://mohirdevbucket.s3.eu-central-1.amazonaws.com/practicum/images/b0fdb946-9b5c-41ed-8381-81a080746807.original.jpeg",
                description="Telegram botni Zarifdev bilan Python orqali o'rganing",

            )
        ]
    )