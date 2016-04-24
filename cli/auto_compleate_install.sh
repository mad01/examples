#!/usr/bin/env bash
if [[ $(basename $SHELL) = 'bash' ]];
then
    if [ -f ~/.bashrc ];
    then
        echo "Installing bash autocompletion..."
        grep -q 'ecli-autocompletion' ~/.bashrc
        if [[ $? -ne 0 ]]; then
            echo "" >> ~/.bashrc
            echo 'eval "$(_ECLI_COMPLETE=source ecli)"' >> ~/.ecli-autocompletion.sh
            echo "source ~/.ecli-autocompletion.sh" >> ~/.bashrc
            echo "source ~/.ecli-complete.sh" >> ~/.bashrc
        fi
    fi
elif [[ $(basename $SHELL) = 'zsh' ]];
then
    if [ -f ~/.zshrc ];
    then
        echo "Installing zsh autocompletion..."
        grep -q 'ecli-autocompletion' ~/.zshrc
        if [[ $? -ne 0 ]]; then
            echo "" >> ~/.zshrc
            echo "autoload bashcompinit" >> ~/.zshrc
            echo "bashcompinit" >> ~/.zshrc
            echo 'eval "$(_ECLI_COMPLETE=source ecli)"' >> ~/.ecli-autocompletion.sh
            echo "source ~/.ecli-autocompletion.sh" >> ~/.zshrc
        fi
    fi
fi
