import urllib
import mechanize


def translateString(home_language,target_language,text):
	text = text.replace(" ","%20")
	get_url = "http://translate.google.com/translate_a/t?client=t&sl="+home_language+"&tl="+target_language+"&hl="+home_language+"&sc=2&ie=UTF-8&oe=UTF-8&prev=btn&ssel=3&tsel=0&q="+text
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('User-agent','Chrome')]
	translate_text = browser.open(get_url).read().decode("UTF-8")
	translate_text = translate_text.split("]]")
	translate_text = translate_text[0].replace("[[[","").replace('"','').split(",")
	return translate_text[0]


def get_spinner(text):
	return translateString ("ar", "en",translateString("en","ar",text).encode("UTF-8"))




def post_request (home_language, target_language, text):
	post_url = "http://translate.google.com/translate_a/t"
	parameters = {
		'client':'t',
		'text':text,
		'sl':home_language,
		'tl':target_language,
		'hl':home_language,
		'ie':'UTF-8',
		'oe':'UTF-8',
		'pc':'1',
		'oc':'1',
		'otf':'1',
		'ssel':'0',
		'tsel':'0',
		}
	try: 
		data = urllib.urlencode(parameters)
	except:
		print "error encoding params"

	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.addheaders = [('User-agent','Chrome')]
	translate_text = browser.open(post_url, data).read()
	response = translate_text

	translate_array = response.replace("[[","").replace("[","$").replace("]","$$").split("$")

	trans_string = ""
	for block in translate_array:
		trans_string += block.split('","')[0]

	return trans_string

def post_spinner(home_language, target_language, text):
	return post_request (target_language, home_language, post_request(home_language,target_language,text))


print post_spinner ("en","ar", 'KABUL, Afghanistan - Months of fraught negotiations and public posturing over how a long-term American military force could remain in Afghanistan have suddenly come down to a demand for a single personal gesture: a display of contrition by President Obama for military mistakes that have hurt Afghans. Afghan officials said Tuesday that in return for such a letter from Mr. Obama, President Hamid Karzai would end his vehement opposition to American counterterrorism raids on private Afghan homes - one of the most contentious issues between allies over a costly dozen-year war - clearing the way for an agreement to keep a smaller American troop force in the country past the 2014 withdrawal deadline. As described by Mr. Karzai\'s spokesman, Aimal Faizi, the letter would be tantamount to an apology, though he did not use that word. But not even that would be enough to ensure the final passage of a security agreement the United States had pressed to have in hand before next year. The Afghans have made final approval subject to an Afghan grand council of elders, a loya jirga, that is to begin meeting on Thursday, and aspects of the security deal remain deeply unpopular with the public. The White House spokesman, Jay Carney, would not confirm details on Tuesday, but he nodded to the potential deal-breaking potential of the meeting. "There are ongoing negotiations," he said. "I would simply say this agreement is not reached until it goes through the loya jirga." The 11th-hour discussions were the latest lurch in a start-and-stop negotiation process that has exposed raw feelings between allies, and has also highlighted Mr. Karzai\'s taste for public brinkmanship. Just two days ago, Afghan officials said that the raid issue had created a stubborn impasse. Afghan and American officials said that the potential for breakthrough was opened by a phone call from Secretary of State John Kerry to Mr. Karzai on Tuesday. According to Mr. Faizi, Mr. Kerry offered to write a letter assuring the importance of an agreement and acknowledging American mistakes, and Mr. Karzai issued a counteroffer: he would compromise if the letter was from Mr. Obama instead. Mr. Faizi said Mr. Kerry agreed to those terms. But Susan E. Rice, the national security adviser, flatly denied in an interview with CNN on Tuesday night that there would be any presidential apology. "No such letter has been drafted or delivered," Ms. Rice said. "There is not a need for the United States to apologize to Afghanistan. Quite the contrary. We have sacrificed and supported them in their democratic progress and in tackling the insurgency and Al Qaeda." A senior State Department official, speaking on condition of anonymity to discuss continuing negotiations, was more noncommittal, saying that a letter acknowledging past issues like civilian casualties was a possibility being weighed. "We will consider his request for reassurances, including the option of a letter from the administration stating our position," the official said. Under the Afghan description, in return for the letter, Mr. Karzai would then accept wording that allowed American Special Operations raids to search and detain militants within Afghan homes, but only under "extraordinary circumstances" to save the lives of American soldiers. That would seem to greatly hamper the American intent behind those operations, which commanders have said are critical to taking the fight directly to Al Qaeda and other terrorist groups. Among members of the Afghan public, though, foreign raids on private homes are seen as deeply offensive, and the prospect of continued American commando operations after 2014 is unlikely to receive a warm reception from the roughly 3,000 delegates to the loya jirga. But Mr. Faizi said that a letter from Mr. Obama would help win critics over. And Afghan political observers have noted that Mr. Karzai, who despite his harsh negotiation tactics has repeatedly mentioned the importance of a lasting security deal with the United States, had the power of approval over the delegate list, making it more likely he could sway the council. Mr. Faizi made it clear that the Afghans had a very detailed understanding of what they expected a letter from Mr. Obama to say, and without that there would be no deal. The letter would clarify what was meant by "extraordinary circumstances" justifying home raids, and go beyond that as well. "The idea was to indeed mention that there were mistakes made in the conduct of military operations in the past, in the conduct of military operations by United States forces in the last decade, and that Afghans have suffered, and that we understand the pain and therefore we give assurances and make sure those mistakes are not repeated," Mr. Faizi said. Afghan officials said they expected to see the text of the letter by Wednesday before Mr. Karzai signs off on the security agreement. With one day remaining to finalize the wording of the security agreement before the loya jirga meets, Mr. Faizi said that was the remaining issue in talks, carried out in their last phase by Mr. Karzai with the American ambassador, James B. Cunningham, and the American military commander, Gen. Joseph F. Dunford Jr. "The rest, everything is solved," Mr. Faizi said. He also said that the Afghan side had agreed to acquiesce on another sticking point: the American requirement that the United States retain legal jurisdiction over its soldiers in Afghanistan. In essence, that would make United States military personnel immune to Afghan prosecution for their actions in the country, though they would remain subject to American prosecution. A similar requirement led to the collapse of talks with Iraq to establish a long-term security deal, and an immediate final withdrawal of American troops from that country in 2011. In recent weeks, American officials have mentioned that the result in Iraq could be duplicated, and that the 2014 military withdrawal from Afghanistan could be made complete and final if their terms on home raids and legal jurisdiction were not met.')

# https://www.youtube.com/watch?v=uLx-lAqHEZc
# PPost Request With Python Signature Series Tutorial Part 2
