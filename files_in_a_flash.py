"""An implementation of Naive Bayes to sort files by theme."""

def files_in_a_flash(path):
    """ Sorts files in the 'unsorted' directory (see notes) by theme.

    Parameters
    ----------
    path : The path to the main directory. (str)

    Notes
    -----
    The main directory should countain :
        - labels.txt
        - a sub-directory named 'sorted' that countains the sorted files to learn from.
        - a sub-directory named 'unsorted' that countains the files to sort.
    """
    pass

def get_words(path):
    """ Creates a list of all useful words in the given text file.

    Parameters
    ----------
    path : the path to the .txt file to read (str).

    Returns
    -------
    words : a list of all useful words in the text file.
    """
    # Get text from the given file.
    current_file = open(path, 'r')
    text = current_file.read().lower()
    current_file.close()

    #Define the useless words/elements.
    useless_elements = ['\n', '/', '\t', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ', ',
                        '?', '!', '.', ';', '-', '\'', '(', ')', '@', '>', '<', ':', ' you ',
                        ' they ', ' she ', ' he ', ' it ', ' your ', ' their ', ' we ', ' is ',
                        ' are ', ' have ', ' has ', ' or ', ' and ', ' an ', ' the ', ' of ',
                        ' in ', ' to ', ' if ', ' to ', ' for ', ' them ', ' my ', ' me ', ' its ',
                        ' yours ', ' as ', 'from ', ' by ', ' on ', ' will ', ' not ', ' no ',
                        ' yes ', ' any ', ' be ', ' etc ', ' but ', ' would ', ' been ', ' had ',
                        ' this ']

    #Replace each useless element by a space.
    for element in useless_elements:
        text = str.replace(text, element, ' ')

    #Put all words in a list.
    words_list = text.split(' ')

    #Create and return a list of every useful words.
    useful_list = []
    for word in words_list:
        if not word in useful_list and len(word) > 1:
            useful_list.append(word)
    return useful_list

def get_frequencies(path):
    """ Creates a dictionary that countains the frequency of each useful word in the given theme.

    Parameters
    ----------
    path: the path to the theme directory to evaluate. (str)

    Returns
    -------
    theme_frequencies : a dictionary of format { word (str) : frequency (float) }.
    """
    pass

def check_differences(frequencies):
    """ Checks the given frequencies in order to have the same word list in each theme.

    Parameters
    ----------
    frequencies : a dictionary of format { theme (str) : theme_frequencies (dict) }.

    Notes
    -----
    The frequencies dictonary is edited: the theme_frequencies dictionaries may be lenghtened.
    All theme_frequencies dictionaries should be of the same size afterwards.

    See also
    --------
    get_frequencies to create the theme_frequencies dictionaries.
    """
    pass

def get_theme_prob(theme_frequencies, list_words):
    """Computes the probability that the word list matches the given theme.

    Parameters
    ----------
    theme_frequencies: a dictionary of format { word (str) : frequency (float) }
    list_words: a list of useful words from a text file (str).

    Returns
    -------
    probability: the probability that the file belongs to the given theme.

    See also
    --------
    get_words to get the list of the useful words in a text file.
    get_frequencies and check_frequencies to create the theme_frequencies dictionary."""
    pass


def check_accuracy(path):
    """ Checks if the files are correctly sorted in  and prints the accuracy.

    Parameters
    ----------
    path : The path (str) to the main directory.

    Notes
    -----
    The main directory should countain :
        - labels.txt
        - a sub-directory named 'sorted' that countains the sorted files.
        - a sub-directory named 'unsorted' that countains the files to sort. (should be empty)
    """
    pass
