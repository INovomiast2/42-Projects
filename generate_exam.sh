#!/bin/bash

# Script made for generating a exam situation

# Exec Exam Rank 02
exec_rank_02 ()
{
    echo -e "You selected: \033[1;31mExam Rank 02\033[0m"
    sleep 1
    echo "Generating Exam Rank 02..."
    sleep 1
    # Now check if the folder exists
    if [ -d "ExamRank02" ]; then
        echo "Exam Rank 02 already exists."
        sleep 1
        echo -n "Do you want to overwrite it? (y/n) "
        read -r OVERWRITE
        if [[ $OVERWRITE == "y" || $OVERWRITE == "yes" ]]; then
            rm -rf ExamRank02
            mkdir ExamRank02
            # Run the script to generate the exam
            python3 core/generate_exam.py 02
            sleep 1
            exit
        else
            echo "Exam Rank 02 has not been generated."
            sleep 1
            exit
        fi
    else
        mkdir ExamRank02
        # Run the script to generate the exam
        python3 core/generate_exam.py 02
        sleep 1
        exit
    fi
}

# Clean all the screen
clear

# Show a stylish menu for selecting the exam to generate.
echo "Select a Exam to generate"
echo "<=======================>"
echo " 1. Exam Rank 02	       "
echo " 2. Exam Rank 03         "
echo " 3. Exam Rank 04         "
echo " 0. Exit                 "
echo "<=======================>"

echo -n "Selection: "
read -r EXAM_OPTION

case $EXAM_OPTION in
	1) exec_rank_02;;
	2) exec_rank_03;;
	3) exec_rank_04;;
	0) exit;;
	*) sleep 1 && echo "Option Selected is not Avaliable." && exit;;
esac

