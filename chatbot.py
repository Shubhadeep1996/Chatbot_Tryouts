#!/usr/bin/python3
import os
import aiml
from flask import Flask
from flask import render_template

k = aiml.Kernel()

PARSE_FILE="bot.dump"

print("This is not the final chatbot, Only a test run of all types of data and integration")
print("The final product may vary from the current one, It will be more complete @Group1")
print("Team members: \n@Shubhadeep Naskar \n@Aditya Ranjan \n@Karunendra Singh \n@Shivam Dutta Purkayashta")

print("Parsing aiml files")
k.learn("std-startup.xml")
k.respond("load aiml b")
print("Saving parse file: " + PARSE_FILE)
k.saveBrain(PARSE_FILE)

# Endless loop 
while True:
    input_text = input(">Query: ")
    response = k.respond(input_text)
    print(">VIKI: "+response)


#Starting WebPage setup

# for filename in os.listdir("Scripts"):
# 	if filename.endswith(".aiml"):
# 		k.learn("Scripts/" + filename)

# app = Flask(__name__)


# @app.route("/")
# def index():
# 	return render_template("index.html")


# @app.route("/<query>")
# def Bot_API(query):
# 	return k.respond(query)


# if __name__ == "__main__":
# 	app.run(debug=True, port=4673)

#This is not a Final product
#It is just a test run, will be improved on a letter session
