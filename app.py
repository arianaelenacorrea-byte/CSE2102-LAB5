from flask import Flask, request, jsonify 

app = Flask(__name__)
subscribers = {}

@app.route('/add-subscriber', methods=['POST'])
def add_subscriber():
    data = request.get_json()
    if not data or 'name' not in data or 'URI' not in data:
        return jsonify({"error": "Invalid input, 'name' and 'URI' are required"})
    name = data['name']
    uri = data['URI']
    subscribers[name] = uri
    print(f"Added susbriber: {name} at {uri}")
    return jsonify({"message": f"Suscriber {name} added successfully."}), 201
@app.route('/list-subscribers', methods=['GET'])
def list_subscribers():
    names = list(subscribers.keys())
    return jsonify(names), 200
@app.route('/delete-subscriber', methods=['DELETE'])
def delete_subscriber():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Invalid input, 'name' is required"}), 400

    name = data['name']
    if name in subscribers:
        del subscribers[name]
        print(f"Deleted subscriber: {name}")
        return jsonify({"message": f"Subscriber {name} deleted."}), 200
    else:
        print(f"Subscriber not found for deletion: {name}")
        return jsonify({"error": "Subscriber not found"}), 404
@app.route('/update-subject', methods=['POST'])
def update_subject():
    data = request.get_json()
    if not data or 'subject-update' not in data:
        return jsonify({"Invalid input, 'subject-update' is required"}), 400
    subject = data['subject-update'] 
    print(f"Subject updated: '{subject}'. Notifying {len(subscribers)}") 

    for name, uri in subscribers.items():
        print(f"-> Notifying subscriber '{name}' at {uri} with subject: '{subject}'") 
    return jsonify({"message": f"Subject updated and {len(subscribers)} subscribers notified"}), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)