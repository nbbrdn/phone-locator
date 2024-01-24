# phone-locator

![ci](https://github.com/nbbrdn/phone-locator/actions/workflows/ci.yml/badge.svg)

Phone Info Lookup is a Django web application that allows users to determine the mobile operator and region based on a phone number.

## Features

- **Phone Number Lookup:** Enter a phone number to retrieve information about the associated mobile operator and region.
- **Asynchronous Data Update:** Periodically updates the database with operator and region information using Celery tasks.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Celery
- Redis

### Installation

1. Clone the repository:

```bash
git clone https://github.com/nbbrdn/phone-locator
cd phone-locator
```

2. Copy `.env.example` to the `.env` and change default parameters:

```bash
cp .env.example .env
```

3. Build and run Docker containers:
```bash
docker-compose up -d --build
```

4. Apply migrations:
```bash
docker-compose exec web python manage.py migrate
```

5. Download DEF codes

6. Enable the daily DEF codes download task

## Usage

1. Open the application in your web browser (http://127.0.0.1:8000/).
2. Enter a valid 11-digit phone number in the provided form.
3. Click the "Search" button to retrieve information about the mobile operator and region associated with the phone number.

## Contributing

If you would like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: git checkout -b feature-name.
3. Make your changes and commit them: git commit -m 'Add new feature'.
4. Push to the branch: git push origin feature-name.
5. Create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
