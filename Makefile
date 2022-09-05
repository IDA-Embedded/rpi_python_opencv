
.PHONY: export_requirements main  

PYTHON_VER=python3


export_requirements:
	$(PYTHON_VER) -m pip freeze > requirements.txt

main:
	$(PYTHON_VER) main.py


upload:
	./tools/to_rpi.sh
