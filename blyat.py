from datetime import datetime as dt

today = dt.today()

sentence = input("Write a sentence you would like to save on a file:\n")

print("Sentence size: {0}".format(len(sentence)))

filename = str(input("How would you like your file to be named?\n"))

with open(filename +".txt", 'w') as f:
    f.write("Last modified = "+str(today)+"\nAuthor = Wraith\n")
    f.writelines(sentence)
    f.close()
    print("Succesfully added the sentence to file!\n")

# input("Press ENTER to quit\n")