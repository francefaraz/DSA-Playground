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

# even we can use set this in .json and then we can load here
#1 Find avg rating


def calculate_average_rating(reviews):
    average_ratings = []

    for review in reviews[0]['reviews']:
        rating_values = [int(rate['value']) for rate in review['rating_votes']]
        average_ratings.append(sum(rating_values) / len(rating_values))

    average_rating = sum(average_ratings) / len(average_ratings)
    return average_rating


#2 Find avg by type
def calculate_average_rating_by_type(reviews,ratings):
    average_ratings_by_type = {}
    rating_types = {}

    for rating in ratings:
        rating_types[rating['rating_code']] = []

    for review in reviews[0]['reviews']:
        for rate in review['rating_votes']:
            rating_types[rate['rating_code']].append(int(rate['value']))

    for rating_code, ratings in rating_types.items():
        average_rating_by_type = sum(ratings) / len(ratings) if ratings else 0
        print(f"  {rating_code}: {average_rating_by_type}")

print(f" average rating out of 5 is {calculate_average_rating(reviews_response)}")
print(f" averate rating by type is ")
calculate_average_rating_by_type(reviews_response,ratings_response)
