'''<adjective1>
<noun1>
<verb1>
<adjective2>
<noun2>
<adjective3>
<verb2>
<adjective4>
<verb3>
<verb4>'''

with open("story.txt", "r") as f:
    story = f.read()
#after reading the file, need to find the words that have <> 
#then replace the instances with user inputted words
words = set()
start_of_word = -1
target_start = "<"
target_end = ">"
for i, char in enumerate(story):
    #enumerate gives access the story and the position in it
    if char == target_start:
          start_of_word = i 
    if char == target_end and start_of_word != -1:
         #starts at -1 because the first element is 0 
         word = story[start_of_word: i + 1]
         #indicate the starting and ending charater  
         words.add(word)
         #instead of a list, use set so there is only 1 instance of unique elements
         start_of_word = -1
answers = {}
#adding an empty dictionary
#generate answers for them
for word in words:
     answer = input(f"Enter a word for {word}: ")
     answers[word] = answer

for word in words: 
     story = story.replace(word, answers[word])
print(story)



