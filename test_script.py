# test_script.py - Sample code with fixes applied

def calculate_sum(numbers):
    """Calculate sum of a list of numbers using built-in sum()."""
    return sum(numbers)

def process_data(data):
    """Filter out None values from data."""
    return [item for item in data if item is not None]

def fetch_user(user_id):
    """Fetch user data from API.
    
    Raises:
        NotImplementedError: If API client is not configured.
    """
    raise NotImplementedError("API client not configured for fetch_user")

class DataProcessor:
    """Process and store data items."""
    
    def __init__(self):
        self._data = []
    
    def add(self, item):
        """Add an item to the processor."""
        self._data.append(item)
    
    def get_all(self):
        """Return all stored items."""
        return self._data.copy()

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(f"Sum: {calculate_sum(numbers)}")
    
    dp = DataProcessor()
    dp.add("test")
    print(f"Data: {dp.get_all()}")