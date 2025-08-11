import re
import numpy as np
from datetime import datetime

# Mappings
CURRENCY_MAP = {'EGP': 0, 'USD': 1, 'AED': 2, 'SAR': 3, 'EUR': 4}

WORKHOUR_MAP = {'Full Time': 1, 'Part Time': 0}

WORKTYPE_MAP = {'Remote': 0, 'On Site': 1, 'Hybrid': 2}

COMPANY_COUNTRY_MAP = {
    'Egyption and site in egypt': 0, 
    'Not Egyption but site in egypt': 1,
    'Else': 2,
    'Not Egyption and site out of egypt': 3,
    'Egyptian and site out of Egypt': 4
}

CITY_MAP = {
    'Cairo': 0, 'Multi Site': 1, 'Dubai': 2, 'Australia': 3, 'Alexandria': 4,
    'Kuwait': 5, 'Riyadh': 6, 'London': 7, 'Giza': 8, 'Jordan ': 9, 'California': 10,
    'Mansoura': 11, 'Manama': 12, 'Canada': 13, 'Beni Suef': 14, 'Berlin': 15, 'Lebnanon': 16,
    'Minya': 17, 'Tanta': 18, 'Else': 19, '6th of October': 20, 'Shiekh zayed': 21, 'USA': 22,
    'Jeddah': 23, 'Georgia': 24, 'Suez': 25, 'Poland': 26, 'Abu Dhabi': 27, 'Marsa Alam': 28,
    'New York': 29, 'Amman': 30, 'Obour City ': 31, 'New Administrative capital ': 32,
    'France': 33, 'Zagazig': 34, 'Vancouver': 35, 'Nasr City': 36, 'Warsaw': 37, 'Munich': 38,
    'Oman': 39, '10th of Ramadan': 40, 'Denmark': 41, 'Montreal': 42, 'Kuwait ': 43,
    'rabat': 44, 'Zurich': 45, 'Shorouk': 46, 'Baghdad': 47, 'Magdeburg': 48
}

# Typo corrections mapping
TYPO_MAP = {
    'deveoper': 'developer', 
    'developsr': 'developer', 
    'developei': 'developer',
    'dot net': '.net', 
    'fulkstack': 'fullstack', 
    'full-stack': 'full stack',
    'mern-stack': 'mern stack', 
    'front-end': 'frontend', 
    'back-end': 'backend',
    'font end': 'frontend', 
    'senuor': 'senior', 
    'engin': 'engineer',
}

# Job title categories and their keywords
JOB_CATEGORIES = {
    1: [  # Software Development
        'frontend', 'backend', 'full stack', '.net', 'php', 'java', 'developer',
        'engineer', 'react', 'angular', 'flutter', 'node', 'golang', 'vue',
        'ios', 'android', 'mobile', 'unity', 'unreal'
    ],
    2: [  # Data Science/AI
        'data', 'machine learning', 'ml', 'ai', 'bi', 'analytics',
        'scientist', 'bigdata', 'nlp', 'computer vision'
    ],
    6: [  # IT Support/Infrastructure
        'it support', 'network', 'system admin', 'infrastructure', 'security',
        'devops', 'cloud', 'cybersecurity', 'd365', 'crm'
    ],
    4: [  # Management/Product
        'product', 'project manager', 'scrum', 'team lead', 'owner', 'manager'
    ],
    3: [  # Quality Assurance
        'qa', 'qc', 'tester', 'testing', 'quality assurance', 'quality control'
    ],
    5: [  # Engineering (Non-Software)
        'mechanical', 'electrical', 'civil', 'embedded', 'biomedical',
        'electronics', 'automation', 'maintenance'
    ],
    7: [  # Business/Other
        'marketing', 'hr', 'accountant', 'sales', 'liaison', 'analyst', 'purchasing'
    ]
}


def clean_title(title):
    """
    Clean and normalize job title text.
    
    Args:
        title (str): Raw job title
    
    Returns:
        str: Cleaned job title
    """
    if not title:
        return ""
    
    title = title.lower()
    # Remove special characters and replace with spaces
    title = re.sub(r'[^\w\s]', ' ', title)
    # Replace multiple spaces with single space
    title = re.sub(r'\s+', ' ', title).strip()
    
    # Apply typo corrections
    for typo, correction in TYPO_MAP.items():
        title = title.replace(typo, correction)
    
    return title


