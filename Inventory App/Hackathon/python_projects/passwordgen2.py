import random  # Random module is used to perform the random generations of numbers, letters, and symbols. random.sample() function does not repeat characters, making for a more secure password. 
import string  

# String module contails a number of useful constants, classes, and a number of fucntiosns to process the standard python string such as:

# Here are some of the functions of the string module:
# 1. string.ascii_letters: This function will concatentate the upper and lower case letters 
# 2. string.ascii_lowercase: All lower case letters 
# 3. string.ascii_uppercase: All uppercase letters 
# 4. string.digits: The string '0123456789'
# 5. string.punctuation: String of the ASCII characters which are considered punctuation characters in the C locale 

# First step is to import the random and string modules, which we have already done. Then we will greet the user.
print("Hello, Welcome to the Password Generator")

# input the length of the password, here we are asking the user for the length of the password 
password_len = int(input('\n Enter in the length of password'))

# Now it's time to define the data, here we will make use of the string module
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
num_digits = string.digits
symbols_punc = string.punctuation

# Now we have stored the lowercase, uppercase, numbers, and symbols, we can now combine the data
character = lower_case + upper_case + num_digits + symbols_punc

# Because we have all of the data stored and combined, we can now use the random module to generate the password 

randomize = random.sample(character, password_len) # This will randomize all of the characters from each of the data types 
password = ''.join(randomize) # join() method takes all items in an iterable and joins them into one string. A str must be specified as the separator. This will then combine all of the randomized characters in order to create the password.

# We are passing in the combined data along with the length of the password, and joining them at the end. Now that you have a clear understanding of the script, we can even reduce the number of lines of code by eliminating the storage of data. Let’s have a look.
# all = string.ascii_letters + string.digits + string.punctuation
# pass1 = "".join(random.sample(all, password_len))

print(password)