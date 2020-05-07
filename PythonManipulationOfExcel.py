import pandas as pd
import os
from openpyxl import load_workbook
import xlsxwriter
from shutil import copyfile
import numpy as np

file = input("File Path: ")
extension = os.path.splitext(file)[1]
filename = os.path.splitext(file)[0]
pth = os.path.dirname(file)

# Create a file with suffix 2 which will contain modified data
newfile = os.path.join(pth, filename + "_2" + extension)

# load the file into a data frame
df = pd.read_excel(file, sheet_name="FirstSet")
df_sec = pd.read_excel(file, sheet_name="SecondSet")
one_frame = [df, df_sec]
all_data_df = pd.concat(one_frame, axis=0)
all_data_df = all_data_df.fillna(0)

# print(all_data_df.head(5))
all_data_df["Date_Year"] = all_data_df["Date"].dt.year
all_data_df["Date_Month"] = all_data_df["Date"].dt.month

one_pivot = all_data_df.groupby(["Colors", "Date_Year", "Date_Month"]).sum()

# print(one_pivot.columns)
# print(one_pivot)


def createSubtotals(pivot_df):
    second_pivot = pd.pivot_table(
        pivot_df,
        index=["Colors"],
        aggfunc=np.sum,
        values=["Added", "Removed"],
        margins=True,
    )
    print(second_pivot)


createSubtotals(one_pivot)


def storePivot(pivot_df):

    pivot_df = pivot_df.reset_index()
    pivot_df.set_index(["Colors", "Date_Year", "Date_Month"], inplace=True)

    print(pivot_df)
    print(file)
    # https://github.com/PyCQA/pylint/issues/3060 pylint: disable=abstract-class-instantiated

    with pd.ExcelWriter(file, engine="openpyxl", mode="a") as writer:
        pivot_df.to_excel(writer, sheet_name="PivotSheet", index=True)
        writer.save()
    return


# storePivot(one_pivot)
