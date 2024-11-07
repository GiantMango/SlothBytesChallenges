test = [
    "the egg and Ctrl + C Ctrl + V the spoon",
    "WARNING Ctrl + V Ctrl + C Ctrl + V",
    "The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V",
    "Save on Ctrl + C food Ctrl + C is here Ctrl + V",
    "Ctrl + V Fairway Ctrl + C",
    "track Ctrl + C Ctrl + V Ctrl + V",
    "Ctrl + C",
    "Ctrl + V"
]

    
def keyboardShortcut(text):
    copy = "Ctrl + C"
    paste = "Ctrl + V"
    
    firstPaste = text.find(paste)
    firstCopy = text.find(copy)
    copiedText = ""
    
    # Delete useless ctrl + v
    while(firstPaste < firstCopy and firstPaste > -1):
        if firstPaste == 0:
            text = text[firstPaste+len(paste):]
        else:
            text = text[:firstPaste-1] + text[firstPaste+len(paste):]
        firstPaste = text.find(paste)
        firstCopy = text.find(copy)
    
    # Repeat until no more Ctrl + C and Ctrl + V
    while(firstCopy > -1 or firstPaste > -1):
        if firstCopy < firstPaste and firstCopy > -1:
            text = text[:firstCopy] + text[firstCopy+len(copy):]
            copiedText = text[:firstCopy]
        
        elif firstPaste < firstCopy and firstPaste > -1:
            text = text[:firstPaste] + copiedText + text[firstPaste+len(paste):]
            
        elif firstCopy == -1:
            text = text[:firstPaste] + copiedText + text[firstPaste+len(paste):]
            
        else:
            text = text[:firstCopy] + text[firstCopy+len(copy):]
            copiedText = text[:firstCopy]
        
        firstPaste = text.find(paste)
        firstCopy = text.find(copy)
            
    return text.replace("  ", " ").strip()