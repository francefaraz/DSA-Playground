class AFCU:

    def __init__(self, credentials):
        self.credentials = credentials

    def create_account(self, request_body):
        print("Creating account with AFCU:", request_body)
        return "AFCU account created"

    def get_cd_rates(self, request_body):
        print("Getting currency rates with AFCU:", request_body)
        return "AFCU currency rates retrieved"


class FisIbs:

    def __init__(self, credentials):
        self.credentials = credentials

    def create_account(self, request_body):
        print("Creating account with FISIBS:", request_body)
        return "FISIBS account created"

    def get_cd_rates(self, request_body):
        print("Getting currency rates with FISIBS:", request_body)
        return "FISIBS currency rates retrieved"


class Core:

    def __init__(self, service_instance):
        self.service = service_instance

    def execute(self, request_body):
        request_type = request_body.get("type")
        request_data = request_body.get("request")
        # #manual checking type and calling
        # if request_type == "create_account":
        #     self.service.create_account(request_data)
        # elif request_type == "get_cd_rates":
        #     self.service.get_cd_rates(request_data)
        # else:
        #     raise ValueError("Unsupported request type")
        #using getattr and calling method dynamic
        if hasattr(self.service, request_type):
            method = getattr(self.service, request_type)
            return method(request_data)
        else:
            raise ValueError(f"Invalid request type: {request_type}")


def get_service(service_name, credentials):
    services = {"afcu": AFCU, "fisibs": FisIbs}

    if service_name.lower() not in services:
        raise ValueError("Unsupported service type  " + str(service_name))

    return services[service_name.lower()](credentials)


hq_credentials = "your_hq_credentials"
service_name = "FISIBS"

service_instance = get_service(service_name, hq_credentials)
core_instance = Core(service_instance)

request_body_create = {
    "type": "create_account",
    "request": {
        "account_number": "414237374",
        "account_group": 3
    }
}

result_create = core_instance.execute(request_body_create)
print(result_create)

request_body_rates = {"type": "get_cd_rates", "request": {"currency": "USD"}}

result_rates = core_instance.execute(request_body_rates)
print(result_rates)
# dynamic dispatcher mechanisim 