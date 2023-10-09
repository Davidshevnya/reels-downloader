import instaloader
from aiogram import Router
from aiogram.types import Message
from aiogram.types.input_file import URLInputFile

router = Router()


@router.message()
async def message_handler(message: Message):
    if message.text=="" or message.text.find('instagram')==-1:
        await message.answer("Please send link to instagram reels")
        return
    try:
        ig = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(ig.context,message.text.split("/")[4])
        video_reels = URLInputFile(post.video_url)
        await message.answer_video(video_reels)
    except IndexError:
        await message.answer("Invalid link")
        
        
    
    