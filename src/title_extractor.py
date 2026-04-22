def extract_title(markdown):
    for line in markdown.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            title = line[2:].strip()
            return title
            
    raise Exception("No h1 tag found in the markdown")



            