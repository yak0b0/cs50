import requests

# me sending a requests to get their data and them giving me a response
# JSON - JavaScript Object Notation


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist}
        )
        response.raise_for_status()  # check if response is valid
    except (requests.HTTPError, requests.ConnectionError, requests.ConnectTimeout):
        print("Couldn't complete request")
        return
    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()
