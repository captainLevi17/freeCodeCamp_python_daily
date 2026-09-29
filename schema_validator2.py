'''
Schema Validator Part 2
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

{
  username: string,
  posts: number,
  verified: boolean
}
Extra keys are allowed


'''

def is_valid_schema(obj):
    if not isinstance(obj, dict):
        return False

    if 'username' not in obj or not isinstance(obj['username'], str):
        return False

    if 'posts' not in obj or not isinstance(obj['posts'], int):
        return False

    if 'verified' not in obj or not isinstance(obj['verified'], bool):
        return False

    return True