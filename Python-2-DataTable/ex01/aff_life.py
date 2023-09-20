from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def all_life(data: pd.DataFrame):
    '''
    Take a panda dataframe in argument.
    Transpose and display France informations.
    '''
    if data is None:
        return print("The program could not load the data")
    data_transpose = data["France":"France"].T
    data_transpose.plot(xlabel="Year", ylabel="Life expectancy",
                        title="France Life expectancy Projections")
    plt.show()


def main():
    '''
    Main funcion.
    Loads the file life_expectancy_years.csv, and displays France informations.
    '''
    try:
        all_life(load("life_expectancy_years.csv"))
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
