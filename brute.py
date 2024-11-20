import string

# Function to perform brute force attack on the password
def brute_force_attack(target_password):
    chars = string.ascii_lowercase  # Set of characters to try (lowercase letters)
    attempt = ""
    attempts = 0
    
    # Try all possible combinations
    for char1 in chars:
        for char2 in chars:
            for char3 in chars:
                attempt = char1 + char2 + char3  # Combine characters
                attempts += 1
                if attempt == target_password:
                    print(f"Password found: {attempt} after {attempts} attempts!")
                    return attempt
    print("Password not found.")
    return None

# Example usage
target_password = "vin"  # Set your target password here
brute_force_attack(target_password)