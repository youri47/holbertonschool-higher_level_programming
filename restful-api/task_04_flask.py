#!/usr/bin/env python3
"""
Module pour créer une API simple avec Flask.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Endpoint racine - message de bienvenue."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Retourne la liste de tous les usernames stockés."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Retourne le statut de l'API."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Retourne les infos complètes d'un utilisateur par son username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Ajoute un nouvel utilisateur via une requête POST."""
    user_data = request.get_json(silent=True)

    # JSON invalide
    if user_data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = user_data.get("username")

    # Pas de username fourni
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Username déjà existant
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run()
