import csv
import matplotlib.pyplot as plt


def resultsBySelection(countries, security_indices, selection):
    countriesFinal = countries[:9]
    pointsFinal = security_indices[:9]
    title = "Most women peace and security countries by Index Score 2023"

    if selection == "2":
        countriesFinal = countries[-9:]
        pointsFinal = security_indices[-9:]
        title = "Less women peace and security countries by Index Score 2023"

    createBarChart(
        countriesFinal,
        pointsFinal,
        title,
        "Countries",
        "Index Score",
    )


def createBarChart(labels, values, title="Bar graph", xlabel="x", ylabel="y"):
    fig, ax = plt.subplots()
    ax.bar(labels, values)

    # Adding title and labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    plt.show()


def initAskQuestion():
    print("Welcom to women peace and security countries data graph")
    print("Type 1 for most women peace and security countries.")
    print("Type 2 for less women peace and security countries.")
    selecction = input("")
    return selecction


def readCsv(path):
    with open(path, "r") as csvFile:
        reader = csv.reader(csvFile, delimiter=",")
        header = next(reader)
        data = []

        for row in reader:
            iterable = zip(header, row)
            dataDict = {key: value for key, value in iterable}
            data.append(dataDict)

    return data


def cleanData(dataList):
    # Taking out extra data
    returningData = list(
        map(
            lambda element: {
                "country": element["country"],
                "securityIndex": float(
                    element[
                        "MostDangerousCountriesForWomen_WomenPeaceAndSecurityIndex_Score_2023"
                    ]
                ),
            },
            dataList,
        )
    )

    # Ordering descending
    orderedData = sorted(returningData, key=lambda x: x["securityIndex"], reverse=True)

    # Difference for key and value arrays
    countries = [item["country"] for item in orderedData]
    security_indices = [item["securityIndex"] for item in orderedData]

    return countries, security_indices
