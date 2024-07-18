# syntax=docker/dockerfile:1

FROM python:3.10.5-slim-buster

WORKDIR /github-scraper

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Github keys
# ENV GITHUB_USERNAME ''
# ENV GITHUB_TOKEN ''
# ENV PDL_API_KEY ''

# updgrade to pip3
RUN /opt/venv/bin/python3 -m pip install --upgrade pip

# Install dependencies:
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Run the application:
COPY . .
CMD ["python3", "run.py"]
