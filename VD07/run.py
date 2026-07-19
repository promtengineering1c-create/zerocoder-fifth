from app import create_app

app = create_app()

if __name__ == '__main__':
    # debug=True позволяет серверу автоматически перезагружаться при изменении кода
    app.run(debug=True)