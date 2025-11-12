import asyncio


def check_params(k=[]):

  def decorator(func):

    def wrapper(*args, **kwargs):
      print("kwars", kwargs)
      print(f"{args=}")
      # for arg in args:
      #     if arg is None:
      #         raise ValueError("Parameter cannot be None.")
      for key, value in args[0].items():
        if key in k and value is None:
          raise ValueError(f"Parameter {key} cannot be None.")
      return func(*args, **kwargs)

    return wrapper

  return decorator


keys = [
    "first_name", "last_name", "major_type_code", "minor_type_code", "TaxId"
]
request_body = {
    "FirstName": "Fiserv",
    "LastName": "Core",
    "AccountType": "SAV",
    "SubAccountType": "SREG",
    "PersonNumber": 213443,
    "TaxId": 232,
    "AgreementNumber": 9900
}


# @check_params(k=keys)
def account_main(first_name=None,
                 last_name=None,
                 major_type_code=None,
                 minor_type_code=None,
                 taxid=None,
                 person_number=None,
                 **kwargs):
  print("HELLO VALID BODY")
  return "FAR"


@check_params(
    k=["FirstName", "LastName", "AccountType", "SubAccountType", "TaxId"])
def create_account(request_body):
  print(" ENTERED INTO FISERV ACCOUNT OPEINING ")
  first_name = request_body['FirstName']
  last_name = request_body['LastName']
  major_type_code = request_body['AccountType']
  minor_type_code = request_body['SubAccountType']
  tax_id = request_body.get('TaxId', None)
  person_number = request_body.get('PersonNumber', None)
  print("VALID BODY")
  account_maintenance_response = account_main(first_name, last_name,
                                              major_type_code, minor_type_code,
                                              tax_id, person_number,
                                              **request_body)  # noqa: E501
  print(account_maintenance_response)

  return "ARU IS GOOD GIRL"


@check_params
def add(a, b):
  return a + b


# print(add(1, 2)) # Returns 3
# print(add(1, None)) # Raises ValueError

# print(create_account(request_body))


class Test:

  def __init__(self):

    pass

  @staticmethod
  @check_params(
      k=["FirstName", "LastName", "AccountType", "SubAccountType", "TaxId"])
  def create_account1(request_body):
    print(" ENTERED INTO class and calling FISERV ACCOUNT OPEINING ")
    first_name = request_body['FirstName']
    last_name = request_body['LastName']
    major_type_code = request_body['AccountType']
    minor_type_code = request_body['SubAccountType']
    tax_id = request_body.get('TaxId', None)
    person_number = request_body.get('PersonNumber', None)
    print("VALID BODY")
    # print("fara", Test.a)
    account_maintenance_response = Test.account_main1(
        first_name, last_name, major_type_code, minor_type_code, tax_id,
        person_number, **request_body)  # noqa: E501

  def account_main1(self,
                    first_name=None,
                    last_name=None,
                    major_type_code=None,
                    minor_type_code=None,
                    taxid=None,
                    person_number=None,
                    **kwargs):
    print("HELLO VALID BODY", dir(self))
    return "FAR"


Test.create_account1(request_body)
# loop = asyncio.get_event_loop()
# coroutine = Test.create_account1(request_body)
# loop.run_until_complete(coroutine)
# asyncio.run(Test.create_account1(request_body))


def hello_decorator(func):

  def inner1(*args, **kwargs):

    print("before Execution")

    # getting the returned value
    returned_valuis_renew_close_db_checke = func(*args, **kwargs)
    print("after Execution")

    # returning the value to the original frame
    return returned_value

  return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
  print("Inside the function")
  return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))
