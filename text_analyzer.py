# --------- PART A -----------

#STEP 1: DEFINE A STRING

givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

#STEP 2: DEFINE THE CLASS ANS ITS ATTRIBUTES

# class TextAnalyzer(object):
#     def __init__(self, text) -> None:
#         pass

#STEP 3: CODE TO FORMAT THE TEXT IN LOWERCASE
    #Remove punctuation marks (periods, exclamation marks, commas, and question marks)
    #Convert the text argument to lowercases with the lower() method

# class TextAnalyzer(object):

#     def __init__(self, text):
#         formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
#         formattedText = formattedText.lower()
#         self.fmtText = formattedText

#STEP 4: IMPLEMENT CODE TO COUNT THE FREQUENCY OF ALL UNIQUE WORDS
    #Split the fmtText into individual words using the split() method
    #Create an empty dictionary to store the word frequency
    #Iterate over the list of words and update the frequency
    #Use count() method for counting
    #Return the frequency

# class TextAnalyzer(object):

#     def __init__(self, text):
#         # remove punctuation
#         formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
#         # transform text to lowercase
#         formattedText = formattedText.lower()
#         # new variable without punctuation and in lowercase
#         self.fmtText = formattedText

#     def freqAll(self):
#         # split text into words
#         wordList = self.fmtText.split(' ')

#         # create new dictionary
#         freqMap = {}
#         # use set to remove duplicates in list
#         for word in set(wordList):
#             freqMap[word] = wordList.count(word)

#         return freqMap

#STEP 5: IMPLEMENT CODE TO COUNT THE FREQUENCY OF A SPECIFIC WORD

class TextAnalyzer(object):

    def __init__(self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        # transform text to lowercase
        formattedText = formattedText.lower()
        # new variable without punctuation and in lowercase
        self.fmtText = formattedText

    def freqAll(self):
        # split text into words
        wordList = self.fmtText.split(' ')

        # create new dictionary
        freqMap = {}
        # use set to remove duplicates in list
        for word in set(wordList):
            freqMap[word] = wordList.count(word)

        return freqMap

    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0

# --------- PART B -----------

#STEP 1: CREATE AN INSTANCE OF TEXTANALYZER CLASS

analyzed = TextAnalyzer(givenstring)

#STEP 2: CALL THE FUNCTION THAT CONVERTS THE DATA INTO LOWERCASE

print("Formatted Text: ", analyzed.fmtText)

#STEP 3: CALL THE FUNCTION THAT COUNTS THE FREQUENCY OF ALL UNIQUE WORDS FROM THE DATA

freqMap = analyzed.freqAll()
print(freqMap)

#STEP 4: CALL THE FUNCTION THAT COUNTS THE FREQUENCY OF SPECIFIC WORD

word = "lorem"
frequency = analyzed.freqOf(word)
print("The word ", word, "appears", frequency, "times.")



