To build the docker image:
```
docker build -t fastapiauth .
```

To run with docker compose:
```
docker compose up -d --build
```

To run the docker image:
```
docker build .
docker run -d --name mycontainer -p 80:80 fastapiauth
```

Check the API on:
```
http://127.0.0.1/

http://127.0.0.1/docs
```

Check the App opening the supabase_signin.html or firebase_signin.html on the browser