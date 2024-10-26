# task1.1
#Write a program that searches through reviews list and looks 
# for keywords such as "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.


reviews_list = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
keywords_list = ["good", "excellent", "bad", "poor", "average"]
for review in reviews_list:
    words = review.split()
    updated_review = ""
    for word in words:
        if word.lower() in keywords_list: 
            uppercase = word.upper()
            updated_review += f" {uppercase} "
        
        elif word[:-1] in keywords_list: 
            uppercase = word.upper() 
            updated_review += f" {uppercase} "    
        else:
            updated_review += f" {word} "
    print(updated_review)

# task 1.2
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]   
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
print(len(positive_words + negative_words))



# task 1.3
reviews_list = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]
    
for characters in reviews_list:
    i = 30
    if characters[i] == " ":
        print(characters[:i]+"...")
    else:
        while characters[i] != " ":
            i+=1
        print(characters[:i]+"...")


# task 2

#Write a script that asks for and checks the length of the user's first name and last name.
#  Both should be at least 2 characters long.
#If not, print an error message.

user_name = input("Please enter your first and last name: ").split(" ")
if len(user_name) == 2:
    print("Name:", user_name[0].upper(),",", user_name[1].upper())
else:
    print("Please enter a valid name.")
