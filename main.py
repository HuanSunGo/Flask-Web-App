from website import create_app

app = create_app()

if __name__ == '__main__': 
    # allows to execute the code when when the file runs as a script, but not when it's imported as a module 
    app.run(debug= True)
