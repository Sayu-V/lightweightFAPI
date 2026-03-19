

# 💰 Lightweight Finance API

A simple and lightweight Finance API built using **FastAPI** to demonstrate how backend systems process requests and return JSON responses.

---

## 📌 Project Objective

To build a lightweight API that:

* Accepts financial data (income & expense)
* Processes it using backend logic
* Returns structured JSON responses

---

## 🚀 Features

* Add Income
* Add Expense
* Get Financial Summary
* Budget Tracking (Optional)

---

## 🛠 Tech Stack

* Python
* FastAPI
* Postman (API Testing)
* Uvicorn (Server)

---

## 📂 Project Structure

```
finance_api/
├── main.py
├── models.py
├── services.py
├── data_store.py
├── requirements.txt
```

---

## 🔌 API Endpoints

| Method | Endpoint       | Description     |
| ------ | -------------- | --------------- |
| POST   | /income        | Add income      |
| POST   | /expense       | Add expense     |
| GET    | /summary       | Get summary     |
| GET    | /budget-status | Budget analysis |

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🧪 Testing

Use **Postman** to test endpoints.

---

## ☁️ Cloud Concept

This API is designed to be:

* Stateless
* Lightweight
* Easily deployable to AWS Lambda / Azure Functions

---

## 📄 Documentation

* [Proposal](docs/PROPOSAL.md)
* [HLD](docs/HLD.md)
* [LLD](docs/LLD.md)

---

## 👨‍💻 Author

Sayu V

---

## 📌 License

This project is for academic purposes.
