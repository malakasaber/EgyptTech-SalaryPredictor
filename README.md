# Egyptian Software Market Salary Analytics & Predictive Modeling 💰

A comprehensive data science project that analyzes salary trends in Egypt's tech industry and provides predictive modeling capabilities through an interactive web application.

## 🎯 Project Overview

This project tackles the common dilemma faced by job seekers: **"What should I ask as expected salary?"** by providing data-driven insights and machine learning predictions based on real market data from Egypt's software industry.

### Key Features
- **📊 Salary Analytics**: Comprehensive analysis of salary trends across different roles, experience levels, and work types
- **🤖 ML-Powered Predictions**: Random Forest model with R² > 0.8 for accurate salary predictions  
- **🎨 Interactive Dashboard**: Beautiful visualizations and filters for exploring salary data
- **🌐 Web Application**: Django-based deployment with modern UI/UX
- **📈 Market Insights**: Actionable insights for job seekers, employers, and HR professionals

## 🏗️ Project Architecture

```
Egyptian-Salary-Analytics/
├── predictor/                 # Django app
│   ├── ml_models/            # Trained models (RandomForest + Scaler)
│   ├── preprocessing.py      # Data preprocessing utilities
│   ├── views.py             # Django views
|   ├── static/                  # CSS, JS, and assets
│   └── templates/           # HTML templates
├── mywork/                  # Project documentation & notebooks
│   ├── notebooks/           # Jupyter notebooks for EDA & modeling
│   └── documentation/       # Complete project documentation
│   └── datasets/       # uncleaned dataset extracted from google form, cleaned dataset I worked on
|   └── dashboard/               # Interactive dashboard files

```

## 📋 Project Planning & Execution

### Planning Phase
I followed a structured approach documented in my **Notion workspace**:

🔗 **[Project Planning & Tracking - Notion](https://www.notion.so/Tech-Mind-Internship-Graduation-Project-24cf44c8d585801cafaff23ba1d15f29?source=copy_link)**

The planning covered:
- **Business Objectives**: Clear problem definition and success metrics
- **Stakeholder Analysis**: Job seekers, employers, HR teams, and analysts
- **Timeline Management**: 5-day structured development cycle
- **Resource Planning**: Tools, technologies, and deliverables

## 📊 Data Source & Processing

### Original Dataset
- **Source**: Egypt Tech Salaries 2025 Survey Data
- **Format**: Google Forms responses (~1,000 records)
- **Original Data**: [Google Drive Link](https://docs.google.com/spreadsheets/u/0/d/1y0bDNtCUy2qvsC-OzetFbIrDOoimNwvQmvpvFWZHB1U/htmlview?fbclid=IwQ0xDSwMDHX5leHRuA2FlbQIxMAABHhDOhbBwtKvf_dEOAdm24NWWMqE1jYEByhW-rwrc3-BStHqSJtYbdTcfJiWR_aem_JdHL6caN497qP4musDMU0w)

### Data Pipeline
1. **Data Cataloging**: Initial schema analysis and quality assessment
2. **Data Cleaning**: Handled inconsistent formats, missing values, and Arabic text
3. **Feature Engineering**: Job title categorization, currency normalization, date parsing
4. **Preprocessing**: Encoding, scaling, and feature selection

## 🎨 Interactive Dashboard

Explore the data through our comprehensive dashboard:

🔗 **[Live Dashboard - Power BI](https://1drv.ms/u/c/b392fe7e56c67368/ETTP2Tx5xxJPrUNF2vJxPMQB-gz9_n2dLTzZTIAzvztVmA?e=6K2Bbo)**

### Dashboard Features:
- **Salary Distribution**: By experience, job title, and work type
- **Geographic Analysis**: City-wise salary comparisons  
- **Trend Analysis**: Market trends over time
- **Interactive Filters**: Drill down by multiple dimensions

## 🤖 Machine Learning Model

### Model Performance
- **Algorithm**: Random Forest Regressor
- **Performance**: R² Score > 0.8
- **Features**: 10 engineered features including job category, experience, location, work type
- **Deployment**: Integrated into Django web application

### Model Architecture
```python
Features Used:
├── Years of Experience
├── Job Category (7 categories)
├── Company Country Type
├── Work Type (Remote/Hybrid/On-site)
├── Work Hours (Full-time/Part-time)
├── City
├── Currency
└── Date Components (Day/Month/Year)
```

## 🌐 Web Application

### Live Application
Experience the salary predictor:

🔗 **[Salary Predictor Web App](NoneInProduction)**

### Key Features:
- **Modern UI/UX**: Glassmorphism design with smooth animations
- **Real-time Predictions**: Instant salary predictions based on user input
- **Responsive Design**: Works seamlessly across all devices
- **Input Validation**: Comprehensive error handling and user feedback

### Technology Stack:
- **Backend**: Django 4.x
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **ML**: scikit-learn, pandas, numpy
- **Deployment**: -
- **Database**: SQLite (development) / PostgreSQL (production)

## 📚 Documentation & Research

### Complete Documentation
Detailed project documentation including methodology, findings, and technical specifications:

📄 **[Complete Project Documentation](./mywork/documentation/Complete_Project_Documentation.pdf)**

### Jupyter Notebooks
Explore the analysis and modeling process:
- **[Data Exploration & Cleaning](./mywork/notebooks/01_data_exploration.ipynb)**
- **[Model Development](./mywork/notebooks/03_model_training.ipynb)**

## 🔧 Installation & Setup

### Prerequisites
```bash
Python 3.8+
Django 4.x
pandas, numpy, scikit-learn
```

### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/egyptian-salary-analytics.git
cd egyptian-salary-analytics

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

### Project Structure Setup
```bash
# Create necessary directories
mkdir -p static/{css,js}
mkdir -p predictor/ml_models
mkdir -p mywork/{notebooks,documentation}

# Ensure models are in place
# Place your trained models in predictor/ml_models/
```

## 📈 Key Insights & Findings

### Market Analysis Results:
- **Experience Impact**: Clear correlation between years of experience and salary
- **Work Type Premium**: Remote positions show 15-20% salary premium
- **Geographic Variations**: Significant salary differences across Egyptian cities
- **Job Category Trends**: Software development roles command highest salaries
- **Currency Analysis**: USD-paid positions significantly higher than EGP

### Business Value:
- **For Job Seekers**: Data-driven salary expectations
- **For Employers**: Market-competitive compensation benchmarking  
- **For HR Teams**: Industry-standard salary bands and trends

## 🎯 Future Enhancements

- [ ] **Real-time Data Pipeline**: Automated data updates from job portals
- [ ] **Advanced ML Models**: Deep learning approaches for improved accuracy
- [ ] **Multi-country Support**: Expand analysis to other MENA markets
- [ ] **API Development**: RESTful API for third-party integrations
- [ ] **Mobile Application**: Native iOS/Android apps

## 👥 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Data quality improvements
- Model performance enhancements  
- UI/UX improvements
- Documentation updates

## 📞 Contact & Support

**Malak Ahmed Saber**
- LinkedIn: [https://www.linkedin.com/in/malak-ahmed-saber-26a37b288/]
- Email: malak.a.saber88@gmail.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Egypt's tech community for providing valuable salary data
- Open source contributors who made this analysis possible
- Survey participants who shared their compensation information

---

⭐ **Star this repository if you found it helpful!** ⭐

*Last updated: August 2025*
