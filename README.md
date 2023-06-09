# house_price_prediction
ML project

Creating conda virtual environment
```
conda create -p venv python==3.7 -y
```
Activate venv
```
conda activate venv/
```
Create requirements.txt file
```
pip install -r requirements.txt
```
## [GIT Documentation](https://git-scm.com/docs/gittutorial)

To add files to git
```
git add .

or

git add file_name
```
Note:- To ignore a file or folder add its name to .gitignore file

To check the git status
```
git status
```
To check all versions maintained by git
```
git log
```
To  create version / commit all changes by git
```
git commit -m "message"
```
To push version/changes to github
```
git push origin main
```
To check remote url
```
git remote -v
```

Build docker image
```
docker build -t <image_name>:<tagname> .
```
> Note :Image name for docker must be lowercase

To list docker image
```
docker images
```
Run docker imgae
```
docker run -p 5000:5000 -e PORT=5000 <image id>
```
To check running docker containers
```
docker ps
```
To stop docker container
```
docker stop <container_id>
```