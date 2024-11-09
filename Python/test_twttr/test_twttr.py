from twttr import shorten
def main():
    test_vowels()

def test_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("HI") == "H"
def test_number():
    assert shorten("123") == "123"
def test_punctuation():
    assert shorten("!,.?") == "!,.?"

if __name__ == "__main__":
    main()

