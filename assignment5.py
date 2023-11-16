#Follow all the Python conventions for a variable name. It must start with a lowercase letter and only contain letters, numbers, and underscores.Not be in a list of taken usernames. taken_usernames = ['admin','admin123', 'root']● If the username doesn’t meet these requirements, print either “Invalidusername” or “Username taken” based on the context, and continue
# Need to add len() for username requiments, maybe  /.append() to username & password


user_name =input("Please Enter User Name: ").lower # Create user input for User Name/.lower might not be needed here but later down in the code
user_password = input("Please Enter Password: ") # Create user input Password
while True:

    if user_name =='stop':
        break







#while True: # we will utilize breaks and continue to control our loop
#     user_input = input("What type of pet do you have? ").lower() # prompting user, adding lower
#     # for uniform data and our stop test
#
#     if user_input == 'stop': # if user types stop, we are all done
#         break
#     elif user_input not in pets: # lets add our pet to our list and give feedback
#         pets.append(user_input)
#         print(f'We have just added {user_input} to our pet list')
#         print(pets)
#     elif user_input in pets:
#         print(f'{user_input} is already in our pets list')
#         print(pets)
#         continue

#for d in remove_dupes:
 #   if d == 2:
  #       remove_dupes.remove(2)
#print(remove_dupes)

#for c in remove_dupes:
#    if remove_dupes.count(2) > 1:
 #       remove_dupes.remove(2)
  #      print(remove_dupes)