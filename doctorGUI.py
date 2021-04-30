"""
Program: doctorGUI.py
Author: Tyler Rodriguez
		 4/23/2021

GUI-based version of the doctor program from Chapter 5
"""

from breezypythongui import EasyFrame
import random

hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.", "Go on, go on...", "Care to expand on that?")

qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "you":"I", "am":"are"}

class Doctor(EasyFrame):

	def __init__(self):
		""" Sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Eliza 1967")

		self.addLabel(text = "Welcome to the Eliza Program", row = 0, column = 0, sticky = "NSEW").config(font = ("Arial", 16))

		self.message = self.addLabel(text = "What can I do for you today?", row = 1, column = 0, sticky = "NSEW")
		self.message.config(font = ("Times New Roman", 12))

		self.inputField = self.addTextField(text = "", row = 2, column = 0, width = 65)
		self.inputField.config(background = "lightyellow")

		# Bind the input text field to the same function as the command button
		self.inputField.bind("<Return>", lambda event: self.reply())

		self.addButton(text = "Submit", row = 3, column = 0, command = self.reply).config(background = "red", foreground = "white")

	def reply(self):
		"""Builds and returns a reply to the sentence entered in the GUI."""
		sentence = self.inputField.getText()

		probability = random.randint(1, 4)
		if probability == 1:
			self.message["text"] = random.choice(hedges)
		else:
			self.message["text"] = random.choice(qualifiers) + changePerson(sentence)
		self.inputField.setText("")

# definition of the changePerson() function
def changePerson(sentence):
	"""Replaces first person pronouns with second person pronouns."""
	words = sentence.split()
	replyWords = []
	# loop through the words array, and decide if the word the loop is examining needs to be replaced
	for word in words:
		replyWords.append(replacements.get(word, word))
	# now that the replyWords array has been built, let's turn it back into a string for returning
	return " ".join(replyWords)

# Definition of the main() function for program entry
def main():
	Doctor().mainloop()

# Global call to main()
main()