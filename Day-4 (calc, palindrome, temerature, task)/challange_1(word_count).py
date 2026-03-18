"""
   Here i performed a word count in a user given string
   and return a total number of word occurs in a string. 
"""

# ------------------------------------------------------------

def count_word_frequency(paragraph: str) -> dict:
    """
    count frequency of each word in a paragraph.

    Args:
        paragraph (str): Input text string

    Return:
        Dictionary of repeted word.
    """
    paragraph = paragraph.lower()

    for char in ",.:?!":
        paragraph = paragraph.replace(char, "")

    word_count = {} # Empty dict

    for word in paragraph.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count   

# ------------------------------------------------------------

def main() -> None:
    """
    Main function to run program.
    """
    paragraph = input("Enter a paragraph:\n")

    result = count_word_frequency(paragraph)

    print(result)

# ------------------------------------------------------------

if __name__ == '__main__':
    main()    



