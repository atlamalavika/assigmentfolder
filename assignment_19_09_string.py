# 1.remove given character from string
word=input("enter_value: ")
new_word=""
for i in word:
    if i=="a":
        new_word+=""
    else:
        new_word=new_word+i
        
print(new_word)


# 2.palindrome or not
palin_word=input("enter_palin: ")
reverse_word=palin_word[::-1]
if palin_word==reverse_word:
    print("It is a polindrome word")
else:
    print("It is not a palindrome word")

# 3.given character is vowel or consonant
given_character=input("enter_char: ")
vowels=["a","e","i","o","u"]
if given_character in vowels:
    print("Given character is vowel")
else:
    print("Given character is consonant")

# 4.replace string space with given character/word
orginal_value=input("enter_orginal_value: ")
replaced_value=orginal_value.replace(" ","india")
print(replaced_value)

# 5.write a rogram to count alphabets,digits,special characters in string
digits=0
alphabets=0
special_characters=0
given_string=input("enter_string: ")
for i in given_string:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        alphabets+=1
    else:
        special_characters+=1

print(digits)
print(alphabets)
print(special_characters)

# 6. Remove all blank spaces in string
word_with_blank=input("enter_value: ")
modified_string=""
for i in word_with_blank:
    if i==" ":
        modified_string+=""
    else:
        modified_string+=i
print(modified_string)

# 7. Find sum of digits in string
string_with_digit=input("string_digit: ")
count=0
for i in string_with_digit:
    if i.isdigit():
        count+=int(i)
print(count)

# 8. Remove repeated char from string
repeated=input("enter_repeated: ")
final_string=""
for i in repeated:
    count=0
    for j in repeated:
        if i==j:
            count=count+1
    if count==1:
        final_string+=i
print(final_string)       

# 9. write a program to count occurance of given character in string
string_with_occurance="malavikayadav"
occurance=input("string_occurance: ")
count=0
for i in string_with_occurance:
    if i==occurance:
        count+=1
print(count)    

# 10. check string is anagrams or not in python
# First method
string1=input("enter_string1: ")
string2=input("enter_string2: ")
if sorted(string1)==sorted(string2):
    print("The strings are anagrams")
else:
    print("strings are not anagrams")


