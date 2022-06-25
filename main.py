#main menu code
account=False
tries = 0
while tries<3:
    want=input('what do you want to do? ')
    print(f"confirm that you want to {want} by pressing yes")
    ansss=['yes','no']
    ans=input('yes or no? ')
    tries+=1
    if ans=='yes' and account==False:
        tries += 1
        print('you need to open an account first, confirm that you want to open an account by pressing yes or no ')
        accnt_ans=input('yes or no? ')
        if accnt_ans=='yes':
            menu_try=0
            print('''
1. Name
2. age
3. Job''')

            while menu_try<3 and menu_try>=0:
                menu = input('>')

                if menu == '1':
                    menu_try += 1
                    name = input('what is your name ')
                    names = []
                    names.append(name)
                elif menu == '2':
                    menu_try += 1
                    yr = input('what is your birth year? ')
                    age = 2021 - int(yr)
                    ages = []
                    ages.append(age)
                elif menu == '3':
                    menu_try += 1
                    job = input('what is your occupation? ')
                    jobs = []
                    jobs.append(job)
                else:
                    print('i dont understand')
                if menu_try >= 3:
                    app_no =-1
                    app_no += 1

                    users=[]
                    user={
                        "name": "names[app_no]",
                        "age":"ages[app_no]",
                        "job": "jobs[app_no]",
                        'number':'app_no'
                    }
                    print(f"your account number is {app_no}")
                    users.append(app_no)

                account = True
                if menu_try > 3:
                    print('your application is not complete.')

        elif accnt_ans=='no':
            print('you cant use this program without an account')
            menu_try=0
        else:
            print('i dont understand you')
            menu_try=0

    if ans=='yes' and account==True:
       prof_no=input('what is your account number?')
       tries += 1
       for acct in prof_no:
           if acct==user.get('number'):
               print('this is your profile')
               print(f'''
Your application number is {app_no}
your name is {names[app_no]}
your age is {ages[app_no]}
your job is {jobs[app_no]}''')
           elif acct!=user.get('number'):
               print('Your application number is not registered')
    elif ans=='no':
        print('then get out of here!')
        tries += 1