from flask import Flask, escape, request
from app import createApp

app = createApp()

if __name__ == "__main__":
    app.run()
