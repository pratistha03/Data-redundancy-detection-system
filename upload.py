<<<<<<< HEAD
import tkinter 
from tkinter import *
from tkinter import filedialog 
# import dask.dataframe as dd
import pandas as pd
import editdistance
import numpy as np


def upload_file():
    file=filedialog.askopenfilename(title="Select file" , filetypes=[("All files", '*.*'),("CSV files", '.csv')])
    # file=filedialog.askopenfilename(title="Select file" , filetypes=[("CSV files", '.csv')])

    if(file):
        lbl_my_file=Label(window, text="File read!", font=("arial", 12, "bold") )
        lbl_my_file.pack()
#     through dask
#         df=dd.read_csv(file)
#         file_name.set(file)
#         # fobj=open(file,'r')
#         file_data.set(df.compute())

# through pandas
        
        
        df=pd.read_csv(file)
        file_name.set(file)
#         print(df)
        df["name"] = df['name'].str.replace(" ", "")
        std_att = df['name'].astype(str) + df['age'].astype(str) + df['age_unit'].astype(str) + df['province_id'].astype(str) + df['district_id'].astype(str) + df['municipality_id'].astype(str) + df['tole'].astype(str) + df['ward'].astype(str) + df['caste'].astype(str) + df['sex'].astype(str)
#         print (std_attribute)
        # df['std_attribute'] = std_att
        # sorted_df = df.sort_values(by=['std_attribute'])
        # print(sorted_df)

        def edit_distance(str1, str2):
            m, n = len(str1), len(str2)
            dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0:
                        dp[i][j] = j
                    elif j == 0:
                        dp[i][j] = i
                    elif str1[i - 1] == str2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

            return dp[m][n]

        def apply_edit_distance(strings):
            n = len(strings)
            distance_matrix = [[0 for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(n):
                    if i != j:
                        distance_matrix[i][j] = edit_distance(strings[i], strings[j])
            return distance_matrix
        def find_duplicates(strings, threshold=3):
            distance_matrix = apply_edit_distance(strings)
            n = len(strings)
            duplicates = []
            for i in range(n):
                for j in range(i+1, n):
                    if distance_matrix[i][j] <= threshold:
                        duplicates.append((i, j, distance_matrix[i][j]))
            duplicates.sort(key=lambda x: x[2])  # sort by edit distance
            return duplicates

        strings = std_att  # Replace ... with the rest of the strings
        duplicates = find_duplicates(strings, threshold=3)
        for i, j, distance in duplicates:
            print(f"{strings[i]} and {strings[j]} are duplicates (edit distance = {distance})")






#         strings = std_att # Replace ... with the rest of the strings
#         distance_matrix = apply_edit_distance(strings)
#         print(distance_matrix)



#         df['std_attribute'] = std_att
#         sorted_df = df.sort_values(by=['std_attribute'])
#         print(sorted_df)
#         distances = np.zeros((len(sorted_df), len(sorted_df)))
#         for i in range(len(sorted_df)):
#             print("hello")
#             for j in range(i+1, len(sorted_df)):
#                 distances[i][j] = levenshtein(sorted_df['std_attribute'].iloc[i], sorted_df['std_attribute'].iloc[j])

#                 distances[j][i] = distances[i][j]

#         print("Distances matrix:")
#         print(distances)
   

        

        
        
    
window=Tk()
window.geometry("400x300")
window.title("Data Redundancy Detection System")
title_lbl=Label(window, text="Upload .csv file", font=("arial", 30, "italic bold"),bd=7)
title_lbl.pack()
button=Button(window, text="Upload File", relief=RAISED,font=("arial", 15, "bold"), width=15, bg="light blue" ,command=upload_file)
button.pack()


file_name=StringVar()
file_data=StringVar()
my_file=StringVar()



lbl_name=Label(window, textvariable=file_name)
lbl_name.pack()



# lbl_data=Label(window, textvariable=file_data, relief=GROOVE)
# lbl_data.pack()


window.mainloop()

# lbl_data.pack(ipadx=10, ipady=10)


=======
import tkinter 
from tkinter import *
from tkinter import filedialog 
# import dask.dataframe as dd
import pandas as pd
import editdistance
import numpy as np

def edit_distance(str1, str2):
            m, n = len(str1), len(str2)
            dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0:
                        dp[i][j] = j
                    elif j == 0:
                        dp[i][j] = i
                    elif str1[i - 1] == str2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

            return dp[m][n]
def apply_edit_distance(strings):
            n = len(strings)
            distance_matrix = [[0 for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(n):
                    if i != j:
                        distance_matrix[i][j] = edit_distance(strings[i], strings[j])
            return distance_matrix

def find_duplicates(strings, threshold=0.05):
            distance_matrix = apply_edit_distance(strings)
            n = len(strings)
            duplicates = []
            for i in range(n):
                for j in range(i+1, n):
                    if distance_matrix[i][j] <= threshold:
                        duplicates.append((i, j, distance_matrix[i][j]))
            duplicates.sort(key=lambda x: x[2])  # sort by edit distance
            return duplicates


def upload_file():
    file=filedialog.askopenfilename(title="Select file" , filetypes=[("All files", '*.*'),("CSV files", '.csv')])
    # file=filedialog.askopenfilename(title="Select file" , filetypes=[("CSV files", '.csv')])

    if(file):
        lbl_my_file=Label(window, text="File read!", font=("arial", 12, "bold") )
        lbl_my_file.pack()
#     through dask
#         df=dd.read_csv(file)
#         file_name.set(file)
#         # fobj=open(file,'r')
#         file_data.set(df.compute())

# through pandas
        
        
        df=pd.read_csv(file)
        file_name.set(file)
#         print(df)
        df["name"] = df['name'].str.replace(" ", "")
        std_att = df['name'].astype(str) + df['age'].astype(str) + df['age_unit'].astype(str) + df['province_id'].astype(str) + df['district_id'].astype(str) + df['municipality_id'].astype(str) + df['tole'].astype(str) + df['ward'].astype(str) + df['caste'].astype(str) + df['sex'].astype(str)
#         print (std_attribute)
        # df['std_attribute'] = std_att
        # sorted_df = df.sort_values(by=['std_attribute'])
        # print(sorted_df)

        strings = std_att  # Replace ... with the rest of the strings
        duplicates = find_duplicates(strings, threshold=3)
        for i, j, distance in duplicates:
            print(f"{strings[i]} and {strings[j]} are duplicates (edit distance = {distance})")



####### divide into chunks##########
        print("Number of lines present:-", len(df))

        def iterate_on_total_rows(filename):
            # Load dataset

            # Get total number of rows
            total_rows = len(df)

            # Define the condition
            condition_met = False
            chunk_size = 100
            num_rows_processed = 0

            # Iterate over the data in chunks of 100 rows at a time until the condition is met
            while not condition_met:
                # Process the next chunk
                chunk = df.iloc[num_rows_processed : num_rows_processed + chunk_size]
                num_rows_processed += len(chunk)

                # Check the condition
                # For example, stop after processing the first 500 rows
                if num_rows_processed >= total_rows:
                    condition_met = True

                # Do something with the processed data
                # For example, print the first 5 rows in each chunk
                print(chunk.head(5))



#         strings = std_att # Replace ... with the rest of the strings
#         distance_matrix = apply_edit_distance(strings)
#         print(distance_matrix)



#         df['std_attribute'] = std_att
#         sorted_df = df.sort_values(by=['std_attribute'])
#         print(sorted_df)
#         distances = np.zeros((len(sorted_df), len(sorted_df)))
#         for i in range(len(sorted_df)):
#             print("hello")
#             for j in range(i+1, len(sorted_df)):
#                 distances[i][j] = levenshtein(sorted_df['std_attribute'].iloc[i], sorted_df['std_attribute'].iloc[j])

#                 distances[j][i] = distances[i][j]

#         print("Distances matrix:")
#         print(distances)
   

        

        
        
    
window=Tk()
window.geometry("400x300")
window.title("Data Redundancy Detection System")
title_lbl=Label(window, text="Upload .csv file", font=("arial", 30, "italic bold"),bd=7)
title_lbl.pack()
button=Button(window, text="Upload File", relief=RAISED,font=("arial", 15, "bold"), width=15, bg="light blue" ,command=upload_file)
button.pack()


file_name=StringVar()
file_data=StringVar()
my_file=StringVar()



lbl_name=Label(window, textvariable=file_name)
lbl_name.pack()



# lbl_data=Label(window, textvariable=file_data, relief=GROOVE)
# lbl_data.pack()


window.mainloop()

# lbl_data.pack(ipadx=10, ipady=10)


>>>>>>> 98b31f0 (divide into 100 chunk and iterate)
