'''
HTML Tag Stripper
Given a string of HTML code, remove the tags and return the plain text content.

The input string will contain only valid HTML.
HTML tags may be nested.
Remove the tags and any attributes.
For example, '<a href="#">Click here</a>' should return "Click here".
'''


def strip_tags(html):
#We need to store the index of the open and closing tags
    open_tags = []
    close_tags = []
    tags = []
    for i,c in enumerate(html):
        if c == "<":
            open_tags.append(i)
            continue
        if c == ">":
            close_tags.append(i)
#This captures html content as it parses whole html strings
    for i in range(len(open_tags)):
        tags.append(html[open_tags[i]:close_tags[i]+1])
#We then remove each tags in the string by replacing it with nothing
    for i in range(len(tags)):
        html = html.replace(tags[i],"")

    return html