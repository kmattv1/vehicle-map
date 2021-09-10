run_dev_backend:
	cd backend && uvicorn main:app --reload

run_backend:
	cd backend && uvicorn main:app

backend_install_dependencies:
	cd backend && pip3 install -r requirements.txt

backend_install_run: backend_install_dependencies run_backend

backend_test:
	cd backend && python3 -m unittest discover -s 'tests' -p '*_test.py'

run_dev_frontend:
	cd frontend && npm start

run_dev_all:
	make run_dev_backend & make run_dev_frontend