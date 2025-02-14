Great approach! You need to create a **dispatcher mechanism** inside the `core` class, where `execute(request_body)` dynamically calls the appropriate method (`create_account`, `get_cdrates`, etc.) based on the `"type"` field in `request_body`.  

---

### **1. Modify Service Classes (`Fiserv`, `Symitar`)**
These classes should have the required methods, such as `create_account()` and `get_cdrates()`.

```python
class Fiserv:
    def __init__(self, credentials):
        self.credentials = credentials

    def create_account(self, request):
        return f"Fiserv: Creating account with {request}"

    def get_cdrates(self, request):
        return f"Fiserv: Fetching CD rates with {request}"


class Symitar:
    def __init__(self, credentials):
        self.credentials = credentials

    def create_account(self, request):
        return f"Symitar: Creating account with {request}"

    def get_cdrates(self, request):
        return f"Symitar: Fetching CD rates with {request}"
```

---

### **2. Implement `Core` Class with `execute()`**
This class initializes the respective service (`Fiserv` or `Symitar`) and dynamically calls the correct method.

```python
class Core:
    services = {
        "fiserv": Fiserv,
        "symitar": Symitar
    }

    def __init__(self, service_name, credentials):
        if service_name.lower() not in self.services:
            raise ValueError(f"Unknown service: {service_name}")
        self.service = self.services[service_name.lower()](credentials)

    def execute(self, request_body):
        """Dynamically execute the correct method based on request_body type"""
        request_type = request_body.get("type")
        request_data = request_body.get("request", {})

        # Check if method exists in the service class
        if hasattr(self.service, request_type):
            method = getattr(self.service, request_type)
            return method(request_data)  # Call the method dynamically
        else:
            raise ValueError(f"Invalid request type: {request_type}")
```

---

### **3. Usage Example**
Now, you can create a `Core` object and call `execute(request_body)`, which will dynamically invoke the correct method.

```python
hq_credentials = {"username": "user123", "password": "pass123"}

# Request to create an account
request_body = {
    "type": "create_account",
    "request": {
        "account_number": "414237374",
        "account_group": 3
    }
}

# Initialize Core with Fiserv
c = Core("fiserv", hq_credentials)
print(c.execute(request_body))  
# Output: Fiserv: Creating account with {'account_number': '414237374', 'account_group': 3}

# Initialize Core with Symitar
c = Core("symitar", hq_credentials)
print(c.execute(request_body))  
# Output: Symitar: Creating account with {'account_number': '414237374', 'account_group': 3}

# Request to get CD rates
cd_rates_request = {
    "type": "get_cdrates",
    "request": {
        "term": 12,
        "amount": 10000
    }
}

print(c.execute(cd_rates_request))  
# Output: Symitar: Fetching CD rates with {'term': 12, 'amount': 10000}
```

---

### **🔹 How It Works**
1. The `Core` class takes `service_name` and `credentials` as input.
2. It initializes the corresponding service (`Fiserv` or `Symitar`).
3. When `execute(request_body)` is called:
   - It extracts the `"type"` field (e.g., `"create_account"`, `"get_cdrates"`) from `request_body`.
   - It checks if the method exists in the service class.
   - It dynamically calls the method with `request_data`.

---

### **🔹 Advantages**
✅ **Scalable** – You can easily add more services without changing existing logic.  
✅ **Flexible** – New request types can be added without modifying the core execution flow.  
✅ **Dynamic Execution** – No need for long if-else or switch statements.  

Would you like me to add logging or exception handling for better error tracking? 🚀