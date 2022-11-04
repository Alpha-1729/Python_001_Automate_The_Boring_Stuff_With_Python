#!/usr/bin/python3
# Web scraping

"""
>>>> Shortcut for view page source.
        Ctrl + U
     Shortcut for inspect element.
        Ctrl + Shift + I
>>>> pip install bs4
>>>> Here we are going to get the price of a particular product from the amazon website.
>>>> Use the Brave or Chrome browser to get the css path of the product.
>>>> Some useful websites for web-scraping.
        https://xkcd.com/1/    -> Which contain web comics, which can be extracted and sent via a telegram bot.
"""
import bs4
import requests

mozilla_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"}

def get_amazon_price(product_url):

    # Downloading the page.
    response = requests.get(product_url, headers=mozilla_headers)

    response.raise_for_status()  # Throw an exception if download fails.

    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # Selecting the css path.
    elements = soup.select(
        "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole")
    return elements[0].text.strip()

product_url = "https://www.amazon.in/Samsung-inch-Bezel-Flicker-Monitor-LF24T350FHWXXL/dp/B08J82K4GX/ref=sr_1_4?keywords=monitor&qid=1667139747&qu=eyJxc2MiOiI2Ljc3IiwicXNhIjoiNi42NyIsInFzcCI6IjUuOTcifQ%3D%3D&sr=8-4"

price = get_amazon_price(product_url)
print('The price is ' + price)

print(" ")
