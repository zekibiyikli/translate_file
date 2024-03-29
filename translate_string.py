import os
import re
from googletrans import Translator
import codecs

file = open("strings.xml", "r") # Source File
baseLanguageCode="en"
resultLanguageCode="fr"
resultPath="values-"+resultLanguageCode
if not os.path.exists(resultPath):
    os.mkdir(resultPath)
resultFile = codecs.open(resultPath+"/strings.xml", "w","utf-8") # Result File

translator = Translator()

print("......... TRANSLATING .........")

for f in file:
    if "<string name" in f and "translatable" not in f and "<![CDATA" not in f:
        result = re.search('>(.*)</string>', f) # Getting String
        baseword=result.group(1)
        a=translator.translate(baseword,src=baseLanguageCode, dest=resultLanguageCode) # Translating String
        res=f.replace(baseword,a.text)
        if "% 1 $ " in res:
            res=res.replace("% 1 $ "," %1$")
        if "% 2 $ " in res:
            res=res.replace("% 2 $ "," %2$")
        if "xliff: g" in res:
            res=res.replace("xliff: g","xliff:g")
        resultFile.writelines(res) # Write Text in Result File
    elif "<![CDATA" in f:
        sub1 = "CDATA["
        sub2 = "]]"
        # getting index of substrings
        idx1 = f.index(sub1)-1
        idx2 = f.index(sub2)
        res = ''
        # getting elements in between
        for idx in range(idx1 + len(sub1) + 1, idx2):
            res = res + f[idx]
        baseword=res
        a=translator.translate(baseword,src=baseLanguageCode, dest=resultLanguageCode) # Translating String
        res=f.replace(baseword,a.text)
        if "% 1 $ " in res:
            res=res.replace("% 1 $ "," %1$")
        if "% 2 $ " in res:
            res=res.replace("% 2 $ "," %2$")
        if "xliff: g" in res:
            res=res.replace("xliff: g","xliff:g")
        resultFile.writelines(res) # Write Text in Result File

    else:
        resultFile.writelines(f)

print("TRANSLATE IS DONE")

"""
Afrikaans => af
Irish => ga
Albanian => sq
Italian => it
Arabic => ar
Japanese => ja
Azerbaijani => az
Kannada => kn
Basque => eu
Korean => ko
Bengali => bn
Latin => la
Belarusian => be
Latvian => lv
Bulgarian => bg
Lithuanian => lt
Catalan => ca
Macedonian => mk
Chinese Simplified => zh-CN
Malay => ms
Chinese Traditional => zh-TW
Maltese => mt
Croatian => hr
Norwegian => no
Czech => cs
Persian => fa
Danish => da
Polish => pl
Dutch => nl
Portuguese => pt
English => en
Romanian => ro
Esperanto => eo
Russian => ru
Estonian => et
Serbian => sr
Filipino => tl
Slovak => sk
Finnish => fi
Slovenian => sl
French => fr
Spanish => es
Galician => gl
Swahili => sw
Georgian => ka
Swedish => sv
German => de
Tamil => ta
Greek => el
Telugu => te
Gujarati => gu
Thai => th
Haitian Creole => ht
Turkish => tr
Hebrew => iw
Ukrainian => uk
Hindi => hi
Urdu => ur
Hungarian => hu
Vietnamese => vi
Icelandic => is
Welsh => cy
Indonesian => id
Yiddish => yi
"""
