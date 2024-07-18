import utilities
import json
import time
import csv
import os
import pandas as pd
from pandas import json_normalize

json_file_location = "my_pdl_enrichment.json"
# # See https://github.com/peopledatalabs/peopledatalabs-python
# # https://docs.peopledatalabs.com/recipes/generate-a-lead-list
# # https://docs.peopledatalabs.com/docs/examples-person-search-api#bulk-retrieval
# # https://docs.peopledatalabs.com/docs/input-parameters-person-search-api#scroll_token


# merge two CSV files of github users
def merge_csv():
    print("Merging...")

# CSV file comming from scrapped github users
# Run it for the ones without emails and don’t send duplicates across both lists.
# Also please in your request specify that emails is a required field. We don’t want to pay for a match if they don’t have an email.
# Of the response fields we want, we’d like email and linkedin URL if they have it.
def remove_duplicate_rows_csv():
    print("Cleaning removing duplicates...")
    data = pd.read_csv('alter.csv')
    new_df = pd.concat([pd.Series(data[i].unique())
                       for i in data.columns], axis=1)
    new_df.columns = data.columns
    new_df.to_csv('alter.csv', index=False)


def change_to_linkedin_csv():
    print("Changing links to linkedin")
    df = pd.read_csv("alter.csv")
    ddata = df['Username']

    for d in ddata:
        user = f'linkedin.com/in/{d}'
        obj = json.dumps({
            'params': {
                'profile': [user],
                'required': 'emails'
            },
        })
        df['Username'] = df['Username'].replace({d: obj})
    data = pd.DataFrame(df)
    print(data)
    # writing into the file
    data.to_csv("parameters.json", header=None, index=False)


def pull_data():
    from peopledatalabs import PDLPY

    # Limit the number of records to pull (to prevent accidentally using
    # more credits than expected when testing this code)
    MAX_NUM_RECORDS_LIMIT = 150  # The maximum number of records to retrieve
    USE_MAX_NUM_RECORDS_LIMIT = True  # Set to False to pull all available records

    # Create a client, specifying your API key
    API_KEY = os.getenv("PDL_API_KEY")
    client = PDLPY(
        api_key=API_KEY,
    )
    all_records = []
    # Create a parameters JSON object
    data = {
        "requests": [
            {"params": {"profile": [
                "linkedin.com/in/shyim"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/keulinho"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/janbuecker"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/leichteckig"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/SebastianFranze"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/mitelg"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/ssltg"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/taltholtmann"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/jenskueper"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/Phil23"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/JanPietrzyk"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/seggewiss"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/pantrtxp"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/benjamin-ott"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/marcelbrode"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/raknison"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/King-of-Babylon"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/PaddyS"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/mstegmeyer"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/philipgatzka"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/Haberkamp"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/dneustadt"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/Staff-d"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/vienthuong"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/lernhart"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/arnoldstoba"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/Cipfahim"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/aschempp"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/ausi"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/leofeyer"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/xchs"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/cliffparnitzky"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/akroii"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/Floxn"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/fritzmg"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/najbo"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/JulienSteininger"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/lorenzbausch"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/manuelm"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/oliverjkb"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/ReneLuecking"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/taca"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/gmpf"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/webkp"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/EliteDevSolution"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/TheRatG"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/ChrisDBrown"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/arthurperton"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/ebeauchamps"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/JohnathonKoster"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/jacksleight"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/edalzell"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/ryanmitchell"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/helloDanuk"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/sauerbraten"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/aryehraber"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/jonassiewertsen"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/aerni"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/wiebkevogel"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/riasvdv"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/FrittenKeeZ"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/stvnthomas"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/j3ll3yfi5h"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/jannejava"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/jsbls"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/tomhelmer"], "required": "emails"}},
            {"params": {"profile": [
                "linkedin.com/in/andershagbard"], "required": "emails"}},

        ]
    }

    # Pass the parameters object to the Person Search API
    json_responses = client.person.bulk(**data).json()

    with open(json_file_location, "w") as out:
        out.write(json.dumps(json_responses) + "\n")


# Convert json file to csv
def convert_to_csv():
    # load json object
    df = pd.read_json(json_file_location)

    df = pd.json_normalize(df.data)
    columns = ['full_name', 'job_title', 'job_company_name', 'job_company_website', 'work_email', 'personal_emails', 'emails', 'mobile_phone', "linkedin_url", "location_country",
               "github_url", "skills"]
    df.to_csv("data.csv", columns=columns, index=False)


# merge_csv()
# remove_duplicate_rows_csv()
# change_to_linkedin_csv()
# pull_data()
# convert_to_csv()
