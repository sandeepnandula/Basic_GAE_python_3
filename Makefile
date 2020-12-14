
env_active:
	source env/bin/activate

start:
	python main.py

deps:
	pip install -Ur requirements.txt

deploy-stage:
	gcloud app deploy app.yaml --project ${project_name} -q --no-promote -v ${ver}