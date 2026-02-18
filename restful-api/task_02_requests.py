#!/usr/bin/python3


import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"
structured_posts = []


def fetch_and_print_posts():
    """Fetch posts from the API and print their titles"""
    response = requests.get(API_URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))

def fetch_and_save_posts():
    """Fetch posts and save selected fields to posts.csv"""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            new_post = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"],
            }
            structured_posts.append(new_post)

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=["id", "title", "body"]
            )
            writer.writeheader()
            writer.writerows(structured_posts)

fetch_and_save_posts()
