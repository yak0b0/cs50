def main():
    file_name = input("File name: ")
    file_type(file_name)


def file_type(file_ending):
    ready_file_txt = file_ending.strip().lower()
    if ready_file_txt.endswith(".gif"):
        print("image/gif")
    elif ready_file_txt.endswith(".jpg"):
        print("image/jpeg")
    elif ready_file_txt.endswith(".jpeg"):
        print("image/jpeg")
    elif ready_file_txt.endswith(".png"):
        print("image/png")
    elif ready_file_txt.endswith(".pdf"):
        print("application/pdf")
    elif ready_file_txt.endswith(".txt"):
        print("text/plain")
    elif ready_file_txt.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()
