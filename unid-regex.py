# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(\([a-z]{3,4}.\d{3,4}\))"

test_str = ("Ri Won Ho is a DPRK Ministry of State Security Official stationed in Syria supporting KOMID.',\n"
	" 'Senior member of Islamic State in Iraq and the Levant (ISIL), listed as Al-Qaida in Iraq (QDe.115). Recruited for ISIL and instructed individuals to perpetrate terrorist acts. Physical description: height 176 cm, weight 73 kg, medium built, colour of eyes- brown, colour of hair- black/bald, complexion- brown.  Speaks English.  INTERPOL-UN Security Council Special Notice web link: https://www.interpol.int/en/How-we-work/Notices/View-UN-Notices-Individuals',\n"
	" 'Jo Yong Chol is a DPRK Ministry of State Security Official stationed in Syria supporting KOMID.',\n"
 
	" 'Kim Chol Sam is a representative for Daedong Credit Bank (DCB) who has been',\n"
	" 'Kim Sok Chol acted as the DPRK Ambassador to Burma and he operates as a KOMID facilitator.  He was paid by KOMID for his assistance and arranges meetings on behalf of KOMID, including a meeting between KOMID and Burmese defense related persons to discuss financial matters.',\n"
	" 'Kim Song Chol is a KOMID official that has conducted business in Sudan on behalf of KOMID’s interests.',\n"
	" 'Leader of Al-Nusrah Front for the People of the Levant (QDe.137) for coastal area of Syrian Arab Republic since March 2016. INTERPOL-UN Security Council Special Notice web link: https://www.interpol.int/en/How-we-work/Notices/View-UN-Notices-Individuals',\n"
	" 'A member of Al-Qaida (QDe.004) as of 2012 and a fighter in the Syrian Arab',\n"
	" 'Has \"links to the Institute of Applied Physics, working closely with',\n"
	" 'Key commander in the Haqqani Network (TAe.012) under Sirajuddin',\n"
	" 'Joined Al-Qaida in 1996 and was at that time an important liaison to the',\n"
	" 'Member of Egyptian Islamic Jihad (QDe.003). Review pursuant to Security Council',\n"
	" 'Belongs to Hotak tribe. Review pursuant to Security Council resolution',\n"
	" 'Arrested in Feb. 2010 and in custody in Pakistan. Extradition request to',\n"
	" 'Financial advisor to Taliban Peshawar Military Council and Head of',\n"
	" 'Alternative title: Sar Muallim. Reconciled after the fall of the Taliban',")

matches = re.finditer(regex, test_str, re.MULTILINE | re.IGNORECASE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
