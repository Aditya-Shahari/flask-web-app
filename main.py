from website import create_app

app = create_app()

# Only if you run this file and not import, then only run this application else it runs web server i.e app.run(debug=True)
# debug=True means after any edit in the python code rerun the webserver automatically

if __name__ == '__main__':
  app.run(debug=True)

