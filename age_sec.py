''' get the age of user in years and convert it into seconds'''
def age_seconds():
    age = input("Enter your age in years:")
    seconds = int(age) * 365 * 24 * 3600
    print("You have lived for {} seconds.".format(seconds))
    
age_seconds()