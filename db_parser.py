import sqlite3
from ast import literal_eval

def add_value(question, answer):
    db = sqlite3.connect("database.db")
    conn = db.cursor()
    answer = [answer]
    answer = str(answer)
    conn.execute("INSERT INTO messages VALUES(?, ?)", (question, answer,))
    db.commit()
    conn.close()
    
def get_answers(question):
    db = sqlite3.connect("database.db")
    conn = db.cursor()
    conn.execute("SELECT answer FROM messages WHERE question=?", (question,))
    answers = literal_eval(conn.fetchone()[0])
    db.commit()
    conn.close()
    return answers
 
    
def get_questions():
    db = sqlite3.connect("database.db")
    conn = db.cursor()
    conn.execute("SELECT question FROM messages")
    questions = conn.fetchall()
    db.commit()
    conn.close()
    return [question[0] for question in questions]
    
def add_answer(question, answer):
    db = sqlite3.connect("database.db")
    conn = db.cursor()
    answers = get_answers(question)
    answers.append(answer)
    answers = str(answers)
    conn.execute("UPDATE messages SET answer=? WHERE question=?", (answers, question,))
    db.commit()
    conn.close()
    

    