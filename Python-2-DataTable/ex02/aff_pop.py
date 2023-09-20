from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def aff_pop(data: pd.DataFrame, versus: str):
    '''
    Take a panda dataframe in argument wich discribe all world coutries
    populations. Transpose the dataframe and display France versus Colombie
    informations between 1850 and 2050.
    '''
    if data is None:
        return print("The program could not load the data")
    repl_dict = {'[kK]': '*1e3', '[mM]': '*1e6', '[bB]': '*1e9'}
    data_transpose = data.T
    db = data_transpose[["France", versus]].replace(repl_dict, regex=True)\
        .applymap(eval).astype(int)
    df_between = db.loc['1850':'2050']
    df_between.plot(xlabel="Year", ylabel="Population",
                    title="Population Projections")
    plt.show()


def main():
    '''
    Main funcion.
    Loads the file population_total.csv, displays the country information of
    your campus versus Colombia.
    '''
    try:
        aff_pop(load("population_total.csv"), 'Colombia')
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
