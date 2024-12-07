from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

def push_keyboard(text1,text2,text3,text4):

    buttons = [
            [
                InlineKeyboardButton(text=text1, callback_data="1"),
                InlineKeyboardButton(text=text2, callback_data="2"),

            ],
                
            [
                InlineKeyboardButton(text=text3, callback_data="3"),
                InlineKeyboardButton(text=text4, callback_data="4"),
            ]
                ]
    
    reply_markup = InlineKeyboardMarkup(inline_keyboard=buttons)
    return reply_markup
