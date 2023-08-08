def oxford_comma(fruits):

    if len(fruits) == 1:
        return fruits[0]
    elif len(fruits) == 2:
        return " and ".join(fruits)
    elif len(fruits) == 3:
        return fruits[0] + ", " + fruits[1] + ", and " + fruits[2]
    else:
        return ", ".join(fruits[0:-1]) + ", and " + fruits[-1]