def sumColumnsAndRows(matrix): 
    sumCols = []
    sumRows = []

    for i in range(len(matrix)):
        sumCol = 0
        sumRow = 0

        for j in range(len(matrix[i])):
            sumCol += matrix[i][j]
            sumRow += matrix[j][i]

        sumCols.append(sumCol)
        sumRows.append(sumRow)
    
    return [sumCols, sumRows]

