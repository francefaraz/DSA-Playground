def get_core_value(hostname, core_dict):
  for core, subdomains in core_dict.items():
    for subdomain in subdomains:
      if subdomain in hostname:
        return core
  return None  # Return None if no match is found


# Example dictionary
core_dictionary = {
    "FISERV": ['sfcu', 'andrews', 'bell'],
    "SYMITAR": ['camino', 'htfffcu', 'velocitycu']
}

# Example hostname
example_hostname = "fi.htfffcuonline.org"

# Get the core value based on the hostname
result = get_core_value(example_hostname, core_dictionary)

# Print the result
print(result)
