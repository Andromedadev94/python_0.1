import re  
#re.search is same as findall but findall will return values in list
pattern = 'w[ha]'  #Character classes, this is wh or wa,  "t[a-z]" : this is t followed by one of a,b,c,d,..z . note that it is inside an string!
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))

pattern="t[a-z]"  # regex pattern
quote='Not all those who wander are lost.'
print(re.findall(pattern, quote))

pattern = '[^a-z]t' #The caret, ^, placed at the beginning of the character class, matches all the characters except those specified in the class.
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))

pattern = '.+' #the . means everything and + meand add the together in a single string
quote = 'Not all those who wander are lost.'
print(re.findall(pattern, quote))


pattern = r'\.'  # since . means all, if we want to find . itself, we use \.
quote = 'Not all those who wander are lost.' # and r to means raw string, it will ignore the special meaning of \ and treat it as a normal character
# print(re.findall(pattern, quote))
# \d - digit
# \w - word character
#  \. - literal period
# \s - whitespace

