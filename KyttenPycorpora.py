'''
Contains Calls to Specific Corpora
'''

import pycorpora

secret = pycorpora.societies_and_groups["semi_secret"]
#print (secret)
genres = pycorpora.music.genres["genres"]
toxic = pycorpora.science.toxic_chemicals["chemicals"]
antipoem = pycorpora.words.rhymeless_words["words"]
watching = pycorpora.governments.mass_surveillance_project_names["projects"]
GD = pycorpora.mythology.hebrew_god["names"]
fib_num = pycorpora.mathematics.fibonnaciSequence["numbers"]
mood = pycorpora.humans.moods["moods"]
gentrify = pycorpora.geography.sf_neighborhoods["neighborhoods"]
plant = pycorpora.plants.plants["instruments"]
legalize = pycorpora.plants.cannabis["cannabis"]