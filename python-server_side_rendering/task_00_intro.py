#!/usr/bin/env python3
"""Module for generating personalized invitation files."""

import os


def generate_invitations(template, attendees):
    """Generate invitation files from a template and a list of attendees.

    Args:
        template: A string containing the template with placeholders.
        attendees: A list of dictionaries with attendee data.
    """
    # 1. Vérification des types
    if not isinstance(template, str):
        print(f"Invalid input: template is not a string, it is {type(template).__name__}.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Invalid input: attendees is not a list of dictionaries, it is {type(attendees).__name__}.")
        return

    # 2. Vérification des entrées vides
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Traitement de chaque participant
    for i, attendee in enumerate(attendees, start=1):
        output = template
        # Remplacement des placeholders
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            # Si la valeur est None ou absente → "N/A"
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        # 4. Écriture du fichier de sortie
        filename = f"output_{i}.txt"
        if os.path.exists(filename):
            print(f"{filename} already exists, skipping.")
            continue
        with open(filename, 'w') as f:
            f.write(output)
