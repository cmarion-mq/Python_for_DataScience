class calculator:
    '''Calculator class'''
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Class Calculator dotproduct method. Take two lists in argument
        and print the dot product of the two lists'''
        try:
            print("Dot product is:",
                  sum([V1[a] * V2[a] for a in range(len(V1))]))
        except Exception as err:
            print(err)

    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''Class Calculator add_vect method. Take two lists in argument
        and print a vector with the sum of the elements two lists'''
        try:
            print("Add Vector is :",
                  [float(V1[a] + V2[a]) for a in range(len(V1))])
        except Exception as err:
            print(err)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''Class Calculator sous_vect method. Take two lists in argument
        and print a vector with the soustraction of the elements two lists'''
        try:
            print("Sous Vector is:",
                  [float(V1[a] - V2[a]) for a in range(len(V1))])
        except Exception as err:
            print(err)
