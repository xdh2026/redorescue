#Get the user's email address
email = input("what is your email address?: ").strip()
#slice 
user_name = email[:email.index("@")]
#slice out the domain 
na = email[email.index("@")+1:]

#domain_name
#Format messagedir

res = f"Your username is '{user_name}' and your domain name is '{na}'"
#Display the result mossag
print(res)
