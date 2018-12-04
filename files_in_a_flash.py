"""An implementation of Naive Bayes to sort files by theme."""
import math
import os


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

    #Learning
    print('Learning...')
    frequencies = get_frequencies('%s/sorted' % path)

    #Sorting
    print('Learning done. Sorting...')

    #For each file in unsorted
    file_counter = 1
    nb_files = len(os.listdir('%s/unsorted' % path))
    for current_file in os.listdir('%s/unsorted' % path):

        #Compute the probability that it belongs to each theme
        word_list = get_words('%s/unsorted/%s' % (path, current_file))
        theme_probs = {}
        for theme in frequencies:
            theme_probs[theme] = get_theme_prob(frequencies[theme], word_list)

        #Get the max
        max = list(theme_probs.keys())[0] #Get a theme to begin with
        max_value = theme_probs[max]
        for theme in theme_probs:
            if theme_probs[theme] > max_value:
                max = theme
                max_value = theme_probs[theme]


        #Print result
        print('File %s: %s (%d/%d)' % (current_file, max, file_counter, nb_files))
        file_counter += 1

        #Move the file in the corresponding directory
        os.rename('%s/unsorted/%s' % (path, current_file), '%s/sorted/%s/%s' % (path, max, current_file))


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
    useless_elements = ['\n', '/', '\t', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',',
                        '"', '?', '!', '.', ';', '-', '\'', '(', ')', '@', '>', '<', ':', '*', '}',
                        '{', '[', ']', '$', '^', '~', '#', '&', '%', '+', '_', '=', '€', '£',
                        ' you ', ' they ', ' she ', ' he ', ' it ', ' your ', ' their ', ' we ',
                        ' is ', ' are ', ' have ', ' has ', ' or ', ' and ', ' an ', ' the ',
                        ' of ', ' in ', ' to ', ' if ', ' to ', ' for ', ' them ', ' my ', ' me ',
                        ' its ', ' yours ', ' as ', 'from ', ' by ', ' on ', ' will ', ' not ',
                        ' no ', ' yes ', ' any ', ' be ', ' etc ', ' but ', ' would ', ' been ',
                        ' had ', ' this ', ' off ', ' up ', ' down ', ' right ', ' left ', ' per ',
                        ' year ', ' am ', ' all ', ' his ', ' her ', ' our ', ' their ', ' at ',
                        ' who ', ' can ', ' very ', ' much ', ' know ', ' how ', ' get ', ' just ',
                        ' thanks ', ' where ', ' out ', ' that ', ' with ', ' last ', ' few ',
                        ' so ', ' two ', ' one ', ' three ', ' four ', ' five ', ' six ', ' com ',
                        ' seven ', ' eight ', ' nine ', ' ten ', ' eleven ', ' most ', ' must ',
                        ' some ', ' need ', ' most ', ' january ', ' february ', ' march ',
                        ' april ', ' may ', ' june ', ' july ', ' august ', ' september ', ' why ',
                        ' october ', ' november ', ' december ', ' old ', ' re ', ' subject ',
                        ' tough ', ' best ', ' good ', ' was ', ' what ', ' lot ', ' every ',
                        ' other ', ' while ', ' day ', ' ever ', ' about ', ' said ', ' let ',
                        ' since ', ' also ', ' say ', ' did ', ' here ', ' there ', ' nor ',
                        ' going ', ' fact ', ' us ', ' do ', ' feel ', ' only ', ' thing ',
                        ' which ', ' bit ', ' luck ', ' ll ', ' great ', ' enough ', ' first ',
                        ' between ', ' reply ', ' when ', ' does ', ' such ']

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

    return frequencies


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
    probability: the probability that the file belongs to the given theme. (float)

    See also
    --------
    get_words to get the list of the useful words in a text file.
    get_frequencies and check_frequencies to create the theme_frequencies dictionary.
    """
    probability = 0

    #For each word
    for word in theme_frequencies:

        #Add the log of the probability that this word is/isn't in this theme
        if word in list_words: #is
            probability += math.log(theme_frequencies[word])
        else: #isn't
            probability += math.log(1 - theme_frequencies[word])

    return probability


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
