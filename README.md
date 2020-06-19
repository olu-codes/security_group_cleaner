# AWS_Security_Group_Cleaner
Scans your aws account  in a specific region and deletes any unused security groups

Usage 1: Delete Security Group one by one.

C:\python\python.exe C:/Users/boluwase.ANT/PycharmProjects/delete-unused-sgs/main.py
#######WELCOME TO THE SECURITY GROUP CLEANER########
Checking your account for unused security groups....

The unused security groups are: ['sg-0a3719cc094e926de', 'sg-04281a235d28333b1', 'sg-0def263e624602f97', 'sg-0fcda01cb0afd945c', 'sg-0bddfb6afe485c74d', 'sg-00a24950c88234271']
Are you sure you want to delete them?, Enter 'Y' for 'Yes', 'N' for 'No': y
Do you want to delete them one by one or all at a time?, Enter 'Y' for 'one by one', 'N' for 'All': y
Do you want to delete sg-0a3719cc094e926de ? , Enter 'Y' for 'yes', 'N' for 'no', 'X' to 'exit': y
Deleted sg-0a3719cc094e926de
Do you want to delete sg-04281a235d28333b1 ? , Enter 'Y' for 'yes', 'N' for 'no', 'X' to 'exit': y
Deleted sg-04281a235d28333b1
Do you want to delete sg-0def263e624602f97 ? , Enter 'Y' for 'yes', 'N' for 'no', 'X' to 'exit': y
Deleted sg-0def263e624602f97
Do you want to delete sg-0fcda01cb0afd945c ? , Enter 'Y' for 'yes', 'N' for 'no', 'X' to 'exit': x

Process finished with exit code 0



Usage 2: Deletes security groups one at a time.

C:\python\python.exe C:/Users/boluwase.ANT/PycharmProjects/delete-unused-sgs/main.py
#######WELCOME TO THE SECURITY GROUP CLEANER########
Checking your account for unused security groups....

The unused security groups are: ['sg-0fcda01cb0afd945c', 'sg-0bddfb6afe485c74d', 'sg-00a24950c88234271']
Are you sure you want to delete them?, Enter 'Y' for 'Yes', 'N' for 'No': y
Do you want to delete them one by one or all at a time?, Enter 'Y' for 'one by one', 'N' for 'All': n
Deleted sg-0fcda01cb0afd945c
Deleted sg-0bddfb6afe485c74d
Deleted sg-00a24950c88234271

Process finished with exit code 0


Usage 3: No unused security groups found.

C:\python\python.exe C:/Users/boluwase.ANT/PycharmProjects/delete-unused-sgs/main.py
#######WELCOME TO THE SECURITY GROUP CLEANER########
Checking your account for unused security groups....

Hooray, you do not have any unused SGs!

Process finished with exit code 0
.
