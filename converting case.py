from typing import Callable, Any, Union
from pydash import camel_case

Normalizer = Callable[[str], str]


def _normalize_keys(data: Any, normalizer: Normalizer, depth: int = 0):    \
    # payload = self._normalize_keys(payload, normalizer)  normalizer = camel_case

  if isinstance(data, list):
    items = []
    for item in data:
      items.push(_normalize_keys(item, normalizer, depth))
    return items
  if isinstance(data, dict):
    result = {}
    for key, value in data.items():
      if depth and (isinstance(value, dict) or isinstance(value, list)):
        value = _normalize_keys(value, normalizer, depth - 1)
      result[normalizer(key)] = value
    return result
  return data


payload = {
    "AccountGroupNumber": None,
    "AccountNumber": 702960580,
    "MajorTypeCode": "TD",
    "MinorTypeCode": "SC24"
}
normalize = True
if normalize:
  normalizer = camel_case
  if callable(normalize):
    normalizer = normalize
print(callable(True))
print(normalizer)
result = _normalize_keys(payload, normalizer)
print(result)
