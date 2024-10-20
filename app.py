from flask import Flask, render_template, request, redirect, session, url_for
import redis
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  


r = redis.Redis(host='redis', port=6379, decode_responses=True)


MUSEUM_IMAGES = ['louve.jpg.jpg', 'gallery.jpg.jpg', 'hall.jpg.jpg', 'elegant.jpg.jpg', 'tapestry.jpg.jpg', 'garden.jpg.jpg', 'door.jpg.jpg', 'image1.jpg.jpg', 'image2.jpg.jpg', 'image3.jpg.jpg', 'image4.jpg.jpg', 'image6.jpg.jpg']

@app.route('/')
def home():
    
    background_image = random.choice(MUSEUM_IMAGES)
    
    
    if 'username' not in session:
        return redirect(url_for('username_prompt'))
    
    
    leaderboard = r.zrevrange('leaderboard', 0, -1, withscores=True)
    
    return render_template('index.html', 
                           message="Hello Everyone, its Aaliyana here, Welcome to GalleryGo :)",
                           username=session['username'],
                           leaderboard=leaderboard,
                           background_image=background_image)

@app.route('/count')
def count():
    
    visits = r.incr('visit_count')
    return f"Number of visits: {visits}"

@app.route('/gamification')
def gamification():
    
    if 'username' not in session:
        return redirect(url_for('username_prompt'))

    
    username = session['username']
    r.zincrby('leaderboard', 1, username)

    
    leaderboard = r.zrevrange('leaderboard', 0, -1, withscores=True)
    
    return render_template('index.html', 
                           message="You've earned a point!", 
                           username=username,
                           leaderboard=leaderboard,
                           background_image=random.choice(MUSEUM_IMAGES))

@app.route('/username', methods=['GET', 'POST'])
def username_prompt():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))

    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>GalleryGo</title>
            <style>
                body {
                    background-image: url("/static/museum_images/flower.jpg.jpg");
                    background-size: cover;
                    background-position: center;
                    background-attachment: fixed;
                    font-family: 'Georgia', serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }

                .overlay {
                    position: absolute;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background-color: rgba(0, 0, 0, 0.5);  /* Semi-transparent dark overlay */
                }

                .centered-form {
                    background-color: rgba(255, 255, 255, 0.9);  /* Semi-transparent white box */
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
                    text-align: center;
                    max-width: 400px;
                    position: relative;
                    z-index: 2;  /* Ensure it's on top of the overlay */
                }

                .form-title {
                    font-size: 48px;
                    font-family: 'Playfair Display', serif;  /* Elegant serif font for title */
                    color: black;
                    margin-bottom: 20px;
                }

                .username-form input[type="text"] {
                    font-size: 18px;
                    padding: 10px;
                    width: 100%;
                    margin-bottom: 20px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }

                .username-form input[type="submit"] {
                    font-size: 18px;
                    padding: 10px 20px;
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 5px;
                    border: none;
                    cursor: pointer;
                }

                .username-form input[type="submit"]:hover {
                    background-color: #45a049;
                    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);  /* Hover effect */
                }
            </style>
        </head>
        <body>
            <div class="overlay"></div>
            <div class="centered-form">
                <h1 class="form-title">GalleryGo!</h1>
                <form class="username-form" method="post">
                    <input type="text" name="username" placeholder="Enter your username" required>
                    <input type="submit" value="Submit">
                </form>
            </div>
        </body>
        </html>
    '''



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  