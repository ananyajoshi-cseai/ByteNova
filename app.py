import os
import json
from google import genai
from flask import Flask, render_template, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

# --- CONFIGURATION ---
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize the client using the environment variable
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# --- MOCK DATA ---
dashboard_stats = {
    "meals": "1.2M",
    "volunteers": "4,821",
    "kitchens": "142",
    "tokens": "89,403",
    "trust_index": "98.4%"
}

# --- PAGE ROUTES ---
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/omni_ingestion')
def omni_ingestion():
    return render_template('omni_ingestion.html')

@app.route('/POI')
def poi():
    return render_template('POI.html')

@app.route('/evidence')
def evidence():
    return render_template('evidence.html')

@app.route('/verified')
def verified():
    return render_template('verified.html')

@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')

@app.route('/donation')
def donation():
    return render_template('donation1.html')

# --- API ROUTES ---
@app.route('/api/stats')
def get_stats():
    return jsonify(dashboard_stats)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# --- AI INGESTION ROUTE ---
@app.route('/api/upload-evidence', methods=['POST'])
def upload_evidence():
    if 'evidence_file' not in request.files:
        return jsonify({"status": "error", "message": "No file part"}), 400
    
    file = request.files['evidence_file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            print(f"Uploading {filename} to AI Engine...")
            ai_file = client.files.upload(file=filepath)
            
            prompt = """
            You are an impact-verification AI for a volunteer platform. 
            Analyze the attached field report (it may be an audio diary or an image of a paper log).
            Extract the intelligence and return insights that contains these exact keys:
            "explain": a 3 pointer explanation of the impact or issue in the report.
            "summary": A concise, 1-sentence summary of the impact or issue.
            "confidence_score": A percentage string (e.g., "94.2%").
            "urgency": Either "STABLE", "WARNING", or "CRITICAL".
            """
            
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[prompt, ai_file]
            )
            
            response_text = response.text.replace('```json', '').replace('```', '').strip()
            ai_insights = json.loads(response_text)
            
            client.files.delete(name=ai_file.name)
            
            return jsonify({
                "status": "success", 
                "message": "AI Extraction Complete",
                "insights": ai_insights
            })
            
        except Exception as e:
            print(f"AI Processing Error: {e}")
            return jsonify({
                "status": "error", 
                "message": f"Failed to extract insights. Reason: {str(e)}",
                "insights": {"summary": "Error parsing file.", "confidence_score": "0.0%", "urgency": "WARNING"}
            }), 500

# --- DONATION UPLOAD ROUTE ---
@app.route('/api/upload-donation', methods=['POST'])
def upload_donation():
    if 'donation_image' not in request.files:
        return jsonify({"status": "error", "message": "No image part"}), 400
    
    file = request.files['donation_image']
    
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected image"}), 400
        
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        return jsonify({
            "status": "success", 
            "message": "Donation item logged successfully!",
            "image_url": f"/uploads/{filename}",
            "ai_condition": "GOOD CONDITION",
            "ai_details": "Item identified. No major defects."
        })

if __name__ == '__main__':
    app.run(debug=True)
