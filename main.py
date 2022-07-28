from tkinter import *
from PyDictionary import PyDictionary
root=Tk()
root.geometry('350x300')
def Translate():
    word = entry.get()
    dictionary = PyDictionary(word)
    trans = dictionary.translateTo("ro")
    print(trans)


def Antonyms():
    word = entry.get()
    dictionary = PyDictionary(word)
    antonym = dictionary.printAntonyms()
    print(antonym)


def Synonyms():
    word=entry.get()
    dictionary=PyDictionary(word)
    synonym=dictionary.printSynonyms()
    print(synonym)

def Meaning():
    word=entry.get()
    dictionary=PyDictionary(word)
    meanings=dictionary.printMeanings()
    print(meanings)


entry=Entry(root,font=("times",15,"bold"))
entry.grid(row=2,column=2)
btn=Button(root,text="Synonyms",command=Synonyms)
btno=Button(root,text="Antonyms",command=Antonyms)
btna=Button(root,text="Translate",command=Translate)
btnd=Button(root,text="Meanings",command=Meaning)
btno.grid(row=4,column=1)
btna.grid(row=4,column=3)
btn.grid(row=4,column=2)
btnd.grid(row=4,column=4)
root.mainloop()