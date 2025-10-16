'''
Email Validator
Given a string, determine if it is a valid email address using the following constraints:

It must contain exactly one @ symbol.
The local part (before the @):
Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
Cannot start or end with a dot.
The domain part (after the @):
Must contain at least one dot.
Must end with a dot followed by at least two letters.
Neither the local or domain part can have two dots in a row.
'''

import re

def validate(email):
    # Must contain exactly one @
    if email.count('@') != 1:
        return False

    local, domain = email.split('@')

    # Local and domain cannot be empty
    if not local or not domain:
        return False

    # Local: letters, digits, dots, underscores, hyphens
    if not re.match(r'^[A-Za-z0-9._-]+$', local):
        return False

    # Local cannot start or end with a dot
    if local.startswith('.') or local.endswith('.'):
        return False

    # No consecutive dots in local
    if '..' in local:
        return False

    # Domain must contain at least one dot
    if '.' not in domain:
        return False

    # No consecutive dots in domain
    if '..' in domain:
        return False

    # Domain must end with a dot followed by at least two letters
    if not re.search(r'\.[A-Za-z]{2,}$', domain):
        return False

    # Allow broader domain characters (letters, digits, hyphen, exclamation, etc.)
    if not re.match(r'^[A-Za-z0-9!._-]+$', domain):
        return False

    return True
