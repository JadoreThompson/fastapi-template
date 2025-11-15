from runners import ServerRunner


if __name__ == "__main__":
    ServerRunner(host="0.0.0.0", port=8000, reload=False).run()