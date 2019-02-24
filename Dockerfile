# Get Data
FROM debian:jessie as data

RUN apt-get update && apt-get install -y \
    git \
    curl \
    jq

WORKDIR /root
RUN ["/bin/bash", "-c", "mkdir data && cd data && while read i; do git clone $i; done < <(curl -s https://api.github.com/orgs/datasets/repos?per_page=100 | jq -r '.[].clone_url')"]


# Bulild App
FROM python:3
COPY --from=data /root/data /usr/src/data

WORKDIR /usr/src/app
COPY . .
CMD ["python", "./main.py --all"]

# Tests Setup
RUN pip install --no-cache-dir -r requirements.txt

# Command To Run Tests
CMD ["pytest -v"]
