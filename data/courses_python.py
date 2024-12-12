from aiogram import types

courses = [
    {
        "id":"001",
        "title":"#01 KERAKLI DASTURLAR",
        "url":"https://praktikum.mohirdev.uz/dashboard/practicums/6551b8636260c6476960fec7",
        "description": "Ushbu bo'limda Python tilida kod yozish uchun kerakli bo'lgan dasturlarni o'rnatamiz",
    },
    {
        "id": "002",
        "title": "#02 Hello world",
        "url": "https://praktikum.mohirdev.uz/dashboard/practicums/645264af69d972027cd02d52/645264af69d972027cd02d71/645264af69d972027cd02d73",
        "description": "Hello worldni kodini yozamiz",
    },
{
        "id": "003",
        "title": "#03 print() (chop etish), sinteks va arifmetik amallar",
        "url": "https://praktikum.mohirdev.uz/dashboard/practicums/645264af69d972027cd02d52/645264af69d972027cd02d71/645264af69d972027cd02d74",
        "description": "print() (chop etish), sinteks va arifmetik amallar",
    },
]


inline_results_python = []
for course in courses:
    inline_results_python.append(
        types.InlineQueryResultArticle(
            id=course["id"],
            title=course["title"],
            input_message_content=types.InputTextMessageContent(
                message_text=f"{course['title']} darsiga link: {course['url']}"
            ),
            url=course["url"],
            description=course["description"],
        )
    )