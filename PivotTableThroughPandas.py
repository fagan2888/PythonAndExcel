import pandas as pd
import os
from openpyxl import load_workbook
import xlsxwriter
from shutil import copyfile
import numpy as np

# file = input("File Path: ")
file = r"C:\\Users\\sjtal\Documents\\PythonAndExcel\\TestFileSplit.xlsx"

extension = os.path.splitext(file)[1]
filename = os.path.splitext(file)[0]
pth = os.path.dirname(file)

# load the file into a data frame
df = pd.read_excel(file, sheet_name="FirstSet")
df_sec = pd.read_excel(file, sheet_name="SecondSet")
one_frame = [df, df_sec]
df = pd.concat(one_frame, axis=0)
df.fillna(0, inplace=True)


pivot_df = df.pivot_table(index=["Colors"], aggfunc=np.sum)
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month

df.sort_values(["Colors"])
print(df.head(50))
pivot_df = df.pivot_table(
    index=["Colors", "Year", "Month"], aggfunc=np.sum, margins=True
)

pivot_df["Diff"] = pivot_df["Removed"] - pivot_df["Added"]
pivot_df.style.apply("background: red")


pivot_df.style.apply(
    lambda x: ["background: red" if v < 0 else "" for v in pivot_df["Diff"]], axis=1
)

print(pivot_df)


def storePivot(print_pivot_df):

    print(file)
    # https://github.com/PyCQA/pylint/issues/3060 pylint: disable=abstract-class-instantiated

    with pd.ExcelWriter(file, engine="openpyxl", mode="a") as writer:
        print_pivot_df.to_excel(writer, sheet_name="PivotSheet", index=True)
        writer.save()
    return


storePivot(pivot_df)
