# Flask API

Flask is a micro web framework for Python that allows developers to build web applications quickly and with minimal boilerplate code. It is lightweight, flexible, and easy to use, making it a popular choice for creating APIs (Application Programming Interfaces) in Python. Flask provides the tools needed to handle HTTP requests and responses, routing, session management, and more, while still giving developers the freedom to structure their applications as they see fit. It follows the WSGI (Web Server Gateway Interface) specification, making it compatible with a wide range of web servers and deployment options.

When building APIs with Flask, developers typically define routes that map HTTP methods and URLs to Python functions, known as view functions. These view functions generate HTTP responses based on the incoming requests, allowing developers to define custom logic for handling API endpoints.

Overall, Flask provides a solid foundation for building APIs in Python, offering a balance of simplicity, flexibility, and performance that makes it well-suited for a wide range of web development tasks.

- **WSGI** – Web Server Gateway Interface, it helps to communicate between the server and web applications.
- **Jinja 2** – Web templating system.

# FastAPI

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. It was created to address the need for a framework that combines high performance with ease of use and developer productivity. FastAPI leverages Python's type system to provide automatic data validation, serialization, and documentation, making it a powerful tool for building robust and well-documented APIs.

## Key Features of FastAPI

- **Fast**: FastAPI is built on top of Starlette and Pydantic, which are two asynchronous-friendly libraries known for their performance. This allows FastAPI to handle high loads and deliver responses with low latency.
- **Type Safety**: FastAPI uses Python type hints to automatically validate request data and generate documentation. By annotating function parameters and return types with Python types, FastAPI can automatically validate incoming requests and convert data to the expected types, reducing the likelihood of runtime errors.
- **Automatic Documentation**: FastAPI generates interactive API documentation automatically based on the Python type hints used in your code. This documentation is generated using OpenAPI (formerly Swagger), making it easy to understand and explore API endpoints without the need for manual documentation.
- **Asynchronous Support**: FastAPI fully supports asynchronous programming, allowing you to write asynchronous code using Python's async and await syntax. This enables developers to build highly scalable and efficient applications that can handle concurrent requests with ease.
- **Dependency Injection**: FastAPI provides a built-in dependency injection system that allows you to easily manage dependencies and share common resources across different parts of your application. This makes it easy to modularize your code and keep it organized.

## Installation

First install the required packages:

```bash
pip install fastapi
pip install uvicorn

uvicorn image_fast:app --reload
