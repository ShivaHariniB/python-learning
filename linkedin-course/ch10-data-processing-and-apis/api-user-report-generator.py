import requests
import json

base_url = "https://jsonplaceholder.typicode.com/users"


def get_user_info():
    try:
        response = requests.get(base_url)

        if response.status_code == 200:
            with open("users.json", "w") as file:
                json.dump(response.json(), file, indent=4)
        else:
            print(f"API Failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Something went wrong {e}")


get_user_info()

# ------------------------------------------city-wise reports-------------------------------

city_wise_report = {}

with open("users.json", "r") as file:
    user_data = json.load(file)
for user in user_data:
    user_count = user["address"]["city"]
    city_wise_report[user_count] = city_wise_report.get(user_count, 0)+1

with open("report.txt", "w") as file:
    file.write("USER ANALYTICS REPORT\n")
    file.write("=====================\n")
    file.write(f"Total User count: {len(user_data)}\n\n")
    file.write("CITY-WISE REPORT\n")
    file.write("---------------------\n")
    json.dump(city_wise_report, file, indent=4)

# print(f"city_wise_report: {json.dumps(city_wise_report, indent=4)}")

# ------------------------------------------company-wise reports-------------------------------

company_wise_report = {}

# with open("users.json", "r") as file:     no need to open file and read data twice
#     user_data = json.load(file)
for user in user_data:
    company_count = user["company"]["name"]
    company_wise_report[company_count] = company_wise_report.get(
        company_count, 0)+1

with open("report.txt", "a") as file:
    file.write("\n\nCOMPANY-WISE REPORT\n")
    file.write("---------------------\n")
    json.dump(company_wise_report, file, indent=4)

# print(f"company_wise_report: {json.dumps(company_wise_report, indent=4)}")
