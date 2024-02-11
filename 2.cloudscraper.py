"""
- To parse sites that are protected
- ethical when dealing with protected robots.txt sites like medium.com
"""

from protego import Protego
import cloudscraper

URL = "https://medium.com"
USER_AGENT = "MyBlogPostBot"


def is_valid_robots_txt(content):
    """Simple check for valid robots.txt files"""
    return "User-agent" in content or "Disallow" in content


scraper = cloudscraper.create_scraper()
r = scraper.get(URL+"/robots.txt")

if is_valid_robots_txt(r.text):
    rp = Protego.parse(r.text)
    print(rp.can_fetch(URL+"/_/", USER_AGENT))
    print(rp.can_fetch(URL+"/me/", USER_AGENT))
else:
    print("Cannot get robots.txt")