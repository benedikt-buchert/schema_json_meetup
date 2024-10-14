import json

from seleniumwire import webdriver  # Import from seleniumwire
from seleniumwire.utils import decode

from validator import validate_schema

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Go to the Google home page
driver.get('https://adobestore.com/-Escape-artist-tee-Art-by-Sam-Wilde-P1346.aspx')

# Access and print requests via the `requests` attribute
for request in driver.requests:
    if request.response and "58cd666d-494a-4431-b918-13ce94ef74e3" in request.url:
        body = request.body
        json_body = json.loads(decode(body, 'utf-8'))
        for event in json_body['events']:
            xdm = event['xdm']
            validate_schema("webSDKevent", xdm)
