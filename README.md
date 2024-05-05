# Repli-Insta

## Introduction

"Repli Insta" is a social website that provides posting, commenting, and likes.

Website: https://planabcd.site/
![index](./docs/index.png)


https://github.com/CSY-Betty/Repli2/assets/84286529/fb84aefe-3e43-4b79-9f55-f702e79e14b2



## Technique

### Frontend

-   Vue.js

### Backend

-   Django
-   AWS RDS MySQL
-   AWS S3
-   AWS CloudFront
-   Nginx

## Structure

### Data Flow Diagram

![creat_post](./docs/structure.png)

### ER diagram

![er_model](./docs/ER_diagram.png)

## Setting
### .env File
Create a .env file in the repli_backend directory and add the following configurations:

```
# RDS
RDSuser=
RDSpassword=
HOST=

# S3
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
AWS_S3_REGION_NAME=
AWS_S3_CUSTOM_DOMAIN=
```
### Configuration Files
In server_files directory, are four configuration Files ,below

#### Nginx Configuration Files
nginx_apirepli.conf: This file contains the configuration settings for api django. It is typically located in /etc/nginx/sites-enabled/.
nginx_repli.conf: This file contains the configuration settings for static file. It is also located in /etc/nginx/sites-enabled/.

#### Gunicorn Configuration File
gunicorn_start.conf: This file contains configuration settings for Gunicorn, the WSGI HTTP server for Python web applications. It is located in /repli/venv/bin/.

#### Supervisor Configuration File

supervisor_repli.conf: This file contains configuration settings for Supervisor, a process control system for Unix-like operating systems. It is located in /etc/supervisor/conf.d/.

