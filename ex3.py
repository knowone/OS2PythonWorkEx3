import re


# Assignment 1:
def find_top_city_postcode():
    """
    Cool, but inefficient, solution using a regex search and a custom
    regex search for each (city, state) pair.
    We first search through the top 30 cities from the list, extracting the
    name of the city and it's state's name. Then we search for that pair in
    the city data file for the postcode. Since their could be many  postcodes
    for the same city, we give only the last one - as in the examples given.
    """

    def search_postcode(city_name, state, database):
        """
        Search the regex with city and state strings in the database.
        The regex we search is in the given form: (\d*),{city_name},{state}
        where {city_name} and {state} are placeholders taken from parameters
        :param city_name: the city name in the database
        :param state: the state name in the database
        :param database: csv file with the cities' data
        :return: the last postal code for that city in that state.
        """
        my_regex = r"(\d*)," + re.escape(city_name) + "," + re.escape(state)
        try:
            result = re.findall(my_regex, database)
            return result[-1]
        except KeyError:
            pass

    top_cities_content = open("largest_cities.txt", "r").read()
    top_cities = re.findall(
        r"\d+([A-Z][A-Za-z\s?]*[a-z])([A-Z][A-Za-z\s?]*)\d",
        top_cities_content)
    city_data_content = open("us_postal_codes.csv", "r").read()

    for i, city in zip(range(1, 31), top_cities):
        print(i, ":", city[0],
              search_postcode(city[0], city[1], city_data_content))


# Assignment 2:
def list_run_correctly(log_filename, output_filename):
    """
    Print to file a list of all the correctly run files as listed in the
    atoms2.log file provided.
    :param log_filename: The file containing the data for the function.
    :param output_filename: The output filename.
    :return: no output is returned.
    """
    atom_content = open(log_filename, "r").read()
    atom_results = re.findall(
        r"RUN\s(\d*).*FILE\s(\w*.dat).\s\d*.\d*\sCPU",
        atom_content)

    result_file = open(output_filename, "w")
    for atom in atom_results:
        result_file.write(atom[0] + " " + atom[1] + "\n")

    result_file.close()


def main():
    print("----------------- Assignment 1: ----------------------\n")
    print("Listing postcodes for top 30 biggest cities in the US:\n")
    print("------------------------------------------------------\n")
    find_top_city_postcode()
    print("\n----------------- Assignment 2: ----------------------")
    print("\nCreating file with all files run correctly...\n")
    list_run_correctly("atoms2.log", "results.txt")
    print("Check file \"results.txt\"\n")
    print("------------------------------------------------------")

main()
