from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock Data - Later, you'll fetch this from Firebase/SQL
dashboard_stats = {
    "meals": "1.2M",
    "volunteers": "4,821",
    "kitchens": "142",
    "tokens": "89,403",
    "trust_index": "98.4%"
}

@app.route('/')
@app.route('/home')
def home():
    # Passing the stats to your HTML
    return render_template('home.html', stats=dashboard_stats)

@app.route('/poi')
def poi():
    return render_template('POI.html')

@app.route('/evidence')
def evidence():
    return render_template('evidence.html')

@app.route('/verify-impact', methods=['POST'])
def verify_impact():
    # This is where the magic happens!
    # 1. Receive data from the frontend
    # 2. Call Gemini API (Gargi can help tune this part later)
    # 3. Update Firebase
    
    # For now, we just simulate a successful verification
    return redirect(url_for('verified'))

@app.route('/verified')
def verified():
    return render_template('verified.html')

@app.route('/profile')
def profile():
    return render_template('volunteer.html')

if __name__ == '__main__':
    app.run(debug=True)
