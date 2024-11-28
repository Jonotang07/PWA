from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

# Route for Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route for Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for Manifest File
@app.route('/manifest.json')
def manifest():
    return send_from_directory(app.static_folder, 'manifest.json')

# Route for Service Worker
@app.route('/service-worker.js')
def service_worker():
    return send_from_directory(app.static_folder, 'service-worker.js')

# Route for Icons (if necessary)
@app.route('/icons/<path:filename>')
def icons(filename):
    return send_from_directory(app.static_folder + '/icons', filename)

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
