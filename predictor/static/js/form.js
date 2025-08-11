// Add subtle animations and interactions
document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input, select');
    
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.style.transform = 'scale(1.02)';
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.style.transform = 'scale(1)';
        });
    });

    // Form submission animation
    const form = document.querySelector('form');
    form.addEventListener('submit', function(e) {
        const submitBtn = document.querySelector('.submit-btn');
        submitBtn.innerHTML = '⏳ Predicting...';
        submitBtn.style.background = 'linear-gradient(135deg, #6b7280, #9ca3af)';
    });
});

// Modal functions
function closeModal() {
    const modal = document.getElementById('predictionModal');
    if (modal) {
        modal.classList.remove('active');
        setTimeout(() => {
            modal.style.display = 'none';
        }, 300);
    }
}

// Close modal when clicking outside
document.addEventListener('click', function(e) {
    const modal = document.getElementById('predictionModal');
    if (modal && e.target === modal) {
        closeModal();
    }
});

// Close modal with Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeModal();
    }
});