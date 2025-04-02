from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

DATABASE = 'personal_site.db'

# Function to get database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # So rows can be accessed like dictionaries
    return conn

# Blog route
@app.route("/blog")
def blog():
    conn = get_db_connection()
    posts = conn.execute("SELECT * FROM posts ORDER BY created DESC").fetchall()
    conn.close()
    return render_template("blog.html", posts=posts)

# Route to initialize a post (for testing)
@app.route("/init_post")
def init_post():
    conn = get_db_connection()
    conn.execute("INSERT INTO posts (title, content) VALUES (?, ?)", 
                 ("My First Blog Post", "This is a sample blog post about my project."))
    conn.commit()
    conn.close()
    return "Initial post added."

# Route to create a new post
@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        if not title or not content:
            flash("Title and content are required!", "danger")
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
            conn.commit()
            conn.close()
            flash("New post added successfully.", "success")
            return redirect(url_for('blog'))
    
    return render_template("new_post.html")


# Homepage route
@app.route("/")
def home():
    projects = [
        {"title": "Substance Abuse in Delhi",
         "desc": "Analyzed the rising prevalence of substance abuse in Delhi, identifying key drug trafficking hubs and trends in youth addiction, smuggling networks, and policy gaps. Evaluated the effectiveness of existing drug laws (NDPS Act, Nasha Mukt Bharat Abhiyan) and proposed policy reforms for stricter enforcement, rehabilitation access, and digital surveillance. Recommended AI-driven law enforcement strategies, expansion of rehabilitation centers, and youth engagement programs modeled on global best practices (Portugal, Iceland, Sikkim approach."},
         {"title": "Inflation Reduction Act (IRA) 2022",
         "desc": "Analyzed the key provisions of the Inflation Reduction Act (IRA) and its implications for economic and environmental policy such as climate action, healthcare affordability, and tax reforms. Provided insights on potential challenges and implementation strategies for effective policy outcomes."}
    ]

    experiences = [
        {"title": "Policy Research Intern | Niti Tantra",
         "desc": "Conducting in-depth policy research on India’s 2025 Union Budget, focusing on fiscal policies,economic reforms, and sectoral allocations to assess their implications on economic growth. Drafting policy briefs and recommendations on social sector reforms, contributing to data-backed policy making discussions.including the PM SVANidhi scheme, evaluating its impact on street vendors’ financial stability and market participation."},
        {"title": "Data Insight Head | Nblik",
         "desc": "Led a team of 8 data interns to analyze user engagement metrics using Amplitude Analytics,identifying key behavioral trends that improved app retention by 15%. Designed weekly data reports for management, offering actionable insights to refine product development and marketing strategies."},
        {"title": "Volunteer | Pratham Foundation, Chandigarh",
         "desc": "Conducted on-ground data collection and analysis for the Annual Status of Education Report (ASER) 2022, assessing schooling, learning levels, and living conditions of children aged 5-16 in rural areas."},
    ]

    return render_template("home.html", projects=projects, experiences=experiences)


# Contact form route
@app.route("/contact", methods=["POST"])
def contact():
    # Get form data
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Simulate form submission (In real apps, save to DB or send email)
    print(f"Received message from {name} ({email}): {message}")

    # Redirect back to home after submitting
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)