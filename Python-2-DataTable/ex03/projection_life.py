from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def projection_life(gross_national_product: pd.DataFrame,
                    life_expectancy: pd.DataFrame):
    '''
    Take two panda dataframe in argument wich discribe life expectancy and
    the gross national product per country, and put them in relation
    for the year 1900.
    '''
    if gross_national_product is None or life_expectancy is None:
        return print("The program could not load the data")
    gross_national_product_1900 = gross_national_product['1900']
    life_expectancy_1900 = life_expectancy['1900']
    gnp_le_1900 = pd.concat(
        [gross_national_product_1900, life_expectancy_1900], axis=1)
    gnp_le_1900.columns = ["gross_national_product", "life_expectancy"]
    plot = gnp_le_1900.plot(x="gross_national_product", y="life_expectancy",
                            kind="scatter", xlabel="Gross domestic product",
                            ylabel="Life Expectancy", title="1900")
    plot.axis(xmin=300, xmax=11000)
    plot.set_xscale("log")

    plt.show()


def main():
    '''
    Main funcion.
    Loads the file population_total.csv and displays the projection of life
    expectancy in relation to the gross national product of the year 1900
    for each country.
    '''
    try:
        gross_national_product =\
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_expectancy = load("life_expectancy_years.csv")
        projection_life(gross_national_product, life_expectancy)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
