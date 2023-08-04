# Paper Trader

Paper Trader is a web application that allows users to gather real-time stock and financial instrument data, view price trajectory graphs, and perform simulated buying and selling of stocks and financial instruments, including cryptocurrencies. The application is built using Django for the backend and HTML, JavaScript, CSS, and Bootstrap for the frontend. It utilizes the Yahoo Finance library to gather data for stocks and financial instruments.

## Features

- Real-time stock and financial instrument data with current prices.
- Price trajectory graphs to visualize historical stock data.
- Simulated buying and selling of stocks and financial instruments.
- Search functionality using stock symbols (e.g., BTC-USD for Bitcoin).

## How to Run the Project Locally

1. Download the source code from the repository.
2. Open the terminal and navigate to the project folder.
3. Install the required dependencies using `pipenv`:

```bash
pipenv install
```

4. Activate the virtual environment:

```bash
pipenv shell
```

5. Run the Django development server:

```bash
python manage.py runserver
```

6. Access the application by opening your web browser and navigating to `http://localhost:8000`.

## Requirements

- Python 3.10 or higher
- Django 4.2.3
- Yahoo Finance library
- Bootstrap 5.3.0-alpha1

## Contributing

We welcome contributions to improve Paper Trader. If you'd like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name for your feature or bug fix.
3. Make your changes and commit them with clear commit messages.
4. Push your branch to your forked repository.
5. Submit a pull request, detailing the changes you made.

## Known Issues

- There might be occasional issues with data retrieval from Yahoo Finance due to API limitations.
- The application currently supports simulated trading and does not involve real money transactions.

## Future Plans

- Implement user authentication and user-specific portfolios.
- Enhance the frontend design and user interface.
- Expand support for more financial instruments and data sources.
