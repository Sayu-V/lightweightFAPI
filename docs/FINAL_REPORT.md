# 📄 Final Report

## Lightweight Finance API using FastAPI

---

## 1. Introduction

This project focuses on developing a lightweight Finance API using FastAPI. The API demonstrates how backend systems process requests and return JSON responses, which are fundamental concepts in cloud computing.

---

## 2. Objective

* Build a lightweight API using FastAPI
* Understand request-response lifecycle
* Implement JSON-based communication
* Demonstrate cloud-ready backend design

---

## 3. System Overview

The system follows a client-server architecture:

Client (Postman) → FastAPI → Business Logic → JSON Response

---

## 4. Features Implemented

* Add Income (`POST /income`)
* Add Expense (`POST /expense`)
* Get Summary (`GET /summary`)
* Set Budget (`POST /budget`)
* Budget Status (`GET /budget-status`)

---

## 5. Technology Stack

* Python
* FastAPI
* Uvicorn
* Docker
* Postman

---

## 6. Implementation Details

* Used FastAPI for building APIs
* Used Pydantic models for validation
* Data stored in memory (lists)
* Docker used for containerization

---

## 7. Testing

All endpoints were tested using Postman:

* Valid inputs → Success responses
* Invalid inputs → Validation errors

---

## 8. Results

The API successfully:

* Processes financial data
* Returns structured JSON responses
* Handles validation and errors

---

## 9. Cloud Computing Relevance

* Stateless API design
* JSON communication
* Serverless-ready architecture

---

## 10. Limitations

* No database (data not persistent)
* No authentication
* Single-user system

---

## 11. Future Enhancements

* Add database (PostgreSQL)
* Add authentication
* Deploy to cloud (AWS/Azure)
* Add frontend UI

---

## 12. Conclusion

The project successfully demonstrates the working of APIs in a cloud computing environment. It provides a strong foundation for building scalable backend systems.

---

## 13. References

* FastAPI Documentation
* Python Documentation
* Cloud Computing Concepts