def categorize_title(title):
    """
    Categorize job title based on keywords.
    
    Args:
        title (str): Job title to categorize
    
    Returns:
        int: Category number (0-7)
    """
    title = clean_title(title)
    
    for category, keywords in JOB_CATEGORIES.items():
        if any(word in title for word in keywords):
            return category
    
    return 0  # Default category for unmatched titles


def parse_date(date_string):
    """
    Parse date string and extract day, month, year.
    
    Args:
        date_string (str): Date in YYYY-MM-DD format
    
    Returns:
        tuple: (day, month, year) as integers
    """
    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        return date_obj.day, date_obj.month, date_obj.year
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}. Expected YYYY-MM-DD")


def validate_input_data(data):
    """
    Validate input data for required fields and correct values.
    
    Args:
        data (dict): Input data dictionary
    
    Returns:
        tuple: (is_valid, error_message)
    """
    required_fields = ['title', 'years', 'salaryDate', 'companyCountry', 
                      'worktype', 'workhour', 'city', 'currency']
    
    # Check for missing fields
    for field in required_fields:
        if field not in data or data[field] is None or data[field] == '':
            return False, f"Missing required field: {field}"
    
    # Validate years (should be numeric and positive)
    try:
        years = float(data['years'])
        if years < 0:
            return False, "Years of experience cannot be negative"
    except (ValueError, TypeError):
        return False, "Years of experience must be a valid number"
    
    # Validate mappings exist
    mapping_validations = [
        (data['currency'], CURRENCY_MAP, 'currency'),
        (data['workhour'], WORKHOUR_MAP, 'work hour'),
        (data['worktype'], WORKTYPE_MAP, 'work type'),
        (data['companyCountry'], COMPANY_COUNTRY_MAP, 'company country'),
        (data['city'], CITY_MAP, 'city')
    ]
    
    for value, mapping, field_name in mapping_validations:
        if value not in mapping:
            return False, f"Invalid {field_name}: {value}"
    
    # Validate date format
    try:
        parse_date(data['salaryDate'])
    except ValueError as e:
        return False, str(e)
    
    return True, ""


def preprocess_input(data):
    """
    Preprocess input data for machine learning model.
    
    Args:
        data (dict): Raw input data
    
    Returns:
        numpy.ndarray: Preprocessed feature array
    
    Raises:
        ValueError: If input validation fails
    """
    # Validate input data
    is_valid, error_message = validate_input_data(data)
    if not is_valid:
        raise ValueError(error_message)
    
    # Extract and process data
    title = data['title']
    years = float(data['years'])
    salary_date = data['salaryDate']
    company_country = data['companyCountry']
    work_type = data['worktype']
    work_hour = data['workhour']
    city = data['city']
    currency = data['currency']
    
    # Process title category
    category = categorize_title(title)
    
    # Parse date
    day, month, year = parse_date(salary_date)
    
    # Create feature array
    features = np.array([[
        years,
        COMPANY_COUNTRY_MAP[company_country],
        WORKTYPE_MAP[work_type],
        WORKHOUR_MAP[work_hour],
        CITY_MAP[city],
        CURRENCY_MAP[currency],
        category,
        day,
        month,
        year
    ]])
    
    return features


def get_feature_names():
    """
    Get the names of features in order.
    
    Returns:
        list: Feature names
    """
    return [
        'years',
        'company_country',
        'work_type',
        'work_hour',
        'city',
        'currency',
        'job_category',
        'day',
        'month',
        'year'
    ]


def get_mapping_info():
    """
    Get all mapping information for reference.
    
    Returns:
        dict: Dictionary containing all mappings
    """
    return {
        'currency': CURRENCY_MAP,
        'workhour': WORKHOUR_MAP,
        'worktype': WORKTYPE_MAP,
        'company_country': COMPANY_COUNTRY_MAP,
        'city': CITY_MAP,
        'job_categories': JOB_CATEGORIES,
        'typo_corrections': TYPO_MAP
    }