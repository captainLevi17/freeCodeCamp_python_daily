'''
Schema Validator Part 3
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles
}
The pipe (|) symbol means "or". role must be one of the listed Roles values.
Extra keys are allowed

'''

def is_valid_schema(obj):
    valid_roles = {"user", "creator", "moderator", "staff", "admin"}
    return (
        isinstance(obj, dict) and
        'username' in obj and isinstance(obj['username'], str) and
        'posts' in obj and isinstance(obj['posts'], (int, float)) and
        'verified' in obj and isinstance(obj['verified'], bool) and
        'role' in obj and obj['role'] in valid_roles
    )