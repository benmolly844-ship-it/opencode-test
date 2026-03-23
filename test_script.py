# test_script.py - Sample code with intentional issues for OpenCode to review

def calculate_sum(list):
    """Calculate sum of a list."""
    total = 0
    for i in range(len(list)):
        total = total + list[i]
    return total

def process_data(data):
    result = []
    for item in data:
        if item != None:
            result.append(item)
    return result

def fetch_user(user_id):
    # TODO: implement actual API call
    return {"id": user_id, "name": "Test User"}

class DataProcessor:
    def __init__(self):
        self.data = []
    
    def add(self, item):
        self.data.append(item)
    
    def get(self):
        return self.data

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(calculate_sum(numbers))
    
    dp = DataProcessor()
    dp.add("test")
    print(dp.get())