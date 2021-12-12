def stepTwo(ws):

    # determine if negative value exists in the set
    def checkForAllPositives(row_cells):
        for i in range(12, len(row_cells)):
            if row_cells[i].value < 0:
                return False
        return True

    # create placeholders for training/testing set data
    res = {
        "0-4": {
            "gender": {
                "male": 0,
                "female": 0
            },
            "health": {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0
            }
        },
        "4-8": {
            "gender": {
                "male": 0,
                "female": 0
            },
            "health": {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0
            }
        },
        "8-12": {
            "gender": {
                "male": 0,
                "female": 0
            },
            "health": {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0
            }
        },
        "12-16": {
            "gender": {
                "male": 0,
                "female": 0
            },
            "health": {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0
            }
        },
        "16-20": {
            "gender": {
                "male": 0,
                "female": 0
            },
            "health": {
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0
            }
        }
    }

    # traverse through all sheets
    for index, row_cells in enumerate(ws.iter_rows()):

        # we don't want to include column header
        if index >= 2:

            # fetch gender of person
            gender = row_cells[1].value
            health = row_cells[28].value
            g3 = row_cells[-1].value

            # placeholder for bucket arrangement 
            resIndex = ""

            # determine which bucket each record should belong to based on G3 score
            if g3 >= 0 and g3 < 4:  
                resIndex = "0-4"
            elif g3 >= 4 and g3 < 8:
                resIndex = "4-8"
            elif g3 >= 8 and g3 < 12:
                resIndex = "8-12"
            elif g3 >= 12 and g3 < 16:
                resIndex = "12-16"
            elif g3 >= 16 and g3 <= 20:
                resIndex = "16-20"
            else:
                print("Invalid Value Found For Res Index: {}".format(gender))

            # handle gender based on provided value
            if gender == "M":
                res[resIndex]["gender"]["male"] += 1
            elif gender == "F":
                res[resIndex]["gender"]["female"] += 1
            else:
                print("Invalid Value Found For Gender: {}".format(gender))

            # handle health based on provided values
            if health == 1:
                res[resIndex]["health"]["1"] += 1
            elif health == 2:
                res[resIndex]["health"]["2"] += 1
            elif health == 3:
                res[resIndex]["health"]["3"] += 1
            elif health == 4:
                res[resIndex]["health"]["4"] += 1
            elif health == 5:
                res[resIndex]["health"]["5"] += 1
            else:
                print("Invalid Value Found For Health: {}".format(health))
                exit()

    return res