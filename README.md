# 🌍 AsarAI: Proof of Impact (PoI) Terminal
**By Team ByteNova | Google Solution Challenge 2026**

AsarAI isn't just a dashboard; it's a Multi-Modal Intelligence Engine. Built to tackle UN SDG 2 (Zero Hunger) and structural inefficiencies in NGO operations, AsarAI acts as a "Digital Bridge" to turn unstructured chaos (voice, photos, paper) into structured action using the Gemini 1.5 Flash long-context window.

---

## 🛑 The Problem
1. **The "Paper Grave"**: In Delhi, community needs aren't captured in spreadsheets; they are trapped in damp notebooks and messy voice notes. 
2. **Language Barriers**: Field reports are often in "Hinglish," making them hard for standard software to parse.
3. **Ghost Volunteers**: NGOs suffer from high operational churn when people sign up for the clout but don't show up.
4. **Reactive Operations**: NGOs only react to today's problem, missing the patterns of tomorrow's crisis.

---

## 💡 The Solution: Proof, Not Promises
AsarAI provides an immutable, trust-based ecosystem where you only get credit if you are physically there. We own the Reputation Layer by converting field work into a portable professional identity.

### ✨ Key Features

#### 🧠 Omni-Ingestion Engine
* **Audio Diaries**: Field workers record 30s voice notes (Hinglish/Hindi). The AI extracts location, need, and urgency from their tone. 
* **Context-Aware OCR**: Respects the "Paper Workflow" by allowing NGOs to snap photos of handwritten logs. Our AI doesn't just read the text; it structurizes it into clean, audit-ready data streams.

#### 🛡️ Proof of Impact (PoI) & Reputation Layer
* **Soulbound Tokens (SBT)**: We mint a permanent, non-transferable digital badge only when a volunteer's GPS matches the task location and the recipient scans their QR code. 
* **Data-Backed Impact Certificate**: Generates certificates showing quantitative achievements (e.g., hours served) and verified skills.
* **Automated Security Tier**: Integrates Aadhaar/e-KYC to verify identities and scans 3,000+ Indian e-courts for past convictions.

#### 🗺️ Smart Resource Allocation
* **Predictive Resource Heatmaps**: Links volunteer data with weather APIs to predict where problems will be tomorrow.
* **Smart Evidence Score**: AI cross-references visual data with location patterns to provide a proven "Urgency" rating. 
* **Dynamic Standby Management**: Uses a 12-hour "Confirmation Pulse" to rank waitlisted volunteers by reliability and automatically reassign slots if a volunteer backs out.

#### 🤝 NGO Collaboration & Kitchen Hub
* **Kitchen Discovery Layer**: Register community kitchens (temples, SHGs) with GPS, capacity, and current stock status.
* **Smart Allocation for Kitchens**: Auto-alert verified volunteers for cooking/distribution shifts based on proximity and skill.
* **Community Feedback System**: Beneficiaries can report issues, rate help received, and close the feedback loop. 
* **Auto-Generated Reports**: One-click generation of weekly impact analysis (PDF/Excel) for collaborative NGOs.

---

## 🛠️ The Tech Stack (ByteNova)
Our architecture is split into four distinct logic blocks:
* **The Engine (Python)**: The "Intelligence Pipeline" using one API call to Gemini for translation, OCR, and urgency scoring.
* **The Pulse (React)**: A live heatmap of Delhi showing "Impact Clusters".
* **The Logic (C++)**: Highly efficient logic block for the volunteer matching algorithm.
* **The Vault (SQL/Firebase)**: Secure storage for volunteer "Trust Tokens" and reports.
* **Blockchain (Polygon/Solana)**: Layer 2 integrations for gasless, high-speed token minting via Account Abstraction.

---

## 🚀 Getting Started (MVP Demo)

### Prerequisites
* Node.js (v18+)
* Python 3.10+
* Google Gemini API Key
* Firebase config file

### Installation
1. Clone the repository:
        git clone https://github.com/ananyajoshi-cseai/ByteNova.git

2. Install frontend dependencies:
        cd client
        npm install

3. Set up the Python AI Engine:
        cd backend
        pip install -r requirements.txt

4. Create a .env file in the root directory and add your API Keys:
        GEMINI_API_KEY=your_key_here
        FIREBASE_API_KEY=your_key_here

5. Run the development servers:
        # Terminal 1 (Frontend)
        npm start
   
        # Terminal 2 (Backend)
        python app.py

---

## 👥 Meet Team ByteNova
* **Ananya Joshi** - Intelligence Pipeline (Python), Database Architecture & AI Integration
* **Gargi Sharma** - Mapping UI (React) & Database (Firebase)
* **Anika Aggarwal** - Frontend Developer
* **Aashi Srivastava** - Bug Testing, Documentation & Security
