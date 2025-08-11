from django.shortcuts import render
from django.contrib import messages
import joblib
import os
from .preprocessing import preprocess_input

# Load models once when the module is imported
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "predictor", "ml_models", "salary_predictor.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "predictor", "ml_models", "scaler.pkl")

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except FileNotFoundError as e:
    print(f"Error loading models: {e}")
    model = None
    scaler = None


def predict_form(request):
    """
    Handle salary prediction form submission and rendering.
    
    Args:
        request: Django HTTP request object
    
    Returns:
        HttpResponse: Rendered template with prediction results
    """
    prediction = None
    
    if request.method == "POST":
        try:
            # Check if models are loaded
            if model is None or scaler is None:
                messages.error(request, "Prediction models are not available. Please contact support.")
                return render(request, "predictor/form.html", {"prediction": None})
            
            # Extract form data
            form_data = {
                'title': request.POST.get("title"),
                'years': request.POST.get("years"),
                'salaryDate': request.POST.get("salaryDate"),
                'companyCountry': request.POST.get("companyCountry"),
                'worktype': request.POST.get("worktype"),
                'workhour': request.POST.get("workhour"),
                'city': request.POST.get("city"),
                'currency': request.POST.get("currency")
            }
            
            # Preprocess the input data
            features = preprocess_input(form_data)
            
            # Scale the features
            features_scaled = scaler.transform(features)
            
            # Make prediction
            prediction_raw = model.predict(features_scaled)[0]
            
            # Format prediction (you can customize this based on your needs)
            if form_data['currency'] == 'EGP':
                prediction = f"{prediction_raw:,.0f} EGP"
            elif form_data['currency'] == 'USD':
                prediction = f"${prediction_raw:,.0f} USD"
            elif form_data['currency'] == 'AED':
                prediction = f"{prediction_raw:,.0f} AED"
            elif form_data['currency'] == 'SAR':
                prediction = f"{prediction_raw:,.0f} SAR"
            elif form_data['currency'] == 'EUR':
                prediction = f"€{prediction_raw:,.0f} EUR"
            else:
                prediction = f"{prediction_raw:,.0f}"
            
        except ValueError as e:
            # Handle validation errors from preprocessing
            messages.error(request, f"Input validation error: {str(e)}")
            prediction = None
            
        except Exception as e:
            # Handle any other unexpected errors
            messages.error(request, "An error occurred while processing your request. Please try again.")
            print(f"Prediction error: {e}")  # Log for debugging
            prediction = None
    
    return render(request, "predictor/form.html", {"prediction": prediction})