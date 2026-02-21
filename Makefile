.PHONY: install run test clean

install:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

run:
	. venv/bin/activate && python app.py

test:
	. venv/bin/activate && python -m pytest tests/ -v

clean:
	rm -rf venv __pycache__ *.pyc debug.log
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
