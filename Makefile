WD := $(shell pwd)
VENV := $(WD)/../venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

.PHONY: generate_sdist
generate_sdist: clean_dist clean_build clean_egginfo
	$(PY) $(WD)/setup.py sdist

.PHONY: upload_sdist
upload_sdist:
	$(PY) $(WD)/setup.py sdist upload

.PHONY: clean_dist
clean_dist:
	rm -rf $(WD)/dist

.PHONY: clean_build
clean_build:
	rm -rf $(WD)/build

.PHONY: clean_egginfo
clean_egginfo:
	rm -rf $(WD)/src/*.egg-info
