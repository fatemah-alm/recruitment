from ast import And
from operator import index


def get_skills():
    # Add at least 3 random skills for the user to select from
    return ['dancing', 'playing the piano','back flipping']


def show_skills(skills):
    # Pretty print skills to the user
    # Write your code here
    print("skills: ")
    for count, value in enumerate(skills, start=1):
     print(count, value)

def get_user_skills(skills):
    # Show the available skills and have user pick from them
    # Write your code here
    show_skills(skills)
    skill1 = int(input('Choose a skill from above by entering its number: '))
    skill2 = int(input('Choose another skill from above by entering its number: '))
    user_skills = [skills[skill1 -1], skills[skill2 -1]]

    return user_skills

    ...


def get_user_cv(skills):
    # Get the users CV from their inputs
    # Write your code here

    cv = {}
    cv["name"]= input('What\'s your name? ')
    cv["age"]= int(input('How old are you? '))
    cv["experience"] = int(input('How many years of experience do you have? '))
    cv["skills"] = get_user_skills(skills)
    return cv
    ...


def check_acceptance(cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    if(cv["age"] >= 25 and cv["age"] <= 40) and (cv["experience"] > 3) and (desired_skill in cv["skills"]):
       return True
   
           
    


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print('Welcome to the special recruitment program, please answer the following questions:')

    skills = get_skills()
    cv = get_user_cv(skills)
    # check_acceptance(cv, skills[2])
    # print(check_acceptance(cv, skills[2]))
    if(check_acceptance(cv, skills[2])):
        print('You have been accepted, ' + cv["name"])
    else:
        print('You have been rejected, ' + cv["name"])


#new commment
if __name__ == "__main__":
    main()
