import requests
from xml.etree import ElementTree as ET

# endpoint = "https://bus.ap-south-1.flightservices.cae.com"
endpoint = "https://bus.ap-south-1.certflightservices.cae.com/"

# Set headers
headers = {
    'Content-Type': 'text/xml',
}

def sendReq(body, filename):
    response_filename = f"output/output_{filename}.xml"
    error_filename = f"error/error_{filename}.xml"
    body_filename = f"body/body_{filename}.xml"
    
    with open(body_filename, 'w') as file:
        file.write(body)

    response = requests.post(endpoint, data=body, headers=headers)
    if 'ns19:Error' in response.text:
        print(f"    SOAP request failed. Writing to file {error_filename}")
        with open(error_filename, 'w') as file:
            file.write(response.text)
        return False
    else:
        print(f"    SOAP request successful. Writing to file {response_filename}")
        with open(response_filename, 'w') as file:
            file.write(response.text)
        return True
        