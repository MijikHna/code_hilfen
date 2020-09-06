1. Go Docker-Image:
```dockerfile
FROM golang:latest

WORKDIR /app

COPY ./ /app

RUN go mod download

RUN go get github.com/githubnemo/CompileDaemon

ENTRYPOINT CompileDaemon --build="go build commands/runserver.go" --command=./runserver
```
* image builden
* `docker run -v ~/projects/go-docker:/app -p 80:80 go-docker-image` - Docker-Go-Image starten
* man aknn auch Docker-Compose dafür benutzen
```yaml
version: "3"
services:
  go-docker-image:
    build: ./
    ports:
      - '80:80'
    volumes:
      - ./:/app
```