from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart


router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Hi, {hbold(message.from_user.full_name)}! Send a link to Reels and I will send you a video")