from fastapi import APIRouter,HTTPException
from model.Scrape_Model import ScrapeRequest
import requests
from bs4 import BeautifulSoup
router = APIRouter(prefix="/api/scrape", tags=["default"])

@router.post("/")
async def scrape_website(body: ScrapeRequest):
    url = body.url  
    print(url) 

    response = requests.get(url)


    if response.status_code == 200:
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        for unwanted in soup(['script', 'style', 'nav', 'footer']):
            unwanted.extract()

        text = soup.get_text()
        cleaned_text = ' '.join(text.split())

        return {"status": "success", "url": url, "data": cleaned_text}
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to retrieve the webpage.")