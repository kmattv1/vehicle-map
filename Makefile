run_dev_backend:
	cd backend && uvicorn main:app --reload

run_backend:
	cd backend && uvicorn main:app

backend_install_dependencies:
	cd backend && pip3 install -r requirements.txt

backend_install_run: backend_install_dependencies run_backend