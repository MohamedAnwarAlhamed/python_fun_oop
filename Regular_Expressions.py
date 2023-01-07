# ----------------------------------
# -- Regular Expressions => Intro --
# ----------------------------------
# [1] Sequence of Characters That Define A Search Pattern
# [2] Regular Expression is Not In Python Its General Concept
# [3] Used In [Credit Card Validation, IP Address Validation, Email Validation]
# [4] Test RegEx "https://pythex.org/"
# [5] Characters Sheet "https://www.debuggex.com/cheatsheet/regex/python"
# -----------------------------------------------------------

# ----------------------------------------
# -- Regular Expressions => Quantifiers --
# ----------------------------------------
# *	0 or more
# +	1 or more
# ?	0 or 1
# {2}	Exactly 2
# {2, 5}	Between 2 and 5
# {2,}	2 or more
# (,5}	Up to 5
# https://regex101.com/
# -------------

# -----------------------------------------------------------------------
# -- Regular Expressions => Characters Classes Training's --
# -----------------------------------------------------------------------
# [0-9]
# [^0-9]
# [A-Z]
# [^A-Z]
# [a-z]
# [^a-z]
# -------------


# ---------------------------------------
# -- Regular Expressions => Assertions --
# ---------------------------------------
# ^	  Start of String
# $	  End of string
# -------------------------
# Match Email
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$

# ----------------------------------------------------
# -- Regular Expressions => Logical Or And Escaping --
# ----------------------------------------------------
# |	  Or
# \	  Escape Special Characters
# ()  Separate Groups
# -----------------------------

# (\d-|\d\)|\d>) (\w+)
# (\d{3}) (\d{4}) (\d{3}|\(\d{3}\))
# ^(https?://)(www\.)?(\w+)\.(net|org|com|info|me)$



# ---------------------------------------------------------
# -- Regular Expressions => Re Module Search And FindAll --
# ---------------------------------------------------------
# search()  => Search A String For A Match And Return A First Match Only
# findall() => Returns A List Of All Matches and Empty List if No Match
# ---------------------------------------------------------------------
# Email Pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------

import re

my_search = re.search(r"[A-Z]{2}", "OOsamaEElzero")

print(my_search)
print(my_search.span())
print(my_search.string)
print(my_search.group())

is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", "os@osama.com")

if is_email:

  print("This is A Valid Email")

  print(is_email.span())
  print(is_email.string)
  print(is_email.group())

else:

  print("This is Not A Valid Email")

email_input = input("Please Write Your Email: ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

empty_list = []

if search != []:

  empty_list.append(search)

  print("Email Added")

else:

  print("Invalid Email")

for email in empty_list:

  print(email)