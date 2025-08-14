import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    for_iframe_r = r"<iframe.*>.+</iframe>$"
    if matche_for_iframe := re.search(for_iframe_r, s):
        pass
    else:
        return "None"
    pattern1 = r'src="(http://youtube\.com/embed/[^"]*)"'
    pattern2 = r'src="(https://youtube\.com/embed/[^"]*)"'
    pattern3 = r'src="(https://www\.youtube\.com/embed/[^"]*)"'
    if matches := re.search(pattern1, s):
        url = matches.group(1)
    elif matches := re.search(pattern2, s):
        url = matches.group(1)
    elif matches := re.search(pattern3, s):
        url = matches.group(1)
    else:
        return "None"
    pattern = r"embed/(.*)"
    if matches1 := re.search(pattern, url):
        tag = matches1.group(1)
    return (f"https://youtu.be/" + f"{tag}")


if __name__ == "__main__":
    main()
