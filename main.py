from flask import Flask, render_template, request, jsonify
from sketch_generator import Sketch  # Import your Sketch class from the previous example

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_feature', methods=['POST'])
def add_feature():
    data = request.get_json()
    feature = data.get('feature')
    description = data.get('description')

    sketch_artist = Sketch()
    sketch_artist.add_feature(feature, description)
    sketch_artist.generate_sketch()

    sketch_html = "<h2>Generated Sketch:</h2><ul>"
    for feat, desc in sketch_artist.sketch.items():
        sketch_html += f"<li><strong>{feat.capitalize()}:</strong> {desc}</li>"
    sketch_html += "</ul>"

    return jsonify({'sketch_html': sketch_html})

if __name__ == '__main__':
    app.run(debug=True)
