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
    pass

def get_frequencies(path):
    """ Creates a dictionary that countains the frequency of each useful word in each theme.

    Parameters
    ----------
    path: the path to the sorted directory (str).

    Returns
    -------
    frequencies : a dictionary of format { theme (str) : theme_frequencies (dict) }.
    
    Notes
    -----
    Each theme_frequencies dictionary is of format { word (str) : frequency (float) }.
    """
    #Initialize the frequencies dictionary
    frequencies = {}

    #For each theme
    for theme in os.listdir(path):

        #Create the theme_frequencies dictionary
        frequencies[theme] = {}

        #For each word of each file of this theme
        for current_file in os.listdir('%s/%s' % (path, theme)):
            for word in get_words('%s/%s/%s' % (path, theme, current_file)):

                # Add 1 to the number of occurences of word in this theme
                if word in frequencies[theme]:
                    frequencies[theme][word] += 1
                else:
                    frequencies[theme][word] = 1

    #Equalize every theme_frequencies dictionary
    check_differences(frequencies)

    #Divide the frequency of each file in each theme by the number of files in that theme
    for theme in frequencies:
        nb_files = len(os.listdir('%s/%s' % (path, theme)))
        for word in frequencies[theme]:
            frequencies[theme][word] /= nb_files

def check_differences(frequencies):
    """ Checks the given frequencies in order to have the same word list in each theme.

    Parameters
    ----------
    frequencies : a dictionary of format { theme (str) : theme_frequencies (dict) }.

    Notes
    -----
    The frequencies dictonary is edited: the theme_frequencies dictionaries may be lenghtened.
    All theme_frequencies dictionaries should be of the same size afterwards.
    Each theme_frequencies dictionary is of format { word (str) : frequency (float) }.

    See also
    --------
    get_frequencies to create the frequencies dictionary.
    """

    checked_words = []
    # For each word
    for theme in frequencies:
        for word in frequencies[theme]:

            #Avoid to check the same word several times
            if not word in checked_words:

                #Check every other theme to see if it countains the word
                for other_theme in frequencies:

                    if other_theme != theme and not word in frequencies[other_theme]:
                        #Add the word
                        frequencies[other_theme][word] = 1

                #add the word to the list so it's not checked anymore
                checked_words.append(word)



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
