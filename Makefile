name = notebook
tag = ae5f7e104dd5

.PHONY: edit view
presentation.html: presentation.ipynb
	docker run --rm -v $(shell pwd):/home/jovyan/work jupyter/datascience-notebook:$(tag) ipython nbconvert --to slides work/presentation.ipynb --stdout | python ipy_hide_input > presentation.html

edit:
	docker run -it --name $(name) --rm -p 8888:8888 -v $(shell pwd):/home/jovyan/work jupyter/datascience-notebook:$(tag)

view: presentation.html
	docker run -it --rm -v $(shell pwd):/work -w "/work" -p 8000:8000 python:3.6-slim-stretch python -m http.server
