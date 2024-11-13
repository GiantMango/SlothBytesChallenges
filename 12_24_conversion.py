test = ["12:00 am",
        "6:20 pm",
        "21:00",
        "5:05"]

def convertTime(t):
    t = t.lower()  
    suffix = ["am", "a.m.", "pm", "p.m."]
    
    #handle 24 hour
    if t[-2:] in suffix[:2]:
        t = t.split(" ")
        return t[0]
    
    elif t[-2:] in suffix[-2:]:
        t = t.split(" ")
        h, m = t[0].split(":")
        return f"{int(h)+12}:{m}"
    
    #handle 12 hour
    h, m = t.split(":")
    if int(h) > 12:
        return f"{int(h)-12}:{m} pm"
    elif int(h) == 12:
        return f"{int(h)-12}:{m} am"
    else:
        return f"{h}:{m} am"
        
for i in test:
    print(convertTime(i))

    
    