server {

    listen 80;

    root /var/www/html;
    index index.nginx-debian.html;
    server_name 3.80.78.149 ec2-3-80-78-149.compute-1.amazonaws.com www.ec2-3-80-78-149.compute-1.amazonaws.com;
    return 301 https://$host$request_uri;

}

server {

    listen 443 ssl http2 default_server;
    include snippets/self-signed.conf;
    include snippets/ssl-params.conf;

}
