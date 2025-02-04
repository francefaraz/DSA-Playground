import requests
from requests.auth import HTTPBasicAuth
import base64
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

auth = HTTPBasicAuth('nueve', 'e7714e8b-aefd-4f04-ac1d-f6fbb61e1d36')
url = 'https://api.sandbox.transferwise.tech/oauth/token'
payload = 'grant_type=client_credentials'

response = requests.request("POST",
                            url,
                            headers=headers,
                            data=payload,
                            auth=auth)
print(response)

print(response.json())

url = "https://symitar-proxy-u9sjqv.sv84rs.usa-e1.cloudhub.io/"

payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:par=\"http://www.symxchange.generated.symitar.com/parameter\" xmlns:tns=\"http://www.symxchange.generated.symitar.com/common/dto/common\">\r\n    <soapenv:Header/>\r\n    <soapenv:Body>\r\n        <par:searchShareDefaultPagedSelectFields>\r\n            <Request MessageId=\"9999\" par:BranchId=\"1\">\r\n                <Credentials tns:ProcessorUser=\"1\">\r\n                    <AdministrativeCredentials>\r\n                        <Password>!99APIPEOPLE</Password>\r\n                    </AdministrativeCredentials>\r\n                </Credentials>\r\n                <DeviceInformation DeviceType=\"APIPEOPLE\" DeviceNumber=\"20681\"/>\r\n                <PagingRequestContext>\r\n                </PagingRequestContext>\r\n                <SelectableFields>\r\n                    <IncludeAllShareDefaultFields>false</IncludeAllShareDefaultFields>\r\n                    <ShareDefaultFields>\r\n                        <Description>true</Description>\r\n                        <DivRate>true</DivRate>\r\n                        <DivType>true</DivType>\r\n                        <ShareCode>true</ShareCode>\r\n                        <ShareType>true</ShareType>\r\n                        <TermFrequency>true</TermFrequency>\r\n                        <TermPeriod>true</TermPeriod>\r\n                        <Type>true</Type>\r\n                    </ShareDefaultFields>\r\n                </SelectableFields>\r\n                <Query>(PENALTYTYPE &lt;&gt; 0 and ShareCode=2 and DivRate &lt;&gt; 0)</Query>\r\n            </Request>\r\n        </par:searchShareDefaultPagedSelectFields>\r\n    </soapenv:Body>\r\n</soapenv:Envelope>"
headers = {
    'service': 'ParameterService',
    'Content-Type': 'application/xml',
}
# auth1 = HTTPBasicAuth('nuevesolutions', 'KWN3FpjcGfytUpAr')
username="nuevesolutions"
password="KWN3FpjcGfytUpAr"
token = base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')
headers.update({'Authorization':"Basic "+token})
# print(dir(auth1))
print(headers)
# print(auth1._credentials.encode('utf-8'))
response = requests.request("POST",
                            url,
                            headers=headers,
                            data=payload,
                        )

print(response.text)
