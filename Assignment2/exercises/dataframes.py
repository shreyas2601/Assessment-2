import pandas as pd

data={
    'student':['kumar','muruli','kiran','rahul','maddy'],
    'marks':[90,76,81,65,98]
}

df=pd.DataFrame(data)

high_score=df[df['marks']>80]

print("student who score more than 80")
print(high_score)