# LangFlash - Validation Testing Report

## Purpose:
This document contains test case scenarios used to validate the functionality, input handling and overall behavior of the LangFlash application.

----

## Test Case 1: Add  Valid Flashcard
**Goal:** Test that the user can add a new English-Spanish flashcard
**Action:** Enter "apple" and "manzana" in input fields, click "Add Flashcard"
**Expected Result:** 
Flashcard is added to the list
Success messagebox: "Added: apple → manzana"
**Actual Result:** Success messagebox appreared. Flashcard saved to flashcards.json
**Screenshot:** 
![Add Flashcard Success](images/add_flashcard_success.png)  
<sub>*Figure 1: Flashcard successfully added after clicking ‘Add Flashcard’.*</sub>

----

## Test Case 2: Add Flashcard with Empty Fields
**Goal:** Test that the user cannot add flashcards with empty fileds
**Action:** User clicks "Add Flashcard" with both fields left empty
**Expected Result:** 
Warning message: "Both fields must be filled!"
**Actual Result:** Warning popup displayed
**Screenshot:**
![Add Empy Flashcards](images/add_flashcard_empty_warning.png)  
<sub>*Figure 2: Warning message appears when attempting to add with empty fields.*</sub>

----

## Test Case 3: Start Quiz with Fewer Than 4 Flashcards
**Goal:** Test that the program needs to have 4 or more flashcards to start a quiz
**Action:** Only 2 flashcards exist. User clicks "Start Quiz."
**Expected Result:** 
Message on screen: "Add at least 4 flashcards to play the quiz
**Actual Result:** Quiz doesn't start. Message is displayed.
**Screenshot:**
![Less Than 4 Flashcard Quiz](images/quiz_too_few_flashcards.png)  
<sub>*Figure 3: Message shown when user tries to start quiz with < 4 cards.*</sub>

----

## Test Case 4: Answer Quiz Question Correctly
**Goal:** Test that a question is answered correctly on the quiz
**Action:** User selects the correct answer from four multiple-choice options.
**Expected Result:** 
Messagebox shows: "Correct! Nice Job!"
Score updates (e.g., Score: 1/1)
**Actual Result:** Correct answer message displayed
**Screenshot:**
![Quiz Correct Answer](images/quiz_correct.png)  
<sub>*Figure 4: Confirmation popup after answering correctly.*</sub>

----

## Test Case 5: Answer Quiz Question Incorrectly
**Goal:** Test that a question is answered incorrectly on the quiz
**Action:** User selects an incorrect option from four choices.
**Expected Result:** 
Messagebox shows: "The correct answer was:___"
Score updates (e.g., Score: 0/1)
**Actual Result:** Incorrect answer message displayed
**Screenshot:**
![Quiz Incorrect Answer](images/quiz_incorrect.png)  
<sub>*Figure 5: Feedback after incorrect answer in quiz.*</sub>