"""
- To get required data by preprocessing the text
"""

from protego import Protego
import cloudscraper
from bs4 import BeautifulSoup

URL = "https://www.foxnews.com"
USER_AGENT = "MyBlogPostBot"


def is_valid_robots_txt(content):
    """Simple check for valid robots.txt files"""
    return "User-agent" in content or "Disallow" in content


scraper = cloudscraper.create_scraper()
r = scraper.get(URL+"/robots.txt")

if is_valid_robots_txt(r.text):
    rp = Protego.parse(r.text)
    
    if rp.can_fetch(URL, USER_AGENT):
        r = scraper.get(URL)
        
        soup = BeautifulSoup(r.text, 'lxml')
        
        print(soup.title)
        title_tag = soup.find('h3', class_='title')
        link = title_tag.find('a')['href'] if title_tag else None
        
        print(title_tag)
        print(link)
else:
    print("Cannot get robots.txt")