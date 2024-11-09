def main():
    extension = input("File name: ").lower()
    print(file(extension))
def file(ok):
    if ".gif" in ok:
        return "image/gif"
    elif ".jpg" in ok:
        return "image/jpeg"
    elif ".jpeg" in ok:
        return "image/jpeg"
    elif ".png" in ok:
        return "image/png"
    elif ".pdf" in ok:
        return "application/pdf"
    elif ".txt" in ok:
        return "text/plain"
    elif ".zip" in ok:
        return "application/zip"
    else:
        return "application/octet-stream"
