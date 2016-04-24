for link in urls:
	#load page
	try:	
		res = requests.get(link)
	except Exception as error:
		print ("there was an error with the request.get command: %s" %error)
		
	#verify there are no errors
	try:
		res.raise_for_status()
		#get html and look for headlines
		site_content = res.content
		parser = BeautifulSoup(site_content, 'html.parser')
		
		headline_html = (parser.find("h2",{ "class" : "pg-headline" }).text) #get the text
		headline_html = (unicodedata.normalize("NFKD", headline_html)) #decompose caracters (with accents) into two caracters (the good one and the accent)
		headline_html = headline_html.encode("ascii", "ignore") #encode to bytes droping the accents (and all non ascii caracters)
		summary_html = parser.find("p",{ "class" : "pg-summary" }).text
		summary_html = (unicodedata.normalize("NFKD", summary_html)).encode("ascii", "ignore")
		body_html = parser.find("div",{ "class" : "mce-body mce" }).text
		body_html = (unicodedata.normalize("NFKD", body_html)).encode("ascii", "ignore")
		date_html = parser.find_all("small",{ "class" : "timestamp" })[-1].text
		
		#remove puntuation
		headline_aux = headline_html.decode('utf-8').strip().lower()
		summary_aux = summary_html.decode('utf-8').strip().lower()
		body_aux = body_html.decode('utf-8').strip().lower()
		for punc in punctuation:
			headline = headline_aux.replace(punc, "")
			summary = summary_aux.replace(punc, "")
			body = body_aux.replace(punc, "")			

		
		#update lists. No spaces and lowercase.
		headlines.append(headline)
		summaries.append(summary)
		bodies.append(body)
		dates_new.append(date_html)
		counter +=1
		if (counter%50 == 0):
			print (counter)
	except Exception as err:
		print ("There was a problem donwloading the page: %s" %err)
	
#update national dataframe	
nacional["headlines"]= headlines
nacional["summaries"]= summaries
nacional["bodies"]= bodies
nacional["news_date"]= dates_new

nacional.to_csv("C:\\Users\\carrai1\\Desktop\\Projects\\Venezuela\\nacional1.csv",index=False)




