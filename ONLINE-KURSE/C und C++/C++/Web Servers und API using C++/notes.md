### 1 - Installing Tools
#### 1 - Installing Docker
#### 2 - Installing Atom
#### 3 - Creating a Dockerfile
* ./cppweb/cppbox
* ./cppweb/cppbox/dockerfile:
```dockerfile
# gcc-Docker-Image (gnu-compiler-collection)
FROM gcc:7.3.0 

RUN apt-get -qq update
RUN apt-get -qq upgrade 
RUN apt-get -qq install cmake

RUN apt-get -qq install libboost-all-dev=1.62.0.1
RUN apt-get -qq build-essential libtcmalloc-minimal4 && \
    ln -s /usr/lib/libtcmalloc_malloc.so.4 /usr/lib/libtcmalloc_minimal.so
```
* `-qq` - quite execute = ohne Ausgabe
#### 4 - Running a Dockerfile
* ./cppweb/cppbox
* `docker build -t cppbox .`
* `docker run -ti cppbox:latest bash`
* `find /usr -name libboost*.*` - sollte mehrere boost-Files anzeigen
#### 5 - Adding a volume
* Syntax: `docker run -v HOST:CONTAINER -ti IMAGE bash` 
* `docker run -v ./cppbox:/usr/src/cppweb -it cppbox:latest bash`
* 
#### 6 - Building a Crow
* Crow = C++ Micro Web Framework (github.com/ipkn/crow); inspiriert von Flask
* auf github auf release klicken und auf crow_all klicken zum Downloaden 
* ./cppweb/hello_crow erstellen und crow_all.h hineinkopieren
* ./cppweb/hello_crwo/main.cpp ertellen
```c++
#include "crow_all.h"
using namespace std;

int main(int argc, char* argv[]){
    crow::Simple app;

    CROW_ROUTE(app, "/")
    ([](){
        return "<div><h1>Hello, Crow</h1></div>";
    });

    char *port = getenv("PORT");
    uint16_t iPORT = static_cast<uint16_t>(port != NULL ? stoi(port) : 18000);
    cout << "PORT = " << iPORT << endl;
    app.port(iPORT).multithreaded().run();
}
```
* ./cppweb/hello_crow/CMakeList.txt erstellen
```txt
cmake_minimum_requiered(VERSION 3.7)

project(hello_crow)

set(CMAKE_CXX_STANDARD 11)

set(THREADS_PREFFER__PTHREAD_FLAG ON)

find_package(Boost COMPONENTS system filesystem REQUIRED)
find_package(Threads)

include_directories(${Boost_INLCLUDE_DIRS})
add_executable(hello_crow main.cpp)
target_link_libraries(hello_crow ${Boost_LINBRARIES} Threads::Threads)
```
* in Docker: `make /usr/src/cppweb/hello_crow/build`
* `cd build`
* `cmake ..`
* `make`

#### 7 - Serving the example
+ `./hello_cro`
+ `localhost:8080`
* `docker run -v ./cppbox:/usr/src/cppweb -p HOST:CONTINER -e PORT=8081 -it cppbox:latest bash`
    + `-e PORT=8081` - environment var erstellen <- wird von C++-App benutzt
* `docker run -v ./cppbox:/usr/src/cppweb -p 8080:8080 -e PORT=8080 -it cppbox:latest bash`
#### 8 - Challenge: Modify example page

### 2 - Deploying to Heroku
#### 1 - Creating a Heroku account
+ man kann auch Free Account erstellen mit DB + Server
#### 2 - Installing the Heroku CLI
* Heroku-CLI installieren
+ `heroku --version`
#### 3 - Deploying container to Heroku
1. App Containisieren
2. in Heroku-CLI anmelden
3. Heroku-App erstellen
4. Container zu Heroku schieben
5. In Browser testen
ALSO:
* `docker ps`
    * `docker cp . CONTAINER-ID:/usr/src/cppweb`
    * `docker commit CONTAINER-ID hello_crow:latest` - man muss im Verzeichnis sein, wo der neue Dockerfile erstellt wurde
    * dockerfile erstellen:
    ```dockerfile
    FROM hello_crow

    WORKDIR /usr/src/cppweb/hello_crow/build
    CMD [ "./hello_crow" ]
    ```
    * `heroku login`
    * `heroku container:loging`
    * `heroku create` - es wird URL und URL für git-pushes angezeigt:
    * `docker build -t hello_crow` - neues Dockerfile builden
    * `heroku container:push web -a APPNAME/APPNAME_DAS_MAN_VON_HEROKU_BEKOMMEN_HAT`
    * `heroku container:release web -a APPNAME/APPNAME_DAS_MAN_VON_HEROKU_BEKOMMEN_HAT`
    * `heroku open -a APPNAME/APPNAME_DAS_MAN_VON_HEROKU_BEKOMMEN_HAT` - es dann automatisch Browser mit APP_URL geöffnent
