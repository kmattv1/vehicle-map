run_dev_backend:
	cd backend && uvicorn main:app --reload

run_backend:
	cd backend && uvicorn main:app