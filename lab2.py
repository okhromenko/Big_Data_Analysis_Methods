import matplotlib.pyplot as plt
import pandas as pd

us_states = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
prison = pd.read_csv(
    'https://raw.githubusercontent.com/nytimes/covid-19-data/master/prisons/facilities.csv')
colleges = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/colleges/colleges.csv')


def file_info():
    pd.set_option('display.max_columns', None)

    print("содержание файла <штаты>:\n", us_states)
    print("\nТип данных столбцов в файле <штаты>:\n", us_states.dtypes)

    print("\n\nсодержание файла <тюрьмы>:\n", prison)
    print("\nТип данных столбцов в файле <тюрьмы>:\n", prison.dtypes)

    print("\n\nсодержание файла <учебные заведения>:\n", colleges)
    print("\nТип данных столбцов в файле <учебные заведения>:\n", colleges.dtypes)


def states(value):
    us_states_d = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv",
                              index_col=[0])

    plt.rcParams['figure.figsize'] = [12, 17]

    for i in set(us_states_d['state']):
        x = us_states_d[us_states_d['state'] == i][value]
        x.plot(label=i)

    us_states_sort = (us_states[us_states['date'] == '2022-10-27']).sort_values(by=value, ascending=False)
    print(value, "\n", us_states_sort.state)

    plt.title(f"The dynamics of {value} by state")
    plt.grid()
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()


def colleges_VS_prisons():
    prison = pd.read_csv(
        'https://raw.githubusercontent.com/nytimes/covid-19-data/master/prisons/facilities.csv', index_col=[1])
    colleges = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/colleges/colleges.csv',
                           index_col=[5])

    plt.rcParams['figure.figsize'] = [12, 17]

    x_colleges = colleges['cases'].sum()

    prison['sum_cases'] = prison[['total_inmate_cases', 'total_officer_cases']].sum(axis=1)
    x_prison = prison['sum_cases'].sum()

    print("всего заболели(colleges)", x_colleges)
    print("всего заболели(prison)", x_prison)


def most_affected_states():
    plt.rcParams['figure.figsize'] = [20, 10]

    y_deaths = list()
    y_cases = list()
    x = list()

    for i in set(us_states['state']):
        x.append(i)
        y_deaths.append(us_states[us_states['state'] == i]['deaths'].max())
        y_cases.append(us_states[us_states['state'] == i]['cases'].max())

    plt.barh(x, y_cases)
    plt.barh(x, y_deaths)
    plt.title("Histogram of affected states(cases/deaths)")
    plt.xlabel("value")
    plt.ylabel("states")
    plt.grid()
    plt.show()


def most_affected_colleges():
    plt.rcParams['figure.figsize'] = [25, 8]

    y_cases = list()
    x = list()

    df_sort = colleges.sort_values(by='cases', ascending=False)
    for i in df_sort['college']:
        x.append(i)
        value = df_sort[df_sort['college'] == i]['cases'].max()

        y_cases.append(value)
        print(i, "  ", value)

    plt.barh(x[0:20], y_cases[0:20])
    plt.title("Histogram of affected colleges(cases)")
    plt.xlabel("value")
    plt.ylabel("colleges")
    plt.grid()
    plt.show()


def most_affected_prison(value):
    plt.rcParams['figure.figsize'] = [28, 8]

    y_cases = list()
    x = list()

    prison['sum_cases'] = prison[['total_inmate_cases', 'total_officer_cases']].sum(axis=1)
    prison['sum_deaths'] = prison[['total_inmate_deaths', 'total_officer_deaths']].sum(axis=1)

    prison_sort = prison.sort_values(by=value, ascending=False)
    for i in prison_sort['facility_name']:
        x.append(i)

        date = prison[prison['facility_name'] == i][value].max()
        y_cases.append(date)

        print(i, "  ", value, " ", date)

    plt.barh(x[0:20], y_cases[0:20])
    plt.title(f"Histogram of affected prison({value})")
    plt.xlabel("value")
    plt.ylabel("prisons")
    plt.grid()
    plt.show()


# file_info()
# states('cases')
# states('deaths')
# colleges_VS_prisons()
# most_affected_states()
# most_affected_colleges()
# most_affected_prison('sum_cases')
# most_affected_prison('sum_deaths')
