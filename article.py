from newspaper import Article
from string import Template
from ntlk import *
url = "https://timesofindia.indiatimes.com/business/india-business/im-being-ignored-after-i-returned-from-long-leave/articleshow/73164812.cms"
toi_article = Article(url, language="en") # en for English 
toi_article.download()  
toi_article.parse()
toi_article.nlp()
title=toi_article.title
text=toi_article.text
hs = open("art.html", 'w')
message='''\
<html>
<head><title></title></head>
<body><h2>$title</h2>
<p>$text</p>
</body>
</html>
'''
x=Template(message).safe_substitute(title=toi_article.title)
y=Template(message).safe_substitute(text=toi_article.text)
hs.write(x)
hs.write(y)
hs.close()
