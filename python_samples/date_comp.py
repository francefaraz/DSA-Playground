from datetime import datetime

date_string = "2024-09-24T00:00:00Z"
date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
now = datetime.utcnow()

if date_object < now:
    print("The date is in the past")
elif date_object > now:
    print("The date is in the future")
else:
    print("The date is now")

print(datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ") >= now)

request_data = {"avlStartDtm": "2022-01-01T05:00:00Z"}
print(
    request_data.get('avlStartDtm') is None, "aksdfjk",
    request_data.get('avlStartDtm'))
a = request_data.get('avlStartDtm') is None or (datetime.strptime(
    request_data.get('avlStartDtm'), "%Y-%m-%dT%H:%M:%SZ") >= datetime.now())
print("a is ", a)


def remove_after_underscore(s):
    return s.split('_')[0]

# Example usage
strings = ['ff2b1bdb-607c-4315-ac64-40ff450d9273_2', 'another_example_1']
modified_strings = [remove_after_underscore(s) for s in strings]

print(modified_strings)


def get_customer_id_and_group():
    primarycif = "ff2b1bdb-607c-4315-ac64-40ff450d92732_3"
    customer_details=primarycif.split('_')
    customer_id = customer_details[0]
    customer_group=customer_details[1] if len(customer_details)>1 else 0
    return customer_id, customer_group

print(get_customer_id_and_group())
customer_id,customer_group=get_customer_id_and_group()
print(customer_group,"dskaf",customer_id)
customer_id,_=get_customer_id_and_group()
print(_,"sadf")
