import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''
    Laod a csv file and return its informations in panda database.
    '''
    if not path.endswith('csv'):
        return print("The program only works with .csv file")
    try:
        data = pd.read_csv(path, index_col=0)
        print("Loading dataset of dimensions", data.shape)
    except Exception as err:
        return print(err)
    return data
