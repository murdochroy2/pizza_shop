# Pizza Shop

A simple Pizza Shop API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python
* Django

### Installing

1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
```

2. Navigate to the project directory

```bash
cd your-repo
```

3. Create a virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

4. Install the required dependencies

```bash
pip install -r requirements.txt
```

5. Migrate the database

```bash
cd your-project
python manage.py migrate
```

6. Run the development server

```bash
python manage.py runserver
```
## API Endpoints

The following API endpoints are available:

### Menu

- **GET** `/menu?name="<name>"`: Retrieve the details for a specific pizza

### Order

- **POST** `/menu/order/`: Place an order for a pizza

