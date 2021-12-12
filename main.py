from openpyxl import load_workbook
#from creditWorthiness import creditWorthiness
from stepTwo import stepTwo
from matplotlib import pyplot as plt
import pandas as pd
import json

# create placeholder for credit worthiness
creditWorthinessResults = {
    "0-9": [],
    "10-19": [],
    "20-29": [],
    "30-39": [],
    "40-49": [],
    "50-59": [],
    "60-69": [],
    "70-79": [],
    "80-89": [],
    "90-99": []
}

# STEP #4
def computeCost(threshold, score, default):

    # final result placeholder based on given variables
    res = 0

    # Approved Loan/Good Credit Risk = +10 Profit
    if score > threshold:
        if default == 1:
            res = -5
        elif default == 0:
            res = 10
        else:
            print("invalid default score")
            res = 0
    elif score <= threshold:
        if default == 1:
            res = 0
        elif default == 0:
            res = -3
        else:
            print("invalid default score")
            res = 0

    return res

    # - Approved Loan/Good Credit Risk = +10 Profit
    # - Approved Loan/Bad Credit Risk = -5 Profit
    # - Declined Loan/Good Credit Risk = -3 Profit
    # - Decline Loan/Bad Credit Risk = 0 Profit

def stageCreditWorthinessScore(trainingSetRecord, creditWorthinessScore):

    # place result into bucket based on score
    if creditWorthinessScore < .10:
        creditWorthinessResults["0-9"].append(trainingSetRecord)

    elif creditWorthinessScore >= .10 and creditWorthinessScore < .20:
        creditWorthinessResults["10-19"].append(trainingSetRecord)

    elif creditWorthinessScore >= .20 and creditWorthinessScore < .29:
        creditWorthinessResults["20-29"].append(trainingSetRecord)

    elif creditWorthinessScore >= .30 and creditWorthinessScore < .39:
        creditWorthinessResults["30-39"].append(trainingSetRecord)

    elif creditWorthinessScore >= .40 and creditWorthinessScore < .49:
        creditWorthinessResults["40-49"].append(trainingSetRecord)

    elif creditWorthinessScore >= .50 and creditWorthinessScore < .59:
        creditWorthinessResults["50-59"].append(trainingSetRecord)

    elif creditWorthinessScore >= .60 and creditWorthinessScore < .69:
        creditWorthinessResults["60-69"].append(trainingSetRecord)

    elif creditWorthinessScore >= .70 and creditWorthinessScore < .79:
        creditWorthinessResults["70-79"].append(trainingSetRecord)

    elif creditWorthinessScore >= .80 and creditWorthinessScore < .89:
        creditWorthinessResults["80-89"].append(trainingSetRecord)

    elif creditWorthinessScore >= .90:
        creditWorthinessResults["90-99"].append(trainingSetRecord)

def plotStep4Chart():

    # organize data to be imported into python histogram
    creditWorthinessResultTotals = {
        "0-9": len(creditWorthinessResults["0-9"]),
        "10-19": len(creditWorthinessResults["10-19"]),
        "20-29": len(creditWorthinessResults["20-29"]),
        "30-39": len(creditWorthinessResults["30-39"]),
        "40-49": len(creditWorthinessResults["40-49"]),
        "50-59": len(creditWorthinessResults["50-59"]),
        "60-69": len(creditWorthinessResults["60-69"]),
        "70-79": len(creditWorthinessResults["70-79"]),
        "80-89": len(creditWorthinessResults["80-89"]),
        "90-99": len(creditWorthinessResults["90-99"])
    }

    # extract credit categories + values
    creditCategories = list(creditWorthinessResultTotals.keys())
    creditValues = list(creditWorthinessResultTotals.values())
    colors = []

    # traverse through all values
    for idx, cc in enumerate(creditCategories):
        if idx < 1.0:
            colors.append('blue')
        elif idx >= 1.0:
            colors.append([173/256, 216/256, 216/256, 0.9])

    # organize plotly figure  
    fig = plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(creditCategories, creditValues, color = colors,
            width = 0.4)

    # plotly vertical line
    plt.axvline(x=0.5, ymin=0.0, ymax=1.0, color='r', linestyle='solid', linewidth=3, label='Threshold = 10')


    # organize py plot
    plt.xlabel("Credit Worthiness")
    plt.ylabel("Members")
    plt.title("Training Data Set -- Quantity Of Males & Females Per/Each Credit Category")
    plt.legend(loc='upper right')

    # show graph
    plt.show()

def plotStep5ChartDisparateImpact(data):
    plt.bar(["Disparate Impact"], [data])
    plt.axhline(y=1.25, color='r', linestyle='-', label="non-bias upper bound (1.25)")
    plt.axhline(y=1.00, color='black', linestyle='-', label="fair (1.00)")
    plt.axhline(y=0.75, color='r', linestyle='-', label="non-bias lower bound (0.75)")
    plt.title("Loan Approval Proportion For Underprivileged Group/Privileged Group")
    plt.legend(loc='lower right')
    plt.show()
    # pass

def plotStep5ChartStatisticalParity(data):
    plt.bar(["Statistical Parity"], [data])
    plt.axhline(y=0.1, color='r', linestyle='-', label="non-bias upper bound (0.10)")
    plt.axhline(y=0, color='black', linestyle='-', label="fair (0)")
    plt.axhline(y=-0.1, color='r', linestyle='-', label="non-bias lower bound (-0.10)")
    plt.title("Loan Approval Proportion For Underprivileged Group/Privileged Group")
    plt.legend(loc='lower right')
    plt.show()


# read workbook object
wb = load_workbook('./student/student-por.xlsx')
ws = wb.active

# query for step three data
data = stepTwo(ws)

print(json.dumps(data, indent=4))

# create dataframe based on inputs GENDER
# df = pd.DataFrame({
#     "male": [9, 7, 129, 95, 26],
#     "female": [7, 7, 141, 171, 56]
# }, index = ["0-4", "4-8", "8-12", "12-16", "16-20"])

# create dataframe based on inputs HEALTH
df = pd.DataFrame({
    "1": [1, 3, 33, 38, 15],
    "2": [2, 0, 30, 35, 11],
    "3": [3, 2, 52, 52, 14],
    "4": [2, 0, 39, 52, 15],
    "5": [8, 9, 116, 89, 27]
}, index = ["0-4 (Very Bad)", "4-8 (Bad)", "8-12 (Average)", "12-16 (Good)", "16-20 (Very Good)"])

ax = df.plot.bar(rot=0)
plt.title("Health Distributon Amoung G3 (Portuguese Final Grades)")
plt.xlabel("G3 Performance In Portuguese")
plt.ylabel("Total Amount Of People")
plt.show()

# process data into histogram
# df = pd.DataFrame(data)
# ax = df.plot(kind="bar")
# ax.set_xticklabels(list(df.iloc[:,0].values))
# plt.xticks(rotation=90)

#print("all done")

