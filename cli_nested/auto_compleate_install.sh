#!/usr/bin/env bash
if [[ $(basename $SHELL) = 'bash' ]];
then
    if [ -f ~/.bashrc ];
    then
        echo "Installing bash autocompletion"
        cp ecli-complete-nested.sh ~/.ecli-complete-nested.sh
        grep -q 'ecli-complete-nested' ~/.bashrc
        if [[ $? -ne 0 ]]; then
            echo "" >> ~/.bashrc
            echo "source ~/.ecli-complete-nested.sh" >> ~/.bashrc
        fi
    fi
elif [[ $(basename $SHELL) = 'zsh' ]];
then
    if [ -f ~/.zshrc ];
    then
        echo "Installing zsh autocompletion"
        cp ecli-complete-nested.sh ~/.ecli-complete-nested.sh
        grep -q 'ecli-complete-nested' ~/.zshrc
        if [[ $? -ne 0 ]]; then
            echo "" >> ~/.zshrc
            echo "autoload bashcompinit" >> ~/.zshrc
            echo "bashcompinit" >> ~/.zshrc
            echo "source ~/.ecli-complete-nested.sh" >> ~/.zshrc
        fi
    fi
fi
