result = []
def dfs(index,path,text,dic):
    if len(text) == len(path):
        result.append(path)
        return
    
    for i in range(index,len(text)):
        for j in dic[text[i]]:
            dfs(i+1,path+j,text,dic)

def main():
    text = input()
    dic = {"2":"abc","3":"def","4":"ghi","5":"jkl",
                "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

    dfs(0,"",text,dic)
    print(result)
if __name__ == "__main__":
    main()