from flask import Flask, render_template, request
from student_manager import (
    calculate_average,
    get_mention,
    is_admitted,
    validate_grades,
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        raw = request.form.get("grades", "").strip()
        if not raw:
            error = "Veuillez saisir au moins une note."
        else:
            try:
                grades = [float(x.strip()) for x in raw.split(",") if x.strip() != ""]
            except ValueError:
                error = "Format invalide : utilisez des nombres séparés par des virgules."
                grades = None

            if grades is not None:
                if not validate_grades(grades):
                    error = "Notes invalides : chaque note doit être entre 0 et 20."
                else:
                    avg = calculate_average(grades)
                    result = {
                        "average": avg,
                        "mention": get_mention(avg),
                        "admitted": is_admitted(avg),
                    }

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)