'''
Browser History
Given an array of browser commands, return an array with two values: the history as an array of URLs, and the index of the current page.

Valid commands are:

"URL" - Where URL is a web address ("freecodecamp.org" for example). Navigates to the given URL, adds it to the history at the next position, and discards any forward history.
"Back" - moves to the previous page in history, or stays on the current page if there isn't one.
"Forward" - moves to the next page in history, or stays on the current page if there isn't one.
For example, given ["freecodecamp.org", "freecodecamp.org/learn", "Back"], return [["freecodecamp.org", "freecodecamp.org/learn"], 0].

'''

def get_browser_history(commands):

    history = []
    current_index = -1
    for command in commands:
        if command == "Back":
            if current_index > 0:
                current_index -= 1
        elif command == "Forward":
            if current_index < len(history) - 1:
                current_index += 1
        else:  # It's a URL
            # If we navigate to a new URL, we need to discard forward history
            history = history[:current_index + 1]
            history.append(command)
            current_index += 1

    return [history, current_index]