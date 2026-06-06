import pandas as pd
from matplotlib import pyplot as plt
data={"Name":["Ravi","Sai","Anu","Kiran","Meena"],"Maths":[85,90,78,92,88],"Science":[80,95,75,89,84],"English":[78,85,82,87,90]}
df=pd.DataFrame(data)
df['Total']=df["Maths"]+df["Science"]+df["English"]
df["Average"]=df["Total"]/3
print(df)
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    else:
        return "C"
df["Grade"]=df["Average"].apply(grade)
top_student=df.loc[df["Total"].idxmax()] 
print(top_student)
plt.bar(df["Name"],df["Total"])
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.title("Student Marks Analysis")
plt.show()