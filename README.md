# gcp-nlp-task

* take the standup report, for each individual.
* save it using numerical scheme.
* 0-1.txt means that person 0's (sir zia in this case) report portion 'today'
* report portion scheme goes like this:
	* 0 = yesterday
	* 1 = today
	* 2 = obstacles
* for user ids, see /standup-reports/user_id.csv

## using the sentence.py:
* the report must be divided into sentences. because i have observed that every sentence contains one task (in case of yesterday and today) or obstacle (in case of obstacles part)
* for that purpose nltk library has been used.
* the additional number in 0-1-2.txt means '2'nd sentence of 'today' portion of user_id '0'.

### syntax.py
* used to import the builtin methods of GCP's NLP API.
