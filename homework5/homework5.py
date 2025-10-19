'''
1. Git is a distributed version control system that tracks changes to source code; 
GitHub is a web based platform that hots git repositories

2. Terminal is an interface program that provides access to the command line; 
Command Line is a text based interface where users type commands to interact with the operating system

3. Local repository is a Git repository that is stored on your own computer, 
Remote repository is a Git repository hosted on a server

4. Version Control records changes to fils over time

5. Staging Area is an intermediate area in Git where changes are prepared before 
being pushed and saved in a Commit

6. git add is a command that stages changes

7. git commit is a command that permanently saves saged changes to a local repository

8. git push is a command that uploads local commits to a remote repository like Github

9. git status is a command that shows the current state of the working directory and 
staging area; what files are commited, not commit, not staged, etc

10. git pull is a command that download changes from a local repository and merges to the remote 

11. pwd prints the current working directory/where you are

12. ls lists files and directories in your current location

13. cd navigates between directories

14. nano is a text editor that runs in the terminal for creating and modifying files

15. touch creates a new empty file 

16. mv moves or renames files and directories

17. rm removes files and directories

18. cat displays the contents of a file in the terminal


====== 3.2 ======

1. pwd

2. ls

3. cd ../brianna_repo

4. cp ∼/python_decal/brianna_repo/homework.py ∼/python_decal/judy_decal/homework/

5. cd ../judy_decal/homework

6. nano homework.py

7. git status git add git commit -m "<message>"

8. this error means that Judy's local repository is out of sync with the remote repository
on Github. Someone else pushed changes to the remote repository that doesn't exist
in Judy's local copy of the repository. Judy shouldve pulled the latest changes from the remote
repository first before pushing

9. cd ../../../Recent
'''

#4.1 
def checkDataTypes(val):
    return type(val).__name__

# print(checkDataTypes(3.14))    # 'float'
# print(checkDataTypes(True))    # 'bool'

#4.2 
def evenORodd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# print(evenORodd(7))   # 'Odd'
# print(evenORodd(10))  # 'Even'

#5
numbers = [1,2,3,4,5]
def sumWithLoop(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return sum

# print(sumWithLoop(numbers))  # 15

#6.1 
list = ['a', 'b', 'c']
def duplicateList(lst):
    result = []
    for item in lst:
        result.append(item)
        result.append(item)
    return result

# print(duplicateList(list))

#6.2 
def square(num):  # error: add :
    return num * num

# print(square(5))

print(sumWithLoop(numbers))







