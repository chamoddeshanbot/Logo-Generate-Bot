from typing import Optional
import aiohttp

LOGO_API_URL1 = "https://techzbotsapi.herokuapp.com/logo?text="
LOGO_API_URL2 = "https://techzbotsapi.herokuapp.com/logo?square=true&text="

async def generate_logo(text: str, square: Optional[bool] = False ):
  "To Create Logos. text = What you want to write on the logo. square = If You Want Square Logo Or Not. Returns Telgraph Image Url"
  
  try:
    square = str(square).capitalize()
  
    if square == "True":
      url = LOGO_API_URL2 + text
    else:
      url = LOGO_API_URL1 + text
  
    async with aiohttp.ClientSession() as session: 
      async with session.get(url) as resp:  
        img_url = resp.url
  except Exception as e:
    return "error" + str(e)
      
  return str(img_url)
