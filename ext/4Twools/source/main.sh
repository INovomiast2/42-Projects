# MAIN.SH - 4Twools (A ToolSet for your 42 Experience)

# Important Functions
improved () {
	open https://bit.ly/impIntra
}

grade () {
	bash "$(curl https://grademe.fr)"
}

showHelp () {
	bash ~/Desktop/ext/4Twools/source/toolz/help.sh
}

setRepo () {
	# Make's a repo following the norma...
	if [ -d "./.git/" ]; then
		echo "[ERROR]: The current folder has a REPOSITORY on it!"
	else
		echo "[STATUS]: Creating Git Repo!"
		git init > /dev/null
		sleep 1;
		echo -e "[STATUS]: Repository Link: "
		read repo_link
		echo "[STATUS]: Setting Up the link to the Repo!"
		sleep 3
		echo "git remote add origin $repo_link"
		sleep 1
		echo "[STATUS]: Creating .gitignore..."
		touch .gitignore
		echo .DS_Store > .gitignore
		echo *.out >> .gitignore
		echo .gitignore >> .gitignore
		sleep 2
		echo "[CHECK]: Showing .gitignore..."
		sleep 1
		echo "[PRINT]:"
		git status --ignored
		sleep 1
	fi
}

# Check if params are passed the time of execution
if [ $# -eq 0 ]; then
	echo "[ERROR]: 4Twools - No tool name was passed!"
else
	case $1 in
		--getSubject) echo "getSubject!";;
		--makeRepo) setRepo;;
		--autoCorrect) echo "autoCorrect!";;
		--ghRepo) echo "ghRepo!";;
		--autoMake) echo "autoMake!!";;
		--findPeer) echo "findPeer!!";;
		--gradeMe) grade;;
		--impIntra) improved;;
		--syncNode) echo "syncNode!!";;
		--intraAuth) echo "intrAuth";;
		--api) echo "Api!!";;
		--help) showHelp;;
	esac	
fi
