import nltk
import operator
nltk.download('words')

eng_words = nltk.corpus.words.words()

letters_dich = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8 , 'I':9 , 'J':10 , 'K': 11 , 'L': 12 , 
'M': 13 , 'N': 14 , 'O': 15 , 'P': 16 , 'Q': 17 , 'R': 18 , 'S': 19 , 'T': 20 , 'U': 21 ,
'V': 22 , 'W': 23 , 'X': 24 , 'Y':25 , 'Z' : 26

}
dich_items = letters_dich.items()

def encrypt(sen , k):
    if k > 26:
        k= k-26
    
    sen = sen.upper()
    result_string = ''
    for i in sen:
        if i in letters_dich:
            result = (letters_dich[i]+k)%26
            for item in dich_items:
                if item[1]==result:
                    result_string+= item[0]
                    break
                if item[1]==26 and result == 0:
                    result_string+= item[0]
                    break
        else:
            result_string+= i

    return result_string 
       

def decrypt(sen, k):
    if k > 26:
        k= k-26
    
    sen = sen.upper()
    result_string = ''
    for i in sen:
        if i in letters_dich:
            result = (letters_dich[i]-k)%26
            for item in dich_items:
                if item[1]==result:
                    result_string+= item[0]
                    break
                if item[1]==26 and result == 0:
                    result_string+= item[0]
                    break
        else:
            result_string+= i

    return result_string 



def hacker(sen):
    iteration = 1
    result_count ={}
    for i in range(26):
        count = 0 
        expext = decrypt(sen,iteration)
        expext_list = expext.split()
        
        for word in expext_list:
            if word in eng_words or word.upper() in eng_words or word.lower() in eng_words:
                count+=1
        result_count[f'{iteration}'] = count
        iteration+=1
    k= int(max(result_count.items(), key=operator.itemgetter(1))[0])
    return decrypt(sen,k)
    



print(encrypt('15 kilogramez',27))
print(decrypt(encrypt('15 kilogramez',27),27))
print(hacker(encrypt('15 kilogram Hello word fksgg',1)))