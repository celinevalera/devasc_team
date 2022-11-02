from flask import Flask, jsonify,request

app = Flask(__name__)
movies = [
    {
        "name": "Kingsman: The Golden Circle",
        "actors" : ["Taron Egerton","Colin Firth", "Julianne Moore", "Mark Strong"],
        "genres" : ["Action","Spy"]
    },
    {
        "name": "Barbie in the 12 Dancing Princesses",
        "actors" : ["Kelly Sheridan","Catherine O'hara"],
        "genres" : ["Fantasy","Romance"]
    },
    {
        "name": "The Golden Compass",
        "actors" : ["Dakota Richards","Nicole Kidman", "Daniel Craig"],
        "genres" : ["Fantasy","Adventure"]
    }

]

@app.route('/movies', methods=['GET'])
def getMovies():
    return jsonify(movies)

@app.route('/movies', methods=['POST'])
def addMovie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)},200

if __name__ == '__main__':
    app.run()

