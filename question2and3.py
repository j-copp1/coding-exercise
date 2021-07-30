#QUESTION 2
#Input is a string word
def abbr(word) :

    #returns (first letter)  + (count of removed letters) + (last letter)
    abbrWord = word[0] + str(len(word) - 2) + word[len(word) - 1]
    
    return abbrWord
    
#QUESTION 3
#Input is a list of string words
def abbrList(words) : 

    results = {}
    uniqueAbbrs = []

    for word in words :
        #run previous method on word from list
        currAbbr = abbr(word)
        #is abbreviation is unique 
        if currAbbr not in uniqueAbbrs :
            uniqueAbbrs.append(currAbbr)
            results.update({word : True})
        #if not unique
        else : 
            results.update({word : False})
    #returns dictionary of results
    return results

#testing functions
testList = ['internationalization', 'localization', 'accessibility', 'automatically']
#q1
print(abbr(testList[0]))
print(abbr(testList[1]))
#q2
print(abbrList(testList))