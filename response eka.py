reviews_response = [{
    "avg_rating_percent":
    "90",
    "count":
    2,
    "reviews": [{
        "review_id":
        "9",
        "created_at":
        "2016-11-07 10:59:58",
        "entity_id":
        "1",
        "entity_pk_value":
        "2",
        "status_id":
        "1",
        "detail_id":
        "9",
        "title":
        "awesome for going back and forth",
        "detail":
        "This is awesome for going back and forth to class. I live off campus and it's a longer walk, but this pack fits comfortably and I can even store my laptop in the main compartment.",
        "nickname":
        "Gaston",
        "customer_id":
        None,
        "entity_code":
        "product",
        "rating_votes": [{
            "vote_id": "9",
            "option_id": "20",
            "remote_ip": "127.0.0.1",
            "remote_ip_long": "2130706433",
            "customer_id": None,
            "entity_pk_value": "2",
            "rating_id": "4",
            "review_id": "9",
            "percent": "100",
            "value": "5",
            "rating_code": "Quality",
            "store_id": "1"
        }, {
            "vote_id": "13",
            "option_id": "127",
            "remote_ip": "127.0.0.1",
            "remote_ip_long": "2130706433",
            "customer_id": None,
            "entity_pk_value": "2",
            "rating_id": "3",
            "review_id": "120",
            "percent": "60",
            "value": "3",
            "rating_code": "Price",
            "store_id": "1"
        }]
    }, {
        "review_id":
        "10",
        "created_at":
        "2016-11-07 10:59:58",
        "entity_id":
        "1",
        "entity_pk_value":
        "2",
        "status_id":
        "1",
        "detail_id":
        "10",
        "title":
        "comfy and i don't feel like a loser",
        "detail":
        "comfy and i don't feel like a loser carrying it.",
        "nickname":
        "Issac",
        "customer_id":
        None,
        "entity_code":
        "product",
        "rating_votes": [{
            "vote_id": "10",
            "option_id": "19",
            "remote_ip": "127.0.0.1",
            "remote_ip_long": "2130706433",
            "customer_id": None,
            "entity_pk_value": "2",
            "rating_id": "4",
            "review_id": "10",
            "percent": "80",
            "value": "4",
            "rating_code": "Quality",
            "store_id": "1"
        }, {
            "vote_id": "11",
            "option_id": "27",
            "remote_ip": "127.0.0.1",
            "remote_ip_long": "2130706433",
            "customer_id": None,
            "entity_pk_value": "2",
            "rating_id": "3",
            "review_id": "150",
            "percent": "40",
            "value": "2",
            "rating_code": "Price",
            "store_id": "1"
        }]
    }]
}]

ratings_response = [{
    "rating_id": "3",
    "entity_id": "1",
    "rating_code": "Price",
    "position": "0",
    "is_active": "1",
    "store_id": "1"
}, {
    "rating_id": "4",
    "entity_id": "1",
    "rating_code": "Quality",
    "position": "0",
    "is_active": "1",
    "store_id": "1"
}, {
    "rating_id": "2",
    "entity_id": "1",
    "rating_code": "Value",
    "position": "0",
    "is_active": "1",
    "store_id": "1"
}]

total_rating = 0
count = 0

for review in reviews_response[0]['reviews']:
  for rating_vote in review['rating_votes']:
    total_rating += int(rating_vote['value'])
    count += 1

avg_rating = total_rating / count
print("Average rating out of 5:", avg_rating)

ratings_dict = {}

for rating in ratings_response:
  ratings_dict[rating['rating_code']] = {'sum': 0, 'count': 0}

# for review in reviews_response[0]['reviews']:
#   for rating_vote in review['rating_votes']:
#     ratings_dict[rating_vote['rating_code']]['sum'] += int(
#         rating_vote['value'])
#     ratings_dict[rating_vote['rating_code']]['count'] += 1
# print(ratings_dict.items(), "hello")
# for rating_code, rating_data in ratings_dict.items():
#   avg_rating = rating_data['sum'] / rating_data['count']
#   print(f"Average rating for {rating_code}: {avg_rating}")


total_rating = 0
count = 0

for review in reviews_response[0]['reviews']:
    for rating_vote in review['rating_votes']:
        rating_out_of_5 = int(rating_vote['percent']) / 100 * 5
        total_rating += rating_out_of_5
        count += 1

avg_rating_out_of_5 = total_rating / count
print("Average rating out of 5:", avg_rating_out_of_5)