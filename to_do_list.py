
def print_menu():
    print('\nTo do list menu:')
    print('1. view Tasks')
    print('2. Add a task')
    print('3. remove a Task')
    print('4. Exit')


def get_choice():
    choice=input("enter your choice:")
    valid_choice=('1','2','3','4')
    if choice not in valid_choice:
        print('Invalid choice')
    else:
        return choice
    


def display_tasks(task):
    if not task:
        print('There is no tasks ')
        return
    

    for index, task in enumerate(task, start=1):
        print(f'{index}.{task}')



def add_tasks(task):
    while True:
        tasks= input('enter the task:').strip()
        if len(tasks)!=0:
            task.append(tasks)
            break
        else:
            print('invalid task')    

def remove_task(task):
    display_tasks(task)

    while True:
        try:
            task_number=input('enter the task number you wanyt to remove')
            if 1<= task_number >= len(task):
                task.pop(task_number-1)
                break
            else:
                raise ValueError
        except:
            print('invalid task number')
         

def main():

    task=[]
    while True:
        print_menu()

        choice=get_choice()


        if choice == '1':
            display_tasks(task)
        elif choice =='2':
            add_tasks(task)
        elif choice=='3':
            remove_task(task)
        else:
            break 
      

        
if __name__== '__main__':
    main()
        

    