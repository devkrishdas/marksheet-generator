import pandas as pd

SUBJECTS = ["Maths", "Physics", "Programming"]


#  Function 1: grade nikalneka
def get_grade(p):
    if p >= 90:
        return "A+"
    elif p >= 80:
        return "A"
    elif p >= 70:
        return "B"
    elif p >= 60:
        return "C"
    elif p >= 50:
        return "D"
    elif p >= 40:
        return "E"
    else:
        return "F"

#Function 2: result nikalne ka
def get_result(row):
    low = []                                # jin subjects me 40 se kam hai
    for sub in SUBJECTS:
        if row[sub] < 40:
            low.append(sub)

    if len(low) == 0:
        return "PASS"
    return "FAIL (" + ", ".join(low) + " below 40)"


# Function 3: for read the file and check it
def load_data(filename):
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print("File " + filename + " not found.")
        return None

    bad_rows = []                           # galat rows ki list
    for index, row in df.iterrows():        # ek ek row dekho
        for sub in SUBJECTS:
            if row[sub] < 0 or row[sub] > 100:
                print("Warning: Row for roll " + str(row["RollNo"]) + " skipped - marks must be between 0 and 100.")
                bad_rows.append(index)
                break                       

    df = df.drop(bad_rows)                  
    
    return df


# Function 4: Total, Percentage, Grade, Result jodna 
def calculate(df):
    df["Total"] = df[SUBJECTS].sum(axis=1)          # har row ke marks ka jod
    df["Percentage"] = df["Total"] / 300 * 100
    df["Grade"] = df["Percentage"].apply(get_grade)
    df["Result"] = df.apply(get_result, axis=1)
    return df


#Function 5: ek marksheet print karna 
def print_marksheet(row):
    print()
    print(f"Roll No: {row['RollNo']} | Name: {row['Name']}")
    print(f"Maths: {row['Maths']} | Physics: {row['Physics']} | Programming: {row['Programming']}")
    print(f"Total: {row['Total']}/300 | Percentage: {row['Percentage']:.2f}%")
    print(f"Grade: {row['Grade']} | Result: {row['Result']}")


# Main program
data = load_data("marks.csv")

if data is not None:
    data = calculate(data)

    while True:
        print()
        print("===== MENU =====")
        print("1. Single marksheet")
        print("2. All marksheets")
        print("3. Exit")
        choice = input("Choice likho: ")

        if choice == "1":
            roll_text = input("Roll no: ")
            try:
                roll = int(roll_text)
            except ValueError:
                print("Invalid roll number.")
                continue                    # wapas menu pe jao

            found = data[data["RollNo"] == roll]    # us roll wali row dhundo
            if found.empty:
                print("Roll number " + str(roll) + " not found.")
            else:
                print_marksheet(found.iloc[0])

        elif choice == "2":
            for index, row in data.iterrows():
                print_marksheet(row)

        elif choice == "3":
            print("Bye!")
            break

        else:
            print("Invalid choice.")