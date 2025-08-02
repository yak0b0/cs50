SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron ",
    "the Proud family"
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append((show.title().strip()))
    for show in cleaned_shows:
        print(show)


main()
