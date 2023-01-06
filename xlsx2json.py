import pandas as pd
df=pd.read_excel('papers1.xlsx',dtype=str)
data=df.values
label=list(df)
df['class'][0]
str="["
for i in range(df.shape[0]):
    str+="{"
    print(i)
    for j in range(len(label)-1):
        if j==1 and int(df.values[i][j])<=2018:
            df.values[i][j]='before'
        print(j)
        if pd.isna(df.values[i][j]):
            df.values[i][j]=""
        str+=label[j]+':'+'"'+df.values[i][j]+'"'+','
    j+=1
    if pd.isna(df.values[i][j]):
        df.values[i][j] = ""
    df.values[i][j]=df.values[i][j].replace("\n","<br>")
    str+=label[j]+':'+'"'+df.values[i][j]+'"'+'},'
print(str+']')