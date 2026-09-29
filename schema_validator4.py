'''
Schema Validator Part 4
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean
}
The pipe (|) symbol means "or". role must be one of the listed Roles values.
The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
Extra keys are allowed


'''


def is_valid_schema(obj):
    valid_roles = {"user", "creator", "moderator", "staff", "admin"}
    return (
        isinstance(obj, dict) and
        'username' in obj and isinstance(obj['username'], str) and
        'posts' in obj and isinstance(obj['posts'], (int, float)) and not isinstance(obj['posts'], bool) and
        'verified' in obj and isinstance(obj['verified'], bool) and
        'role' in obj and obj['role'] in valid_roles and
        ('supporter' not in obj or isinstance(obj['supporter'], bool))
    )   