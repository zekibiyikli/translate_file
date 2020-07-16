import os
import re
from googletrans import Translator
import codecs

file = open("strings.xml", "r") # Source File
baseLanguageCode="en"
resultLanguageCode="tr"
resultPath="values-"+resultLanguageCode
if not os.path.exists(resultPath):
    os.mkdir(resultPath)
resultFile = codecs.open(resultPath+"/string.xml", "w","utf-8") # Result File

translator = Translator()

for f in file:
    if "<string name" in f:
        result = re.search('>(.*)<', f) # Getting String
        a=translator.translate(result.group(1),src=baseLanguageCode, dest=resultLanguageCode) # Translating String
        res=f.replace(result.group(1),a.text)
        if "% 1 $ " in res:
            res=res.replace("% 1 $ "," %1$")
        if "xliff: g" in res:
            res=res.replace("xliff: g","xliff:g")
        resultFile.writelines(res) # Write Text in Result File
    else:
        resultFile.writelines(f)

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