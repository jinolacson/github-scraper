# import utilities
import json, time, csv, os
# See https://github.com/peopledatalabs/peopledatalabs-python
# https://docs.peopledatalabs.com/recipes/generate-a-lead-list
# https://docs.peopledatalabs.com/docs/examples-person-search-api#bulk-retrieval
# https://docs.peopledatalabs.com/docs/input-parameters-person-search-api#scroll_token
from peopledatalabs import PDLPY

# Limit the number of records to pull (to prevent accidentally using 
# more credits than expected when testing this code)
MAX_NUM_RECORDS_LIMIT = 150 # The maximum number of records to retrieve
USE_MAX_NUM_RECORDS_LIMIT = True # Set to False to pull all available records

# Create a client, specifying your API key
API_KEY = os.getenv("PDL_API_KEY")
CLIENT = PDLPY(
    api_key=API_KEY,
)

# Create an Elasticsearch query
ES_QUERY = {
    "query": {
        "bool": {
            "must": [
                {
                    "exists": {
                        "field": "emails"
                    }
                },
                {
                    "exists": {
                        "field": "experience.title"
                    }
                },
                {
                    "term": {
                        "skills": "vue.js"
                    }
                },
                {
                    "terms": {
                        "location_country": [
                            "philippines",
                            "canada",
                            "argentina"
                        ]
                    }
                }
            ]
        }
    }
}


# Create a parameters JSON object
PARAMS = {
  'query': ES_QUERY,
  'size': 100, 
  'pretty': True
}

# Pull all results in multiple batches
batch = 1
# Store all records retreived in an array
all_records = []
# Time the process
start_time = time.time()
found_all_records = False
continue_scrolling = True

# While still scrolling through data and still records to be found
while continue_scrolling and not found_all_records: 

  # Check if we reached the maximum number of records we want
  if USE_MAX_NUM_RECORDS_LIMIT:
    num_records_to_request = MAX_NUM_RECORDS_LIMIT - len(all_records)
    # Adjust size parameter
    PARAMS['size'] = max(0, min(100, num_records_to_request))
    # Check if MAX_NUM_RECORDS_LIMIT reached
    if num_records_to_request == 0:
      print(f"Stopping - reached maximum number of records to pull "
            f"[MAX_NUM_RECORDS_LIMIT = {MAX_NUM_RECORDS_LIMIT}].")
      break

  # Pass the parameters object to the Person Search API
  response = CLIENT.person.search(**PARAMS).json()

  # Check for successful response
  if response['status'] == 200:
    # Add records retrieved to the records array
    all_records.extend(response['data'])
    print(f"Retrieved {len(response['data'])} records in batch {batch} "
          f"- {response['total'] - len(all_records)} records remaining.")
  else:
    print(f"Error retrieving some records:\n\t"
          f"[{response['status']} - {response['error']['type']}] "
          f"{response['error']['message']}")
  
  # Get scroll_token from response if exists and store it in parameters object
  if 'scroll_token' in response:
    PARAMS['scroll_token'] = response['scroll_token']
  else:
    continue_scrolling = False
    print(f"Unable to continue scrolling.")

  batch += 1
  found_all_records = (len(all_records) == response['total'])
  time.sleep(6) # Avoid hitting rate limit thresholds
 
# Calculate time required to process batches
end_time = time.time()
runtime = end_time - start_time
        
print(f"Successfully recovered {len(all_records)} profiles in "
      f"{batch} batches [{round(runtime, 2)} seconds].")

# Save profiles to CSV (utility function)
def save_profiles_to_csv(profiles, filename, fields=[], delim=','):
  # Define header fields
  if fields == [] and len(profiles) > 0:
      fields = profiles[0].keys()
  # Write CSV file
  with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=delim)
    # Write header
    writer.writerow(fields)
    # Write body
    count = 0
    for profile in profiles:
      writer.writerow([ profile[field] for field in fields ])
      count += 1
  print(f"Wrote {count} lines to: '{filename}'.")

# Use utility function to save all records retrieved to CSV    
csv_header_fields = ['full_name', 'job_title', 'job_company_name', 'job_company_website', 'work_email', 'personal_emails' , 'emails', 'mobile_phone', "linkedin_url", "location_country",
           "github_url", "skills"]
csv_filename = "all_employee_profiles.csv"
save_profiles_to_csv(all_records, csv_filename, csv_header_fields)