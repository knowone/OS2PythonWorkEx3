import re


def list_run_correctly():
    atom_content = open("atoms2.log", "r").read()
    atom_results = re.findall(r"RUN\s(\d*).*FILE\s(\w*.dat).\s\d*.\d*\sCPU"
                              , atom_content)

    result_file = open("result.txt", "w")
    for atom in atom_results:
        result_file.write(atom[0] + " " + atom[1] + "\n")

    result_file.close()


def find_top_city_postcode():

    def search_post_code(city_name, state, database):
        my_regex = r"(\d*)," + re.escape(city_name) + "," + re.escape(state)
        try:
            result = re.findall(my_regex, database)
            print(city_name, result[-1])
        except KeyError:
            pass

    top_cities_content = open("largest_cities.txt", "r").read()
    top_cities = re.findall(r"\d+([A-Z][A-Za-z\s?]*[a-z])([A-Z][A-Za-z\s?]*)\d"
                            , top_cities_content)
    city_data_content = open("us_postal_codes.csv", "r").read()

    for city in top_cities:
        search_post_code(city[0], city[1], city_data_content)


def main():
    print("------------------------------------------------------")
    print("Listing postcodes for top 30 biggest cities in the US:")
    print("------------------------------------------------------\n")
    find_top_city_postcode()
    print("------------------------------------------------------")
    print("\nCreating file with all files run correctly...\n")
    list_run_correctly()
    print("Check file \"result.txt\"\n")
    print("------------------------------------------------------")
main()
