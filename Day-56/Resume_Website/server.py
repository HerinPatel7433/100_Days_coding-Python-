from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    resume_data = {
        "name": "Herin Patel Sanjay Kumar",
        "title": "Computer Engineering Student & Developer",
        "location": "Gujarat, India",
        "university": "Indus University",
        "about": "I'm a 20-year-old developer currently expanding my expertise in software \
        development and web-based applications. I've recently tackled the 100 Days of Code \
        challenge, which gave me hands-on experience building everything from automation \
        scripts and GUI desktop apps to classic game clones. I'm passionate about building \
        end-to-end solutions and love the challenge of learning new tools.",
        "what_i_do": [
            "Python automation & scripting",
            "Web scraping (BeautifulSoup, Selenium)",
            "Database management & interactive web forms"
        ],
        "tech_stack": [
            "Python", "Flask", "Pandas", "NumPy", "Selenium", 
            "HTML5", "CSS3", "JavaScript", "TypeScript", 
            "Git", "GitHub", "Markdown", "Windows Terminal"
        ],
        "socials": ["Instagram", "LinkedIn", "X", "Email"]
    }
    
    return render_template('index.html', data=resume_data)

if __name__ == '__main__':
    app.run(debug=True)