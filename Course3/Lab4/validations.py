#!/usr/bin/env python3
import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if not isinstance(minlen, int) or minlen < 1:
        raise ValueError("minlen must be a positive integer")

    if not isinstance(username, str) or len(username) < minlen:
        return False
    
    # Check for empty username
    if not username:
        return False
    
    # Usernames can only use letters, numbers, dots, and underscores
    if not re.search(r'^[a-zA-Z][a-zA-Z0-9._]*$', username):
        return False
    
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False

