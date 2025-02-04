import json


def calculate_average_rating(reviews):
  """Calculates the average rating of a product based on its reviews.

  Args:
    reviews: A list of review objects.

  Returns:
    The average rating of the product.
  """

  review_averages = []
  for review in reviews:
    rating_values = [int(vote['value']) for vote in review['rating_votes']]
    review_average = sum(rating_values) / len(rating_values)
    review_averages.append(review_average)

  return sum(review_averages) / len(review_averages)


def calculate_average_per_type(reviews):
  """Calculates the average rating for each rating type.

  Args:
    reviews: A list of review objects.

  Returns:
    A list of dictionaries, where each dictionary contains a rating code and its average.
  """

  rating_votes_by_type = {}
  for review in reviews:
    for vote in review['rating_votes']:
      rating_code = vote['rating_code']
      if rating_code not in rating_votes_by_type:
        rating_votes_by_type[rating_code] = []
      rating_votes_by_type[rating_code].append(int(vote['value']))
  print(f"rating votes by type is {rating_votes_by_type} {rating_votes_by_type.items()} {type(rating_votes_by_type.items())} ")
  average_per_type = []
  for rating_code, values in rating_votes_by_type.items():
    average = sum(values) / len(values)
    average_per_type.append({'rating_code': rating_code, 'average': average})

  return average_per_type


# Assuming you have the review data in a JSON file
with open('reviews.json', 'r') as f:
  reviews = json.load(f)

average_rating = calculate_average_rating(reviews)
average_per_type = calculate_average_per_type(reviews)

print("Average Rating:", average_rating)
print("Average Per Type:", average_per_type)
