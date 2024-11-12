import tools

if __name__ == "__main__":
    # Retriving csv data
    csvData = tools.readCsv("assets/most-dangerous-countries-for-women-2024.csv")

    # Clean data
    countries, security_indices = tools.cleanData(csvData)

    # Asking for data to show
    result = tools.initAskQuestion()

    # Showingn up results
    tools.resultsBySelection(countries, security_indices, result)
