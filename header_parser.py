def get_headings(csv):
    #split the strings into a list by commas
    header = csv.split(",")
    #strip any whitespace from each heading
    header = [h.strip() for h in header]
    return header