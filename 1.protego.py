"""
- reppy should be better but was not able to install
- this works only on some sites that are not protected
"""

import requests

from protego import Protego

URL = "https://medium.com"
USER_AGENT = "MyBlogPostBot"


def is_valid_robots_txt(content):
    """Simple check for valid robots.txt files"""
    return "User-agent" in content or "Disallow" in content


r = requests.get(URL+"/robots.txt")

if is_valid_robots_txt(r.text):
    rp = Protego.parse(r.text)
    print(rp.can_fetch(URL+"/dwa22/comments", USER_AGENT))
    print(rp.can_fetch(URL+"/me/", USER_AGENT))
else:
    print("Cannot get robots.txt")