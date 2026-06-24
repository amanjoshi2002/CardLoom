# Cardloom

Cardloom is an AI-powered business card management platform that helps users convert physical business cards into structured digital data.

Simply scan or upload a business card, extract information using your preferred AI provider, review the results, and export the data when needed.

## Features

* Business card scanning and upload
* AI-powered information extraction
* Support for multiple AI providers
* Dynamic model selection
* Card management and organization
* Export data to Excel, CSV, or JSON
* FastAPI backend
* Swagger API documentation

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* React
* TypeScript

## Getting Started

Clone the repository:

```bash
git clone https://github.com/amanjoshi2002/CardLoom.git
cd cardloom
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Run the backend:

```bash
uvicorn backend.main:app --reload
```

Open API documentation:

```text
http://localhost:8000/docs
```

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a branch
3. Make your changes
4. Open a Pull Request

## License

MIT License
