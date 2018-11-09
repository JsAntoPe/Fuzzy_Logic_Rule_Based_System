import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as plty
import plotly.graph_objs as go
import plotly


plotly.tools.set_credentials_file(username='JsAntoPe', api_key='FYoXSRfgoO7uVToeBeKK')


def alittle(result):
    return pow(result, 1.3)


def slightly(result):
    return pow(result, 1.7)


def very(result):
    return pow(result, 2)


def extremely(result):
    return pow(result, 3)


def veryvery(result):
    return pow(result, 4)


def moreorless(result):
    return pow(result, 1/2)


def somewhat(result):
    return moreorless(result)


def indeed(result):
    if result <= 0.5:
        return 2 * very(result)
    else:
        return 1 - 2 * (1 - very(result))


edges = {
    'alittle': alittle,
    'slightly': slightly,
    'very': very,
    'extremely': extremely,
    'veryvery': veryvery,
    'moreorless': moreorless,
    'somewhat': somewhat,
    'indeed': indeed
}


def fuzzytransforming(range, input):
    if input > range[-1] or input < range[0]:
        return 0

    else:
        if range[1] - range[0] == 0:
            firstf = 1

        else:
            firstf = (input - range[0]) * (1 / (range[1] - range[0]))

        if range[-1] - range[-2] == 0:
            secondf = 1

        else:
            secondf = 1 + (input - range[-2]) * (-1 / (range[-1] - range[-2]))

        fx = max(min(firstf, 1, secondf), 0)
        return fx


def complexfuzzy(ranges: dict, input, edgestoapply=None):
    if edgestoapply is None:
        edgestoapply = []
    result = ranges.copy()
    index = 0
    for range in ranges:
        ind = fuzzytransforming(ranges[range], input)
        if edgestoapply.__len__() > 0:
            if edges.__contains__(edgestoapply[index]):
                ind = edges[edgestoapply[index]](ind)

        result[range] = ind
        index += 1

    return result


def and_or_or(values, operator):
    if operator == 1:
        return min(values)
    else:
        return max(values)


def obtainValues(rules, sets, solutionRanges):
    solutionSet = {}
    for key in solutionRanges:
        solutionSet[key] = 0

    for rule in rules:
        values = []
        for index in range(rule.__len__() - 2):
            set = sets[index]
            if rule[index] != 0:
                values.append(set[rule[index]])

        sol = and_or_or(values, rule[-2])
        if sol > solutionSet[rule[-1]]:
            solutionSet[rule[-1]] = sol

    return solutionSet


def centerofgravity(valuesofranges):
    total = 0
    accumulated = 0
    for key in valuesofranges:
        total += key * valuesofranges[key]
        accumulated += valuesofranges[key]

    if accumulated != 0:
        return total / accumulated

    else:
        return 0


def sortedList(values):
    valuesList = []
    for value in values:
        valuesList.append([value, values[value]])
    valuesList = sorted(valuesList, key=lambda x: x[1])

    return valuesList


def centerofgravityfunction_clipping_mandani(ranges: dict, values: dict):
    valuesList = sortedList(values)

    valuesofranges = {}
    for value in valuesList:
        for number in range(ranges[value[0]][0], ranges[value[0]][-1] + 1):
            valuesofranges[number] = value[1]

    return centerofgravity(valuesofranges)


def centerofgravityfunction_scaled_mandani(ranges: dict, values: dict):
    valuesList = sortedList(values)

    valuesofranges = {}
    for value in valuesList:
        for number in range(ranges[value[0]][0], ranges[value[0]][-1] + 1):
            possibleValues = []
            values_on_number = complexfuzzy(ranges, number)
            for value_on_number in values_on_number:
                possibleValues.append(values[value_on_number] * values_on_number[value_on_number])
            valuesofranges[number] = max(possibleValues)

    return centerofgravity(valuesofranges)


def centerofgravityfunction_sugeno(ranges: dict, values: dict):
    cripsInputs = {}

    for key in ranges:
        cripsInputs[key] = ranges[key][0] + ((ranges[key][-1] - ranges[key][0]) / 2)

    total = 0
    accumulated = 0
    for key in cripsInputs:
        total += cripsInputs[key] * values[key]
        accumulated += values[key]

    if accumulated != 0:
        return total / accumulated

    else:
        return 0


def two_dim_plot(ranges: dict, filename):
    maximun_value_of_x = max(max(ranges.values()))
    x = np.arange(maximun_value_of_x + 1)
    values = np.zeros([maximun_value_of_x + 1, ranges.__len__()])
    for number in range(maximun_value_of_x + 1):
        index = 0
        for value in complexfuzzy(ranges, number).values():
            values[number][index] = value
            index += 1
    # Create traces
    data = []
    yvalues = np.hsplit(values, ranges.__len__())
    for index in range(ranges.__len__()):
        data.append(go.Scatter(
            x=x,
            y=yvalues[index],
            mode='lines',
            name='lines'
        ))

    fig = go.Figure(data=data)
    plty.iplot(fig, filename=filename)


def three_dim_plot(rules, ranges, usedOnFigure, solutionRanges, filename, centerofgravityfunction):
    dimensionOfMatrix = []
    inputs = []
    for i in range(usedOnFigure.__len__()):
        if usedOnFigure[i]:
            maxValueOfTheRange = lambda r: max(max(r.values()))+1
            dimensionOfMatrix.append(maxValueOfTheRange(ranges[i]))
            inputs.append(0)
        else:
            valueOfTheHalf = lambda r: (max(max(r.values()))-min(min(r.values())))/2
            inputs.append(valueOfTheHalf(ranges[i]))

    indexesOfChangingInputs = []
    for input in range(inputs.__len__()):
        if inputs[input] == 0:
            indexesOfChangingInputs.append(input)
        inputs[input] = complexfuzzy(ranges[input], inputs[input])

    x = np.arange(0, dimensionOfMatrix[0])
    y = np.arange(0, dimensionOfMatrix[1])
    z = np.empty([x.__len__(), y.__len__()])
    for i in range(x.__len__()):
        inputs[indexesOfChangingInputs[0]] = complexfuzzy(ranges[indexesOfChangingInputs[0]], x[i])
        for j in range(y.__len__()):
            inputs[indexesOfChangingInputs[1]] = complexfuzzy(ranges[indexesOfChangingInputs[1]], y[j])
            solutionValues = obtainValues(rules, inputs, solutionRanges)
            z[i][j] = centerofgravityfunction(solutionRanges, solutionValues)

    data = [
        go.Surface(
            z=z,
            visible=True
        )
    ]

    layout = go.Layout(
        title=filename,
        autosize=True,
        xaxis=dict(
            ticks='outside'
        ),
        yaxis=dict(
            ticks='outside'
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plty.iplot(fig, filename=filename)
