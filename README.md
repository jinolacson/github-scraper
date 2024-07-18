# github-scraper
Python script that scrap developers information in github

```
sudo apt install python3-pip python3-virtualenv
```
### Rename envionment file
```
mv tmpl.env .env
```

### Insert credentials
``` 
GITHUB_USERNAME=
GITHUB_TOKEN=
PDL_API_KEY=
```

### Create virtual environment
```
cd github-scrapper
virtualenv github-scrapper
```

### Activate virtual environment
```
source github-scrapper/bin/activate
pip install -r requirements.txt
```

### Update your setting in `run.py`
```
keyword = "Python"
```

### Run 
```
python3 run.py
```


# Running thru docker
Open docker file and update github keys

```
# Github keys
ENV GITHUB_USERNAME 
ENV GITHUB_TOKEN  
ENV PDL_API_KEY 
```

Build image
```
docker build --tag scrap-demo .
```

Run 
```
docker run scrap-demo
```

View result folder
```
docker exec -it {container_id} bash
```

### Clear all images and containers after usage
```
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
```

# Search using pdl 

### Update the `run_person_search.py` with your prefer query please reference to the [docs](https://dashboard.peopledatalabs.com/tools/query-builder) 
```
ES_QUERY = {
    "query": {
        "bool": {
            "must": [
                {
                    "terms": {
                        "skills": [
                            "vue.js",
                            "php"
                        ]
                    }
                },
                {
                    "terms": {
                        "countries": [
                            "philippines",
                            "canada",
                            "argentina"
                        ]
                    }
                },
                {
                    "exists": {
                        "field": "experience.title"
                    }
                }
            ]
        }
    }
}

```

### Run and start searching
```
python run_person_search.py
```
