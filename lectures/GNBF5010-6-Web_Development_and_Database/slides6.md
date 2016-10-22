name: inverse
layout: true
class: middle, inverse

---
.title[Web Development and Database]

.author[Gang Chen]

.author[chengangcs@gmail.com]

---
# Outline

* Introduction to HTTP
* CGI: A Simple Website in Python
* Data Persistence: File, SQL and NoSQL
* Web Site and Database
---

# HTTP: HyperText Transfer Protocol

---

## HyperText Transfer Protocol

* The Hypertext Transfer Protocol (HTTP) is an application protocol for distributed, collaborative, hypermedia information systems.
* HTTP is the foundation of data communication for the World Wide Web
* Hypertext is structured text that uses logical links (hyperlinks) between nodes containing text. HTTP is the protocol to exchange or transfer hypertext.
* HTTP functions as a request–response protocol in the client–server computing model.

---

## Server and Client

* http server and Client
* back-end and front-end
* Python, PHP, Java, Ruby ...
* HTML, CSS, JavaScript ...
---

# A Simple Website in Python

---

## Configuration
* http server: Python
* Client: browser
* backend: Python
* front-end: HTML

---

server.py:

````python
import http.server

def run(port = 8000,
        server_class = http.server.HTTPServer,
        handler_class = http.server.SimpleHTTPRequestHandler):
    httpd = server_class(('', port), handler_class)
    httpd.serve_forever()

run()
````
---
index.html:

````html
<html>
<head>
    <title>A Simple Website on Python Server</title>
</head>
<body>
    <h1>Hello Python</h1>
    A useful website is coming soon.
</body>
</html>
````
---
Dynamic

# Data Persistence: File and database

---

## Pickle and Shelve

Modules:
* pickle
* shelve

---

## SQL Databases

* What is database?
* What is SQL?
* RDMS
* NoSQL Databases
* Distributed Storage

---

# Website and Database

---

## Connecting to DB in Python

MySQL:
* pymysql for Python3
* Upgrade from files to database

---

## Web Development Frameworks

* Django
* Flask
