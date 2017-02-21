from bs4 import BeautifulSoup
import urllib.request
import time

startIdx = 3456047
operationRange = 1000000
operationTerm = 1;

TARGET_ENDPOINT = "http://bbs.icnkr.com/forum.php?mod=viewthread&tid=%d&mobile=2"

while startIdx < startIdx + operationRange:
    startIdx += 1
    response = urllib.request.urlopen(TARGET_ENDPOINT % startIdx).read()
    soup = BeautifulSoup(response, 'html.parser')

    contentData = soup.find("div", {"class": "message"})
    # contentImages = contentData.find("img")
    if contentData is None:
        print("Data not found")
    else:
        print(contentData.text.strip())
        # print(contentImages)
        time.sleep(1)
