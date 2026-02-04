# from checking_functions import manager_authentication



def menu():
    flag = False
    user=input('please choise, to manager press: 1: to passenger press: 2:')
    while flag== False:
         try:
            if int(user) == 1:
                manager_name=input('please enter your name: ')
                manager_pw=input('please enter your password: ')
                # manager_authentication(manager_name, manager_pw, file_path)
                flag = True
            elif int(user) == 2:
                flag=True
                pass
            else:
                user = input('please choise only 1 or 2, to manager press: 1 to passenger press: 2')
         except:
            print('invaid input')
            user = input('please choise, to manager press: 1 to passenger press: 2')






menu()
