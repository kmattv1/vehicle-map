# Vehicle Map
This is a project that wraps an MVP of a React front end and a Python backend for frontend service.
Aim of the backend for frontend service is to gather every required information for the frontend and expose it via an endpoint.

## Product requirements:
* visualizing e-scooter data
  * location
  * availability
  * pricing information
* filtering on the visualised data based on
  * availability

## Assumptions:
* This is a simple tool that can be used to share the internal status with external users withouth authentication
* Information is read only in this tool
* Information does not need to be real time cached data can be used to decrease load on the downstream services

## Technical decisions:
* Backend:
  * Backend service could be a graphQL to provide flexibility on the client side iterations, on the other hand it would have its on cons because the backend itself would have less control on the load that it will push to the downstream services.
  * Using a REST API gives us clear visibility on the load we generate with eatch request.
  * Framework should be selected where self documentation is an out of the box feature based on annotations.
    * Selected framework is [FastAPI](https://fastapi.tiangolo.com)
* Frontend:
  * React with typescript will be used this will provide us type safety and a component based structure that can be considered as reusable component.

## Design decisions:
* To display the required information a map with clustering can be used.
* A sidebar should be able to fulfill the needs to display and set the filters with selectors.


## Configuration:
* .env file inside the backend folder contains the configuration of the backend application
* variables set in the .env file
  * DOWNSTREAM_URL
  * API_KEY

## Local dev setup:
* Make file contains commands to start separate parts of the app
  * make run_dev_all will start the backend for local dev and the frontend for local dev also
  * make backend_test will run the unit tests for the backend service


## Metrics and documantation:
* Metrics of the backend service can be accessed under the [/metrics](http://localhost:8000/metrics) endpoint
* API documantation of the backend service can be accessed under the [/docs](http://localhost:8000/docs) endpoint


## TODO:
* Deployment:
  * Add build step for the frontend and an additional step that would deploy it to S3
  * Containerize the python service and have a build and deploy step that would start it in ECS
  * Gateway that routes the frontend requests to the static store in S3
  * Gateway config to route api requests to the backend service that is running in ECS

* Frontend:
  * Fix typing problems that are disabled now by ts-ignore

* Testing:
  * Frontend has 0 tests and for the backend only the happy path is tested for the core logic of the service
  
* Performance improvements:
  * There is no cache in any layer of the current app a cahce layer could be adde:
      * Backend side to reduce load on the downstream service.
      * Cahce header added by the backend the could be used out of the box by the web browsers to reduce load on the backend service