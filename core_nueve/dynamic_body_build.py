import os
import json
from datetime import datetime


def build_dynamic_body(renew_account_request_body,form_fields, config):
    for key, form_key in config.get("renew_with_diff_terms", {}).items():
        print("hello")
        renew_account_request_body["request"][key] = form_fields.get(form_key)


# Mock of form_fields (in real code, this comes from user input)
form_fields = {
    "accountIds": "123456",
    "renewSubAccountType": "TypeA",
    "shareId": "SH123",
    "TDVnValue": "5.5",
    "interestRate": "2.0",
    "maturityDate": "2025-02-26",
    "renewTerm": "12M",
    "renewTermId": "RT12",
    "interestPlan": "Standard",
    "MaturityDate": "2026-02-26",
    "lastMaturityDate": "2024-02-26",
    "personIdentityNumber": "P123456",
    "accountNumber": "987654",
    "renewAccountType": "Savings",
    "depositRateIndex": "35",
    "PositionNumber": "4xxVeFCS7ZtiiTAT-RxozMlw",
    "MaturityOption": "1",
    "RenewProduct": "CD9_Prod",
    "TdId": 2
}

# Load additional keys from environment variable
config_str = os.getenv(
    "RENEW_CONFIG",
    '{"renew_with_diff_terms":{"td_id":"TdId","last_maturity_date":"LastMaturityDate"}}'
)

config = json.loads(config_str)
print("config is ", config)
# Define your request body
renew_account_request_body = {
    "request": {
        "account_number":
        form_fields.get('accountIds'),
        "renew_sub_account_type":
        form_fields.get('renewSubAccountType'),
        "effective_date":
        str(datetime.utcnow()),
        "share_id":
        form_fields.get('shareId'),
        "td_vn_value":
        form_fields.get('TDVnValue'),
        "interest_rate":
        form_fields.get('interestRate'),
        "old_maturity_date":
        form_fields.get('maturityDate'),
        "term":
        form_fields.get('term', '0 0'),
        "is_immediate_change":
        True,
        "renewal_id":
        form_fields.get('renewalShareId'),
        "account_serial":
        form_fields.get('accountSerial'),
        "member_number":
        form_fields.get('memberNumber', 1234),
        "renew_term":
        form_fields.get('renewTerm'),
        "renew_term_id":
        form_fields.get('renewTermId'),
        "interest_plan":
        form_fields.get('interestPlan'),
        "new_maturity_date":
        form_fields.get('MaturityDate'),
        "last_maturity_date":
        form_fields.get('lastMaturityDate'),
        "person_identity_number":
        form_fields.get('personIdentityNumber'),
        "maturity_date":
        form_fields.get('maturityDate'),
        "maturity_post_code":
        "XYZ123",  # Example constant
        "institution_number":
        "IN12345",  # Example constant
        "person_account_id":
        form_fields.get('accountNumber'),
        "renew_account_type":
        form_fields.get('renewAccountType'),
        "deposit_rate_code":
        form_fields.get('depositRateIndex', "30"),
        "position_number":
        form_fields.get('PositionNumber', "4xxVeFCS7ZtiiTAT-RxozMlw"),
        "maturity_option":
        form_fields.get('MaturityOption', 2),
        "renew_product":
        form_fields.get('RenewProduct', 'CD9_Test')
    }
}

# Dynamically append additional fields from config

build_dynamic_body(renew_account_request_body,form_fields,config)
# Print final request body
print(json.dumps(renew_account_request_body, indent=2))
