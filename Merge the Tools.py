list = []
unique_list = []
def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    
    for i in range(0,n):
        if i%k==0:
            list.append(string[i:i+k])
    
    for sub_string in list:
        unique_list.append(''.join(dict.fromkeys(sub_string)))
    
    for x in unique_list:
        print(x)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
