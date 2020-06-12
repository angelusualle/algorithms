def urlify(url, length):
    urlified_string = ""
    i = 0
    while i < length:
        if url[i] == " ":
            urlified_string += "%20"
        else:
            urlified_string += url[i]
        i += 1
    return urlified_string