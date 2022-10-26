def Algoritmo(data):
    data = data.str.lower()
    data = data.str.replace(".", "")
    data = data.str.replace("cll", "cl ")
    data = data.str.replace("calle", "cl ")
    data = data.str.replace("calla", "cl ")
    data = data.str.replace("call", "cl ")
    data = data.str.replace("carrera", "cra ")
    data = data.str.replace("carr", "cra ")
    data = data.str.replace("cr ", "cra ")

    for index, val in enumerate(data):
        try:
            data.loc[index] = "cl " + val.split("cl ")[1]
        except:
            try:
                data.loc[index] = "cra " + val.split("cra ")[1]
            except:
                continue

    for index, val in enumerate(data):
        try:
            data.loc[index] = val.split("casa")[0]
        except:
            try:
                data.loc[index] = val.split("torre")[0]
            except:
                try:
                    data.loc[index] = val.split("apto")[0]
                except:
                    continue

    for index, val in enumerate(data):
        data.loc[index] = " ".join(val.split())

    return data