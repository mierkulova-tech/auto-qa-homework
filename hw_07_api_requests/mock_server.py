

from flask import Flask, request, jsonify

app = Flask(__name__)


employees: dict[int, dict] = {}
next_id = 1


@app.post("/employee/create")
def create_employee():
    global next_id
    data = request.get_json(silent=True) or {}

    required = ("company_id", "name", "position")
    missing = [f for f in required if f not in data]
    if missing:
        return jsonify({
            "detail": [{"loc": ["body", f], "msg": "Field required", "type": "missing"}
                       for f in missing]
        }), 422

    emp = {
        "id": next_id,
        "company_id": data["company_id"],
        "name": data["name"],
        "position": data["position"],
    }
    employees[next_id] = emp
    next_id += 1
    return jsonify(emp), 201


@app.get("/employee/info")
def get_employee():
    emp_id = request.args.get("id", type=int)
    if emp_id is None or emp_id not in employees:
        return jsonify({"detail": "Not found"}), 404
    return jsonify(employees[emp_id]), 200


@app.patch("/employee/change")
def change_employee():
    emp_id = request.args.get("id", type=int)
    if emp_id is None or emp_id not in employees:
        return jsonify({"detail": "Not found"}), 404

    data = request.get_json(silent=True) or {}
    employees[emp_id].update({k: v for k, v in data.items() if k != "id"})
    return jsonify(employees[emp_id]), 200


@app.post("/auth/login")
def login():
    return jsonify({"user_token": "local-mock-token"}), 200


if __name__ == "__main__":
    print("Mock API: http://127.0.0.1:8000")
    app.run(host="127.0.0.1", port=8000, debug=False)