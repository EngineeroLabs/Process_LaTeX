docker version for [EngineeroLabs/Process_LaTeX](https://github.com/EngineeroLabs/Process_LaTeX)(GPL)

client: [EngineeroLabs/latex_in_word](https://github.com/EngineeroLabs/latex_in_word)

mix with [kaushalkishorejaiswal/Docker-Centos-Nginx-PHP](https://github.com/kaushalkishorejaiswal/Docker-Centos-Nginx-PHP)(LGPL)

LGPL comes from Docker-Centos-Nginx-PHP

## for docker user

### build
```
git clone https://github.com/EngineeroLabs/Process_LaTeX
cd Process_LaTeX
git checkout docker
docker build -t your_docker_image_name . # this point is important
```
### run

```
docker run -d -p 8090:80 your_docker_image_name
```
 #this will bind your port 8090 to container's port 80. nginx run on 80 in the container.