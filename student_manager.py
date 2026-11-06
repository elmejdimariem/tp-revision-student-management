def calculate_average(grades):
    """Return the average of a list of grades. Raise ValueError if empty."""
    if not grades:
        raise ValueError("La liste des notes est vide.")
    return sum(grades) / len(grades)


def get_mention(average):
    """Return the mention corresponding to the average."""
    if average < 10:
        return "Échec"
    elif average < 12:
        return "Passable"
    elif average < 14:
        return "Assez bien"
    elif average < 16:
        return "Bien"
    elif average < 18:
        return "Très bien"
    else:
        return "Excellent"


def is_admitted(average):
    """Return True if average >= 10, else False."""
    return average >= 10


def validate_grades(grades):
    """Return False if list is empty or any grade < 0 or > 20."""
    if not grades:
        return False
    return all(0 <= g <= 20 for g in grades)


# C. Test manuel
if __name__ == "__main__":
    notes = [12, 15, 18]
    average = calculate_average(notes)
    print("Moyenne :", average)
    print("Mention :", get_mention(average))
    print("Admis :", is_admitted(average))
    print("Notes valides :", validate_grades(notes))