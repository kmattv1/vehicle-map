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

## Documentation:
```
* Placeholder for backend documentation link
```

## Local dev setup:
```
* Placeholder for local dev setup
```

## Deployment:
```
* Placeholder for deployment
```