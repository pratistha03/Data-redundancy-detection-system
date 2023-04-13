from tkinter import *
from tkinter import filedialog 
import pandas as pd



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


def dcs(duplicate_list):
    # defining the window size
    w = 10

    # read the data from a file or other source
    data = duplicate_list  

    # initialize the window
    window_start = 0
    window_end = w
    window_data = data[window_start:window_end]

    # initialize the list of duplicates
    duplicates = []

    # loop through the data
    while window_end <= len(data):
        # compare all pairs of records within the window
        for i in range(len(window_data)):
            for j in range(i+1, len(window_data)):
                distance = calculate_edit_distance(window_data[i], window_data[j])
                if distance == 0:
                    duplicates.append((window_start+i, window_start+j, distance))
                    
                    # add adjacent records to the window
                    start = max(0, window_start+i-w+1)
                    end = min(len(data), window_start+j+w-1)
                    window_start = start
                    window_end = end
                    window_data = data[window_start:window_end]
                    break  # exit inner loop if duplicates are found
        
        # slide the window if no duplicates found
        window_start += 1
        window_end += 1
        window_data = data[window_start:window_end]

    # print the list of duplicates
    for i, j, distance in duplicates:
        print(f"{data[i]} and {data[j]} are duplicates (edit distance = {distance})")

    # define a function to calculate the edit distance
    # def calculate_edit_distance(s1, s2):
    #     # replace with your own implementation of the edit distance algorithm
    #     distance = 0
    #     return distance


def upload_file():
    file=filedialog.askopenfilename(title="Select file" , filetypes=[("All files", '*.*'),("CSV files", '.csv')])

    if(file):
        lbl_my_file=Label(window, text="File read!", font=("arial", 12, "bold") )
        lbl_my_file.pack()
        threshold=10
        chunk_size=100
        df=pd.read_csv(file, chunksize=chunk_size)

        file_name.set(file)
        duplicate_list=[]

        for chunk in pd.read_csv(file, chunksize=chunk_size):
            chunk["modified_name"] = chunk["name"].str.replace(" ", "")            
            std_att = chunk['modified_name'].astype(str) + chunk['age'].astype(str) + chunk['age_unit'].astype(str) + chunk['province_id'].astype(str) + chunk['district_id'].astype(str) + chunk['municipality_id'].astype(str) + chunk['tole'].astype(str) + chunk['ward'].astype(str) + chunk['caste'].astype(str) + chunk['sex'].astype(str)

            # apply the edit distance function to the string array
            duplicates = find_duplicates(std_att, threshold)
            length= len(duplicates)
            lbl_duplicate=Label(window, text="Number of duplicates detected")
            lbl_duplicate.pack()
            lbl=Label(window,text=length)
            lbl.pack()
            mylist = Text(window)
            mylist.pack(side=LEFT, fill=BOTH, expand=True)

            # create a scrollbar and associate it with the listbox
            sb = Scrollbar(window)
            sb.pack(side=RIGHT, fill=Y)
            mylist.config(yscrollcommand=sb.set)
            sb.config(command=mylist.yview)

            # create scrollbar
            sb = Scrollbar(window)
            sb.pack(side=BOTTOM, fill=BOTH)
            
            window.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
        

            for i, j, distance in duplicates:
                duplicate_list.append(f"{std_att[i]} and {std_att[j]} are duplicates (edit distance = {distance})")
                mylist.insert(END, f"{std_att[i]} and {std_att[j]} are duplicates (edit distance = {distance})\n")
            
            duplicate_list.sort()
            dcs(duplicate_list)
            # print(duplicate_list)

        






        
    
window=Tk()
window.geometry("1920x1080")
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


