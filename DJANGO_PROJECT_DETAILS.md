# Django CI Project

A comprehensive Django project demonstrating CI/CD best practices with a multi-departmental structure.

## Project Overview

This project is a sample Django application that demonstrates proper project structure, testing practices, and CI/CD workflows. It includes four main applications representing different departments:

1. **Dashboard** - Overview and home page
2. **Engineering Department** - Manage engineers and their roles
3. **Marketing Department** - Manage marketing campaigns
4. **Sales Department** - Track sales leads and status

## Project Structure

```
django-ci/
├── config/                 # Main project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
│
├── dashboard/             # Dashboard app (overview)
│   ├── migrations/
│   ├── templates/
│   │   └── dashboard/
│   │       └── index.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── engineering_dept/      # Engineering department app
│   ├── migrations/
│   ├── templates/
│   │   └── engineering_dept/
│   │       ├── engineer_list.html
│   │       └── engineer_detail.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   │   └── Engineer model
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│       ├── EngineerListView
│       └── EngineerDetailView
│
├── marketing_dept/        # Marketing department app
│   ├── migrations/
│   ├── templates/
│   │   └── marketing_dept/
│   │       ├── campaign_list.html
│   │       └── campaign_detail.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   │   └── Campaign model
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│       ├── CampaignListView
│       └── CampaignDetailView
│
├── sales_dept/            # Sales department app
│   ├── migrations/
│   ├── templates/
│   │   └── sales_dept/
│   │       ├── lead_list.html
│   │       └── lead_detail.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   │   └── Lead model
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│       ├── LeadListView
│       └── LeadDetailView
│
├── templates/             # Global templates
│   ├── base.html         # Base template
│   ├── dashboard/
│   ├── engineering_dept/
│   ├── marketing_dept/
│   └── sales_dept/
│
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── Makefile              # Make targets for common commands
├── .gitignore            # Git ignore file
└── README.md             # Project README
```

## Models

### Engineer (engineering_dept)
- **name** (CharField): Engineer's full name
- **email** (EmailField): Engineer's email address
- **role** (CharField): Engineer's job role
- **created_at** (DateTimeField): Auto-generated creation timestamp

### Campaign (marketing_dept)
- **title** (CharField): Campaign name
- **budget** (DecimalField): Campaign budget amount
- **active** (BooleanField): Campaign status (default: True)
- **created_at** (DateTimeField): Auto-generated creation timestamp
- **updated_at** (DateTimeField): Auto-updated modification timestamp

### Lead (sales_dept)
- **company** (CharField): Company name
- **contact_name** (CharField): Contact person's name
- **status** (CharField with choices): Lead status
  - new: New lead
  - contacted: Lead contacted
  - converted: Lead converted to customer
- **created_at** (DateTimeField): Auto-generated creation timestamp
- **updated_at** (DateTimeField): Auto-updated modification timestamp

## Views

### Engineering Department
- **EngineerListView**: List all engineers with pagination (10 per page)
- **EngineerDetailView**: Display details of a specific engineer

### Marketing Department
- **CampaignListView**: List all campaigns with pagination (10 per page)
- **CampaignDetailView**: Display details of a specific campaign

### Sales Department
- **LeadListView**: List all leads with pagination (10 per page)
- **LeadDetailView**: Display details of a specific lead

### Dashboard
- **DashboardView**: Display project overview and quick navigation

## URL Routing

```
/                         - Dashboard home page
/engineering/             - List of engineers
/engineering/<id>/        - Engineer detail
/marketing/              - List of campaigns
/marketing/<id>/         - Campaign detail
/sales/                  - List of leads
/sales/<id>/             - Lead detail
/admin/                  - Django admin interface
```

## Testing

The project includes comprehensive tests covering:

- **Model Tests**: Verify model creation, string representations, and ordering
- **View Tests**: Verify view responses, templates, and context data
- **Integration Tests**: Test URL routing and template rendering

Run tests with:
```bash
python manage.py test
```

Run tests with coverage report:
```bash
make coverage
```

## Installation and Setup

### Prerequisites
- Python 3.8+
- pip

### Steps

1. **Clone the repository:**
```bash
git clone <repository-url>
cd django-ci
```

2. **Install dependencies:**
```bash
make install
# or
pip install -r requirements.txt
```

3. **Run migrations:**
```bash
make migrate
# or
python manage.py migrate
```

4. **Create a superuser (admin account):**
```bash
make createsuperuser
# or
python manage.py createsuperuser
```

5. **Run the development server:**
```bash
make runserver
# or
python manage.py runserver
```

6. **Access the application:**
- Web interface: http://localhost:8000/
- Admin interface: http://localhost:8000/admin/

## Available Make Commands

| Command | Description |
|---------|-------------|
| `make install` | Install all dependencies from requirements.txt |
| `make migrate` | Run database migrations |
| `make test` | Run the test suite |
| `make coverage` | Generate a coverage report |
| `make lint` | Run flake8 code style checks |
| `make shell` | Open Django interactive shell |
| `make runserver` | Start the development server |
| `make clean` | Clean up Python cache files and directories |
| `make createsuperuser` | Create a new admin user |
| `make help` | Display all available commands |

## Admin Interface

The Django admin interface is available at `/admin/` for managing:
- Engineers
- Campaigns
- Leads

All models have been registered with custom admin configurations including:
- List display customization
- Search capabilities
- Filtering options

## Dependencies

### Core
- **Django >= 4.2**: Web framework

### Testing & Quality
- **pytest-django >= 4.5.2**: Testing framework integration with Django
- **pytest >= 7.0.0**: Python testing framework
- **coverage >= 7.0.0**: Code coverage measurement
- **flake8 >= 5.0.0**: Code style checker

## CI/CD Integration

This project is designed to work with CI/CD pipelines. Key features:

- **Automated Testing**: All tests run automatically
- **Code Coverage**: Coverage reports are generated
- **Code Quality**: Flake8 linting checks code style
- **Database Migrations**: Automatically run during deployment

## Development Workflow

1. Create a feature branch
2. Make code changes with corresponding tests
3. Run `make test` to verify tests pass
4. Run `make lint` to check code style
5. Run `make coverage` to verify coverage
6. Commit changes and create a pull request
7. CI/CD pipeline automatically tests and deploys

## Environment Variables

No environment variables are required for basic development, but you can configure:

- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: List of allowed hosts
- `SECRET_KEY`: Django secret key (generated by default)
- `DATABASE_URL`: Database connection string

## Production Considerations

For production deployment:

1. Set `DEBUG = False` in settings
2. Update `SECRET_KEY` to a strong random value
3. Configure `ALLOWED_HOSTS` properly
4. Set up a production database (PostgreSQL recommended)
5. Configure static files serving
6. Set up proper logging and monitoring
7. Use environment variables for sensitive configuration

## Contributing

1. Create a feature branch
2. Write tests for new features
3. Ensure all tests pass
4. Run linting checks
5. Submit a pull request

## License

This project is provided as a sample for educational and CI/CD demonstration purposes.

## Support

For issues or questions, please create an issue in the repository or contact the development team.
