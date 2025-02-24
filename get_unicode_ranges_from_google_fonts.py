import re
import urllib.request

USER_AGENT = "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0"
CSS_URL = "https://fonts.googleapis.com/css2?family=Noto+Sans+JP"
OUTPUT_FILE_NAME = "unicode_ranges.txt"


def extract_unicode_ranges(text):
    pattern = r"^\s*unicode-range:\s+([^;]+);"
    matches = re.findall(pattern, text, flags=re.MULTILINE)
    matches = [i.upper() for i in matches]
    return matches


def main():
    url = CSS_URL
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    with urllib.request.urlopen(req) as response:
        data = response.read()
    text = data.decode("utf-8")

    unicode_ranges = extract_unicode_ranges(text)
    with open(OUTPUT_FILE_NAME, "w") as file:
        file.write("\n".join(unicode_ranges))


main()
