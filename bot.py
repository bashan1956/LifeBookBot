# -*- coding: utf-8 -*-
    )


@dp.message(lambda message: message.text == "Последние статьи")
async def latest_articles_handler(message: types.Message):
    zen_url = "https://bit.ly/bahan1956"
    inline_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Перейти на канал в Дзене", url=zen_url)]
    ])
    await message.answer(
        "<b>Последние опубликованные статьи и материалы</b>\n\n"
        "Все мои размышления, статьи и материалы по темам жизни, кармы и духовного поиска "
        "вы найдете на моем канале в Дзене.\n\n"
        f'<a href="{zen_url}">Или нажмите здесь, если кнопка не работает</a>',
        reply_markup=inline_kb,
        parse_mode="HTML"
    )
    await message.answer(
        "Нажмите кнопку ниже, чтобы вернуться в меню:",
        reply_markup=get_back_keyboard()
    )


@dp.message(lambda message: message.text == "Скачать PDF")
async def download_pdf_handler(message: types.Message):
    if not os.path.exists(PDF_PATH):
        await message.answer(
            "К сожалению, файл книги временно недоступен. Пожалуйста, сообщите автору.",
            reply_markup=get_back_keyboard()
        )
        return

    try:
        pdf_file = FSInputFile(PDF_PATH)
        await message.answer_document(
            document=pdf_file,
            caption="«Мой бесконечный путь» — автобиография Владимира Бэшэн-Сидоренко.\n\nСпасибо, что читаете! 🌟",
            reply_markup=get_back_keyboard()
        )
    except Exception as e:
        logging.error(f"Ошибка при отправке PDF: {e}")
        await message.answer(
            "Не удалось отправить книгу. Попробуйте позже.",
            reply_markup=get_back_keyboard()
        )


@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(
        "Извините, я не понимаю эту команду.\nПожалуйста, используйте кнопки меню.",
        reply_markup=get_main_keyboard()
    )


async def main():
    print("✅ Бот запускается... Ожидайте подключения к Telegram.")
    try:
        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types(),
            handle_signals=False  # Обязательно для PythonAnywhere
        )
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")


if __name__ == '__main__':
    asyncio.run(main())