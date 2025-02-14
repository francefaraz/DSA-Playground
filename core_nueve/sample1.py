class AFCU:

    def __init__(self, credentials):
        self.credentials = credentials

    def create_account(self, request_body):
        print("Creating account with AFCU:", request_body)
        return "AFCU account created"

    def get_cdrates(self, request_body):
        print("Getting currency rates with AFCU:", request_body)
        return "AFCU currency rates retrieved"


class FisIbs:

    def __init__(self, credentials):
        self.credentials = credentials

    def create_account(self, request_body):
        print("Creating account with FISIBS:", request_body)
        return "FISIBS account created"

    def get_cdrates(self, request_body):
        print("Getting currency rates with FISIBS:", request_body)
        return "FISIBS currency rates retrieved"


class Core:

    def __init__(self, service_instance):
        self.service = service_instance

    def create_account(self, request_body):
        return self.service.create_account(request_body)

    def get_cdrates(self, request_body):
        return self.service.get_cdrates(request_body)


def get_service(service_name, credentials):
    services = {"afcu": AFCU, "fisibs": FisIbs}

    if service_name.lower() not in services:
        raise ValueError("Unsupported service type  " + str(service_name))

    return services[service_name.lower()](credentials)


hq_credentials = "your_hq_credentials"
service_name = "fisibs"

service_instance = get_service(service_name, hq_credentials)
core_instance = Core(service_instance)

request_body = {"account_name": "Test Account"}

result_create = core_instance.create_account(request_body)
print(result_create)

result_rates = core_instance.get_cdrates(request_body)
print(result_rates)
