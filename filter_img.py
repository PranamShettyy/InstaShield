from nudenet import NudeDetector

all_labels = [
    "BELLY_EXPOSED",
    "ARMPITS_EXPOSED",
    "MALE_BREAST_EXPOSED",
    "BUTTOCKS_EXPOSED",
    "FEMALE_BREAST_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED",
    "ANUS_EXPOSED",
    "MALE_GENITALIA_EXPOSED",
    ]

def getval(type):
    with open('a.txt','w') as w:
        w.write(type)   

nude_detector=NudeDetector()

def strict(img_link):
    results=nude_detector.detect(img_link)

    for i in results:
        for j in i:
            if i[j] in all_labels:
                return True
    return False

def moderate(img_link):
    results=nude_detector.detect(img_link)

    for i in results:
        for j in i:
            if i[j] in all_labels[3:]:
                return True
    return False

def is_explict(img_link):
    with open('a.txt','r') as f:
        a=f.read()
    if a=='strict':
        print(a)
        return strict(img_link)
    else:
        #sys.exit(0)
        return moderate(img_link)
