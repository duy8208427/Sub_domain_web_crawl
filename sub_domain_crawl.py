import requests
sub_domain_temp = []
sub_domain = []
not_important = []

url = input('Paste the website here: ')
special_word = url.split('=')[1]

def crawling_website():
    global sub_domain_temp
    source_code = requests.get(url)
    plain_text = source_code.text
    for word in plain_text.split():
        if special_word in word :
            not_important.append(word)
    sub_domain_temp = list(dict.fromkeys(not_important))    #remove duplicate
    remove_temp_from_sub()
    
    
def remove_temp_from_sub():
    global sub_domain_temp
    not_important = []
    for word in sub_domain_temp:
        if '*' not in word:
            sub_domain.append(word)
        sub_domain_temp = []    
    remove_extra_thingy()
    
def remove_extra_thingy():
    global sub_domain
    for word in sub_domain:
        if '<TD>' in word:
            sub_domain_temp.append(word[4:-5])
            
    for word in sub_domain_temp:    
        if '<BR>' in word:
            temp = word.split('<BR>')
            #temp = word[(word.find('BR>')+3):-5]
            for t in temp:
                sub_domain_temp.append(t)
        sub_domain = []
    remove_all_BR()

def remove_all_BR():
    global sub_domain_temp
    global sub_domain
    for word in sub_domain_temp:
        if '<BR>' in word:
            sub_domain_temp.pop(sub_domain_temp.index(word))
    for word in sub_domain_temp:
        if '<BR>' in word:
            sub_domain_temp.remove(word)
    sub_domain = list(dict.fromkeys(sub_domain_temp))
    sub_domain_temp = []
            
    #Open and write to a file
    file = open("sub_domain.txt","w")
    for word in sub_domain:
        file.write(word + '\n')
    file.close()
    
crawling_website()
