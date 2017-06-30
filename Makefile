update-package:
	pip list --outdated | awk '{print $$1}' | xargs pip install --upgrade

install-package:
	pip install -r requirements.txt
