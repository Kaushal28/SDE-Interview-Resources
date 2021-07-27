# URL Shortener

## Getting Started

### Using Docker Image

To run the URL shortener, fire the following commands:

```shell
docker pull kaushal28/urlshortener:latest
docker run -d -p 80:80 -e STORE_TYPE=<MEMORY|FILE> kaushal28/urlshortener:latest
```

The docker container should be up and running after firing the above command. Check the status using the following command:

```
docker ps
```

The output should be similar to this:

```shell
CONTAINER ID   IMAGE                           COMMAND              CREATED         STATUS         PORTS                               NAMES
1a9ebcdb0a55   kaushal28/urlshortener:latest   "/bin/sh start.sh"   4 minutes ago   Up 4 minutes   0.0.0.0:80->80/tcp, :::80->80/tcp   affectionate_carver
```

### Using Git Repository

Clone the Github repo using the following command:

```shell
git clone https://github.com/Kaushal28/url-shortener.git
cd url-shortener
```

Install the Python requirements:

```shell
python -m pip install -r requirements.txt
```

Start the API server:

```shell
uvicorn src.main:app
```

The output should be similar to this:

```
INFO:     Started server process [9432]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Shortening the URLs

Once the server is up and running using one of the above methods, make a POST request to `/shorten` endpoint with
long URL as the request body. Here is the sample cURL command (Assuming that the server is running at `http://localhost:80`):

```shell
curl --location --request POST "http://localhost:80/shorten" \
--header "Content-Type: application/json" \
--data "{
	\"url\": \"https://www.google.com\"
}"
```

The response should be something like this:

```json
{
    "url": "http://localhost:80/ac6bb669"
}
```

Which is the shortened version of the given URL.

### Note

To view the swagger documentations of the available endpoints, visit: `http://localhost/docs#/` (Assuming that the server is hosted on `localhost`) 


## Visiting the shortened URLs

Once you have a shortened URL, open a browser and paste it in the search bar.
It should redirect to the original URL.

Here is an example:

<p align="center"><img src="https://i.imgur.com/R7T17Gq.gif" width="800" height="500"></p>


## Assumptions and Trade-offs

- To generate short URLs, I could think of two approaches:
    - Hash the long URL and use the first 8 characters
    - Base 62 of an autoincrement counter
    
- The second approach would be preferable if for every new request, a unique short URL needed to be generated (No duplication check). Checking duplicates using this approach would involve more storage.
- Checking duplicate URLs would be easier using the first approach. However, there are slight chances of hash collision.
