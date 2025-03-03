import random
def coding_message(sentence):
    final_message_list=[]
    for word in sentence:
        c=0
        final_message=""
        temp_mesage=""
        for char in (word):
            c=c+1
        if(c>=3):
            l=len(word)
            for i,new_word in enumerate(word):
                if(i>=1):
                    temp_mesage=temp_mesage+new_word
                else: temp_mesage=""
            #print(temp_mesage)
            temp_mesage=temp_mesage+word[0]
            random_start=""
            random_end=""
            for i in range(0,3):
                random_integers=random.randint(97,122)
                random_char=(chr)(random_integers)
                random_start=random_start+random_char
            for i in range(0,3):
                random_integers=random.randint(97,122)
                random_char=(chr)(random_integers)
                random_end=random_end+random_char
            final_message=random_start+temp_mesage+random_end
            #print(final_message)
            final_message_list.append(final_message)     
        else:
            leng=len(word)
            if(leng==2):
                final_message=word[1]+word[0]
            else:
                final_message=word
            #print(final_message)
            final_message_list.append(final_message)
    return(final_message_list)
def decoding_message(sentence):
    final_message=""
    final_decoded_message=[]
    for word in sentence:
        c=0
        for char in word:
            c=c+1
        if(c<3):
            l=len(word)
            if(l==2):
                final_message=word[1]+word[0]
            else:
                final_message=word
            final_decoded_message.append(final_message)
        else:
            l=len(word)
            temp_message=word[3:l-3]
            #print(temp_message)
            newl=len(temp_message)
            near_final_message=""
            near_final_message=near_final_message+temp_message[newl-1]
            #print(near_final_message)
            for x,w in enumerate(temp_message):
                if(x<newl-1):
                    near_final_message=near_final_message+w
            #print(near_final_message)  
            final_decoded_message.append(near_final_message)
    return(final_decoded_message)
user_message=input("Enter your Message : ")
word_list=(user_message.split(" "))
final_list=coding_message(word_list)
#print(final_list)
coded_message=""
for word in final_list:
    coded_message=coded_message+word+" "
print(coded_message)
print("\nNow Let's decode our message - ")
word_list2=coded_message.split(" ")
final_list2=decoding_message(word_list2)
decoded_message=""
for word in final_list2:
    decoded_message=decoded_message+word+" "
print(decoded_message)