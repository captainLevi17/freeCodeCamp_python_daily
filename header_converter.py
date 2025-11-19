'''
Markdown Heading Converter
Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

Start with zero or more spaces, followed by
1 to 6 hash characters (#) in a row, then
At least one space. And finally,
The heading text.
The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return "Invalid format".

For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".
'''

def convert(heading):
    heading = heading.strip()
    heading = heading.split(" ")
    for i in heading:
        if i == "":
            heading.remove(i)
    if heading[0].count("#") > 6 or heading[0].count("#") < 1:
        return "Invalid format"
    characters = heading[0].count("#")
    if len(heading[0]) != characters:
        return "Invalid format"
    if characters == 1:
        return f"<h1>{' '.join(heading[1:])}</h1>"
    if characters == 2:
        return f"<h2>{' '.join(heading[1:])}</h2>"
    if characters == 3:
        return f"<h3>{' '.join(heading[1:])}</h3>"
    if characters == 4:
        return f"<h4>{' '.join(heading[1:])}</h4>"
    if characters == 5:
        return f"<h5>{' '.join(heading[1:])}</h5>"
    


#Pseudocode
    # Trim leading and trailing spaces
    # Convert into list
    # Remove empty strings from list
    # Check if first element has #, if not return invalid format
    # Count number of #, if more than 6 return invalid format
    # Check if next element is space, if not return invalid format
    # Join the rest of the list into a string for heading text