#### 4 - Saving container to Docker Hub
* `docker login --userame=kirill`
* `docker tag IMAGE-ID kirill/iMAGE_NAME:latest`
* `docker push kirill/IMAGE_NAME`

### 3 - Building Websites
#### 1 - Creating HTML pages
+ Zwei Wege:
    1. HTML als Datei
    2. HTML + Mustache Templates -> wird bevorzugt
* Vorgehen:
    1. HTML-datei erstellen
        * ./public/index.html erstellen
        ```html
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>Crow C++</title>
            </head>
            <body>
                <div>
                    <h1>Hi, Crow</h1>
                </div>
            </body>
        </html>
        ```
    2. RouteHandler schreiben

#### 2 - Serving HTML pages
```cpp
#include "crow_all.h"
using namespace std;
using namespace crow;

int main(int argc, char* argv[]){
    crow::Simple app;

    CROW_ROUTE(app, "/")
    ([](const request &req, response &res){
        ifstream in("../public/index.html", ifstream::in);
        if (in){
            osstringstream contents;
            contents << in.rdbuf();
            in.close();

            res.write(contents.str());
        }
        else{
            res.write("Not found");
        }
        res.end();
    });

    char *port = getenv("PORT");
    uint16_t iPORT = static_cast<uint16_t>(port != NULL ? stoi(port) : 18000);
    cout << "PORT = " << iPORT << endl;
    app.port(iPORT).multithreaded().run();
}
```
* `make`
* Server/Docker neustarten
#### 3 - Serving static content
+ Stuktur für statische Dateien:
    * public
        * images
        * scripts
        * styles
        * html
```cpp
#include "crow_all.h"
using namespace std;
using namespace crow;

void sendFile(response &res, string filename, string contentType){
    ifstream in("../public/" + filename, ifstream::in);
    if (in){
        osstringstream contents;
        contents << in.rdbuf();
        in.close();

        res.set_header("Content-Type", contentType);     
        res.write(contents.str());
    }
    else{
        res.code = 404;
        res.write("Not found");
    }
    res.end();
}

void sendHtml(response &res, string filename){
    sendFile(res, filename + ".html", "text/html");
}

void sendImage(response &res, string filename){
    sendFile(res, "images/" + filename, "image/jpeg");
}

void sendScript(response &res, string filename){
    sendFile(res, "scripts/" + filename, "text/javascript");
}

void sendStyle(response &res, string filename){
    sendFile(res, "styles/" + filename, "text/css");
}

int main(int argc, char* argv[]){
    crow::Simple app;

    //Handler-Methoden
    CROW_ROUTE(app, "/")
        ([](const request &req, response &res){
            sendHtml(res, "index");
        });

    CROW_ROUTE(app, "/styles/<string>") //Route-Parameter
        ([](const request &req, response &res, string filename){ //filename ist <string>-Param ! muss wenigsten konvertierbar sein
            sendStyle(res, "index");
        });
    
    CROW_ROUTE(app, "/scripts/<string>")
        ([](const request &req, response &res, string filename){
            sendScript(res, filename);
        });

    char *port = getenv("PORT");
    uint16_t iPORT = static_cast<uint16_t>(port != NULL ? stoi(port) : 18000);
    cout << "PORT = " << iPORT << endl;
    app.port(iPORT).multithreaded().run();
}
```
* /styles/style.css anlegen
```css
body {
    background-color: blue;
}
```
* /scripts/test.js
```js
console.log("test");
```
* /images/test.jpeg anlegen
* index.html anpassen
```html
<!-- --->
    <link rel="stylesheet" href="styles/style.css">
    <script src="scripts/test.js"></script>
    <!-- -->
    <img src="images/test.jpg" />
<!-- -- >
```
#### 4 - Challenge: Create a new webpage
* about.html erstellen
```cpp
    CROW_ROUTE(app, "/about")
        ([](const request &req, response &res, string filename){
            sendHtml(res, "about");
        });
```

### 4 - Data Access
#### 1 - Creating an mLab account
* in Heroku anmelden
* Kongigure Add-Ons
    * mLab mongoDB (Sandbox - Free) auswählen 
    * Setting -> Review Configs Var -> in Config Vars kann man entsprechende VAR ansehen
    * in Overview auf mLab MongoDb klicken -> User für DB erstellen
#### 2 - Uploading JSON data
#### 3 - Adding the MongoDB C++ drivers
#### 4 - Querying Mongo data
#### 5 - Adding dynamic data to page
#### 6 - Challenge: Create a webpage with data

### 5 - REStful APIs
#### 1 - Create an endpoint
#### 2 - Parsing the path
#### 3 - Reading the query string
#### 4 - Converting to JSON data
#### 5 - Challenge: Create an endpoint

### 6 - WebSockets and Crow
### 1 - Reviewing the JS client code
### 2 - Creating C++ server code
### 3 - Running WebSocket on Heroku