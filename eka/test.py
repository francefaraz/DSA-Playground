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

# 1  Find avg rating out of 5
# 2  Find avg per type
average_ratings = []
for review in reviews_response[0]['reviews']:
    print(review)
    rating_values = [int(rate['value']) for rate in review['rating_votes']]
    avg_rating = sum(rating_values) / len(rating_values)
    print(avg_rating)
    average_ratings.append(avg_rating)
print(
    f'average rating out of 5 is {sum(average_ratings)/len(average_ratings)}')
# 3  Find avg per type

rating_types = {}
for rating in ratings_response:
    rating_code = rating['rating_code']
    rating_types[rating_code] = []
print(f"rating types are {rating_types}")

for review in reviews_response[0]['reviews']:
    for rate in review['rating_votes']:
        rating_code = rate['rating_code']
        rating_types[rating_code].append(int(rate['value']))

# for rating_code, values in rating_types.items():
#     avg_rating = sum(values) / len(values)
#     print(f'Average rating for {rating_code}: {avg_rating}')


def calculate_average_rating():
    average_ratings = []
    for review in reviews_response[0]['reviews']:
        rating_values = [int(rate['value']) for rate in review['rating_votes']]
        avg_rating = sum(rating_values) / len(rating_values)
        average_ratings.append(avg_rating)
    return sum(average_ratings)/len(average_ratings)

def calculate_average_rating_per_type():
    rating_types = {}
    for rating in ratings_response:
        rating_code = rating['rating_code']
        rating_types[rating_code] = []
        
    for review in reviews_response[0]['reviews']:
        for rate in review['rating_votes']:
            rating_code = rate['rating_code']
            rating_types[rating_code].append(int(rate['value']))

    for rating_code, values in rating_types.items():
        
        avg_rating = sum(values) / len(values) if values else 0
        print(f'Average rating for {rating_code}: {avg_rating}')


calculate_average_rating()
calculate_average_rating_per_type()



for rating_code, ratings in rating_types.items():
    average_rating_by_type = sum(ratings) / len(ratings) if ratings else 0
    print(f"  {rating_code}: {average_rating_by_type}")