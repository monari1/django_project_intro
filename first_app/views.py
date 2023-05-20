import json
from django.shortcuts import render
from pprint import pprint
# Create your views here.

# pip install requests
import requests

url = 'https://accounts.multitenant.slade360.co.ke/oauth2/token/'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = {
    "grant_type": "password",
    "client_id": "BNMNhPJiab8yWgXz1pPE9HkocMqECU8n9o4Ico6Y", # Substitute with your client_id,
    "client_secret": "4KmwY3cmDgip54RG1kEgmqnNYRzTZLhuA1za8tEd3RxmzJ7Yg8NtvJHNGL3ViyM5uqOXaHs9eLudEvVkonBmxIxCtwb141DPYa9cq4CFmcjVGasCurFp4w9jMeKgHuSa", # Substitute with your client_secret.
    "username": "francismonari250@gmail.com", # Your email.
    "password": "xavier10", # Your healthcloud account password.
}
response = requests.post(url, data=data, headers=headers)
response.raise_for_status()
print(response.status_code)
#data = response.json()

#pprint(data)

access_token = '8uYeuKJY8YwvEtACqLFauxS12XXdPE'

def get_logged_in_user():
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    response = requests.get(
    'https://accounts.multitenant.slade360.co.ke/v1/user/me/',
    headers=headers)
    response.raise_for_status()
    return print(response.json())
#get_logged_in_user()

def get_member_eligibility():
    member_number = 'DEMO/001'
    payer_slade_code = '457'
    headers = {'Authorization': 'Bearer {}'.format(access_token)}

    url = (
    'https://provider-edi-api.multitenant.slade360.co.ke/v1/beneficiaries/'
    'member_eligibility/?member_number={}&payer_slade_code={}'.format(
        member_number, payer_slade_code
    )
    )

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return pprint(response.json())

#get_member_eligibility()


def request_otp():
    member_number = 'DEMO/001'
    payer_slade_code = '457'
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    url = (
    'https://provider-edi-api.multitenant.slade360.co.ke/v1/beneficiaries/beneficiary_contacts/5531/send_otp/'
    )
    

    response = requests.post(url, headers=headers)
    response.raise_for_status()
    
    return pprint(response.json())

#request_otp()
def start_visit_via_otp():
    # member_number = 'DEMO/001'
    # payer_slade_code = '457'
    payload = {
    "beneficiary_id": 636561,
    "factors": [
        "OTP"
    ],
    "benefit_type": "OUTPATIENT",
    "benefit_code": "BEN/001",
    "policy_number": "POL/001",
    "policy_effective_date": "2023-01-01T00:00:00+03:00",
    "otp": 720291,
    "beneficiary_contact": +254790360360,
    "scheme_name": "Muungano Scheme",
    "scheme_code": "POL/001"
    }
    headers = {'Authorization': 'Bearer {}'.format(access_token) ,"Content-Type": 'application/json'}
    url = (
        'https://is-api.multitenant.slade360.co.ke/v1/authorizations/start_visit/'
    )
    
    response = requests.post(url, headers=headers, json = payload)
    # if response.status_code != 200:
    #     print(f"Error in response: {response}")
    #     return
    return pprint(response.json())
#start_visit_via_otp()

# # def validate_authorization_token():
# #     {
# #     "first_name": "John",
# #     "last_name": "Kerry",
# #     "other_names": "string",
# #     "member_number": "DEMO/001",
# #     "auth_token": "CGY7WNU8S8",
# #     "visit_type": "OUTPATIENT",
# #     "scheme_code": "string",
# #     "scheme_name": "string",
# #     "payer_code": "string"
# #     }
# #     return x
# # #validate_authorization_token()

# # def create_balance_reservation():
# #     {
# #     "authorization": "35b36a8a-6799-4ab5-81d8-1635adef3a6b",
# #     "invoice_number": "ORE1234/22",
# #     "amount": 2500
# #     }