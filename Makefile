ch:
	rm -rf file.json __pycache__  models/__pycache__ tests/__pycache__ models/engine/__pycache__
ps:
	git add $1
	git commit -m "$2"
	git push --set-upstream origin $3
