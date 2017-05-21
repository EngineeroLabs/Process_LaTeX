FROM kaushalkishore/docker-centos-nginx-php
RUN yum install texlive -y

COPY src/ /var/www/
EXPOSE 443 80

CMD ["/start.sh"]