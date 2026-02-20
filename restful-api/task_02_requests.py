#!/usr/bin/env python3
"""
Module pour consommer et traiter des données depuis JSONPlaceholder API.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Récupère tous les posts depuis JSONPlaceholder et affiche leurs titres.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Récupère tous les posts depuis JSONPlaceholder et les sauvegarde
    dans un fichier CSV (posts.csv) avec les colonnes id, title, body.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()

        # Structurer les données : garder uniquement id, title, body
        structured_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Écrire dans le fichier CSV
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_posts)
